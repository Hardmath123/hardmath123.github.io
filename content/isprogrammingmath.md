So recently, Sarah Mei blogged that [programming is not math](http://www.sarahmei.com/blog/2014/07/15/programming-is-not-math/). Jeremy Kun [responded](http://j2kun.svbtle.com/programming-is-not-math-huh), pointing out that math is an integral part of programming.

I found both articles interesting, but I wanted to add my thoughts on some things both of them wrote. So here they are.

Let's start with math. Math feels like mining. You know there's gold somewhere below you. Perhaps it's some theorem you're trying to prove. Math is about digging in the right direction from the right spot in the massive network of tunnels we've already derived. And although you can dig in any direction, it's not always obvious how to proceed from where you are to your target. The most brilliant mathematicians are the ones who have the best intuition about which way to dig. Some directions are obviously less efficient than others—digging through a rocky bit is much harder (but a clever mathematician might notice that it's just a thin wall and there's gold on the other side).

For example, consider a problem like *"Find the area of a triangle with side lengths 39, 52, and 65."* This was on my math final back in 7th grade. We were taught the path that goes through Heron's formula. Calculate semiperimeter, multiply, square root. That's the long way through soft earth. Of course, if you haven't noticed already, there's an easier way. You notice that 39, 52, and 65 are all multiples of 13, which is suspicious. If you divide by 13, you get 3, 4, and 5 which is a Pythagorean triple! So this is just a right triangle scaled up by a factor of 13. So the area is just the half the product of the two smaller side lengths.

This was the short path through the rocky earth. You need intuition to even consider going that way; and that intuition isn't easy to acquire.

This is far from a perfect analogy, but it suffices to explain why a lot of people find math hard. Many schools teach you the paths to take, rather than the intuition you need to build up to be able to find them yourself.

I write all this to make a contrast with CS: *the majority of CS doesn't require mathematical rock-wall insights*. You simply need to be able to think about how to solve problems by breaking them into smaller problems. You never get 'stuck', because you can *always* reduce a problem you have to something else (even if it's an ugly brute-force solution). Math has dead ends and paths that circle back to where you were originally. Programming is like building a skyscraper: the only way is up.

This, I think, is why many people find programming easier than pure math.

> …computer science is not programming. At most academic CS schools, the explicit intent is that students learn programming as a byproduct of learning CS. Programming itself is seen as rather pedestrian, a sort of exercise left to the reader.
>
> -- Sarah Wei

I thought this was rather interesting. I have seen this idea in a lot of places, but I have the opposite viewpoint.

CS is a way to formalize programming concepts. Learning programming isn't a byproduct of learning CS, bur rather learning CS is a byproduct of learning programming. The more you have programmed, the more problems you have solved, and the more CS ideas you've internalized.

Here's an example. You have a curb 100 meters long. (Idealized) cars 3 meters long park randomly along the curb, one after another, until there's no space greater than 3 meters between any two cars. Write a program to simulate this many times and compute the average number of cars that can park.

Take a moment to try to envision this program.

If you took an awesome CS class, you should have ended up with something like this:

```scheme
(define (number-of-cars len)
    (if (< len 3) 0 ; can't park any cars, too short
        (+ 1        ; +1 for current car
            (let ((offset (random)))
                (+  ; compute number of cars on left and right side
                    (number-of-cars (* (- len 3) offset))
                    (number-of-cars (* (- len 3) (- 1 offset))))))))
```

Guess what? It's *tree recursion*, which is, surprise surprise, a classic 'CS concept'). But your programming mind didn't think of it as a tree recursion problem. CS formalizes the idea of tree recursion because it's so common in programming. It gives this idea a name, and lets you use this name when communicating with humans. It lets you use someone else's Tree implementation, knowing exactly what to expect. It gives you an overview of common ideas that expand on trees—binary search trees, or perhaps breadth-first searching.

But in the end, it's all programming that has been catalogued so that you can do math on it.

> I taught Ruby on Rails, which is a web programming framework; people came because they wanted to learn how to make websites. Because of those motivations, the curriculum had virtually no math.
>
> -- Sarah Wei

Ah, this brings up the topic of a really interesting discussion I had with some friends a while ago. Here's a summary:

There's a lot of CS to be learned by studying the Internet: networking, protocol design, language design, layout engines, and security are just a few.

But is setting up a web server really programming? We felt it's a distinction between building and assembling. Teaching someone how to make a web server with today's frameworks is more about teaching them Ruby syntax and the APIs, and less about algorithms and logic. It's not raw computer science, it's following some instructions and inputting your own values. Using a clay mold shouldn't count as sculpting.

As much as I admire initiatives to teach CS, I feel that we should be teaching the algorithmic beauty alongside the more practical day-to-day skills.

> Specifically, learning to program is more like learning a new language than it is like doing math problems.
>
> -- Sarah Wei

A lot of people talk about CS as math and language, but I've always felt that it's more like building a tower with LEGOs. Programming isn't about the language you use—it's about the paradigm. Once you understand classes and methods, learning a new language of the same paradigm is at best a weekend job. Instead, programming is about taking blocks you already have, and fitting them together. The language is just a medium to communicate with the computer; we could use punch cards, or command lines, or fancy graphical programming software. What matters is what that medium is communicating. Writing in general follows this, too—writing a good blog post requires an exciting idea to convey. Text is just a medium to communicate the idea.

> It helps even more that mathematics and programming readily share topics. You teach graph coloring for register allocation, linear algebra and vector calculus for graphics, combinatorics for algorithms.
>
> -- Jeremy Kun

Programming isn't about math you *implement*.

Understanding, for example, vector algebra to write a raytracer is important to know *what* you're doing, but it's not programming—programming is being able to know *how* to do it.

To be successful in the modern computing landscape, you need to know math because the ability to compute is enhanced by the ability to put computation in a mathematical context. Twenty or thirty years ago, you might have considered discrete math (parsing), calculus (waveforms), and trig (graphics) to be instrumental. Today, it's statistics (big data) and number theory (crypto).

### Conclusion

What I wanted to say—and ended up digressing in rambles along the way—was that the intrinsic difference between math and computing is that math needs you to have good taking-apart intuition, while programming needs you to have good putting-together intuition.

And so here's a parting thought: in my school, CS is lumped with all the other electives. Theater, drawing, photography, food, and auto tech are in the same category. Would you move CS to the math department? Hint: this isn't a trivial question!
