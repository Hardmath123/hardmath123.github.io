In a desparate attempt to learn a little more about the brilliant, strange,
confusing, mystifying world we all live in, I have spent the past few weeks
reading about it. About camelids and Cavendish, about 17th-century piracy and
21st-century photography, about Betsy Ross and clause learning, about metric
structure and morse code.

Those last two subjects --- metric structure and morse code --- were Friday
night's reading, and as I read, I felt that familiar sensation you feel when
you notice big ideas intersecting. It's a tremendously exciting sensation, one
that invites you to think just a little harder about each idea, to probe just a
little more aggressively at their boundaries, until at last you can dig out the
connection from your intuition.

The connection in this case turned out to be simple: many morse code signs
correspond to [metric feet](https://en.wikipedia.org/wiki/Foot_%28prosody%29).
"A" or `.-` is an *iamb* ("To be or not to be"), "D" or `-..` is a *dactyl*
("Merrily, merrily, merrily, merrily"), "U" or `..-` is an *anapest* ("There
was once an old man in Peru..."), "M" or `--` is a *spondee* ("Rage, rage"),
and so on.

A practical result of this fact is that we can come up with nice metric
mnemonics for Morse code, and indeed [Wikipedians have already done
so](https://en.wikipedia.org/wiki/Morse_code_mnemonics). By remembering the
syllable stress patterns for such mnemonics, you can remember the dot-and-dash
pattern for the associated letter.

The real question, of course, is whether or not we can *automate* the search
for such mnemonics.

Armed with the [pronouncing](https://github.com/aparrish/pronouncingpy) Python
library (which feeds off of the [CMU Pronouncing
Dictionary](http://www.speech.cs.cmu.edu/cgi-bin/cmudict)), I decided to make
my own set of Morse code mnemonics. This set is optimized for CS students, and
was generated with the assistance of a simple computer program I named
*versificator*. Here it is --- enjoy!

---

| Letter | Morse  | Mnemonics                                |
| ------ | ------ | ---------------------------------------- |
| A      | `.-  ` | assert                                   |
|        |        | array                                    |
| B      | `-...` | bcrypt hashing                           |
|        |        | base64                                   |
| C      | `-.-.` | computation                              |
|        |        | CS major                                 |
| D      | `-.. ` | digital                                  |
|        |        | dithering                                |
| E      | `.   ` | eh?                                      |
|        |        | err...                                   |
| F      | `..-.` | Futamura                                 |
|        |        | fs_usage                                 |
| G      | `--. ` | GNU emacs                                |
|        |        | git checkout                             |
| H      | `....` | hullabaloo                               |
|        |        | Hewlett-Packard                          |
| I      | `..  ` | IP                                       |
|        |        | id                                       |
| J      | `.---` | JS? How sad!                             |
|        |        | moar jQuery                              |
| K      | `-.- ` | kilobyte                                 |
|        |        | kangaroo                                 |
| L      | `.-..` | linguistics course                       |
|        |        | legitimate                               |
| M      | `--  ` | malware                                  |
|        |        | Markov                                   |
| N      | `-.  ` | Nyquist                                  |
|        |        | nearley                                  |
| O      | `--- ` | oh my zsh                                |
|        |        | output file                              |
| P      | `.--.` | prevent errors                           |
|        |        | prometheus                               |
| Q      | `--.-` | QuickTime has crashed                    |
|        |        | quad-core machine                        |
| R      | `.-. ` | recursion                                |
|        |        | rotation                                 |
| S      | `... ` | sudoer                                   |
|        |        | scp                                      |
| T      | `-   ` | type                                     |
|        |        | tree                                     |
| U      | `..- ` | unsubscribe                              |
|        |        | undeclared                               |
| V      | `...-` | video game                               |
|        |        | visual mode                              |
| W      | `.-- ` | wget it                                  |
|        |        | Wilensky                                 |
| X      | `-..-` | LaTeX by Knuth                           |
|        |        | Xcode is slow                            |
| Y      | `-.--` | combinator                               |
|        |        | Yukihiro                                 |
| Z      | `--..` | Z3 solver                                |
|        |        | zip archiver                             |
