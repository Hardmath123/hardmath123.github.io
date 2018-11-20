// g++ -std=c++11 fast.cc ; ./a.out

#include <thread>
#include <queue>
#include <mutex>
#include <iostream>
#include <stdlib.h>

#include "digraphs.h"

using namespace std;

const int alphabet_size = 26;

// a permutation is a 26-element vector

int score(vector<int>& perm) {
  int answer = 0;
  for (size_t i = 0; i < 26; i++) {
    for (size_t j = 0; j < 26; j++) {
      answer += abs(perm[i] - perm[j]) * digraphs[i][j];
    }
  }
  return answer;
}

vector<int> get_perm(char* perm) {
  vector<int> answer(26);
  for (size_t i = 0; i < 26; i++) {
    answer[perm[i] - 'A'] = i;
  }
  return answer;
}

void swap(vector<int>& v, int x, int y) {
  int tmp = v[x];
  v[x] = v[y];
  v[y] = tmp;
}

void shuffle(vector<int>& v) {
  for (size_t i = 0; i < 26; i++) {
    swap(v, i, rand() % (26 - i) + i);
  }
}

void randomize(vector<int>& guess) {
  for (size_t i = 0; i < 26; i++)
    guess.push_back(i);
  shuffle(guess);
}

void print_perm(vector<int>& perm) {
  char out[27];
  for (size_t i = 0; i < 26; i++)
    out[perm[i]] = 'a' + i;
  out[26] = '\0';
  cout << score(perm) << "\t" << out << endl;
}

void worker(int& best, mutex& bestlock) {
  while (true) {
    vector<int> guess;
    randomize(guess);

    int old_score = score(guess);
    while (true) {
      for (size_t x = 0; x < 26; x++) {
        for (size_t y = 0; y < 26; y++) {
          swap(guess, x, y);
          int new_score = score(guess);
          if (new_score < old_score) {
            old_score = new_score;
            goto nextloop;
          } else {
            swap(guess, x, y);
          }
        }
      }
      break;
nextloop:
      old_score += 0;
    }
    bestlock.lock();
    if (old_score <= best && guess[0] < 13) {
      print_perm(guess);
      best = old_score;
    }
    bestlock.unlock();
  }
}

int main(int argc, char* argv[]) {
  char crown[27] = "XQKGBPMCOFLANDTHERISUWYJVZ";
  char naive[27] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  auto cr = get_perm(crown);
  print_perm(cr);
  cr = get_perm(naive);
  print_perm(cr);

  thread workers[32];
  int best = INT_MAX;
  mutex bestlock;
  for (thread& w : workers) {
    w = thread(worker, ref(best), ref(bestlock));
  }

  for (thread& w : workers) {
    w.join();
  }
}
