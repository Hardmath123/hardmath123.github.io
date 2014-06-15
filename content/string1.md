> It all began with the forking of the great pings...

Gandalf was trapped. Surrounded by malicious shell scripts, his only hope lay in `/rivendell`, which only granted access to the user group `Elves`.

He cd'd himself into `/rivendell` moments before a violent fork bomb exploded.

"Well, Elrond, it appears we have some visitors,"" he said, putting down his staff for a moment.

"Ah, Gandalf, a welcome sight in our time of need." Elrond appeared. He was perturbed—things must really be bad.

"As are you, my friend. The recent attacks are troubling. Not many dare attack a Sysadmin."

"Yes, indeed, they worry me, too," sighed Elrond, "the Dwarves sent word that their bitcoin mines in `/moria` were raided for valuable nonces."

"`/moria`? Don't they log all commands run there, ever since the Trolls of 1402775481?"

"Yes, Gandalf, I believe `/moria/log` contains information about everyone that tries to access `/moria`. I wonder…"

"Way ahead of you." `cat /moria/log`, chanted Gandalf. His staff started spewing hundreds of lines of information. "Argh, there's too much data! We'll never analyze it all manually." He flushed the smoke-words in a puff of `^C`.

"Just got word from the Dwarves—they said they flagged suspicious log messages with the word `suspicious` at the end."

"Good, so we don't have to filter it by hand. We can just `grep`."

"Grep? Is that another of those black spells you found in `/mordor`?"

"No, Elrond, `grep` is the purest of spells. Grep searches files." `grep suspicious /moria/log`, he shouted, and the staff started listing all log messages containing 'suspicious'.

```
3:12:12 legolas 'just visiting' suspicious
3:12:15 samwise 'lost my pony!' suspicious
3:12:18 saruman 'mwahahahaha!!' suspicious
3:13:53 gandalf 'meet a friend' suspicious
3:15:30 baggins 'where is sam?' suspicious
3:16:32 smeagol 'lost, we are!' suspicious
4:43:33 aragorn 'meeting gimli' suspicious
...
```
"Aha! 3:12:15—saruman's involved." Gandalf winked.

"Gandalf, this is still far too much output. The Dwarves think everyone who isn't a Dwarf is suspicious!"

"Ah, but you haven't seen the power of `grep` yet. What else do we know about the intruders' log messages?" Gandalf looked excited. Elrond did not approve.

"Well, let's assume they all said `mwahahahaha`"

"How many ha's were there, again?"

"It doesn't matter. We can `grep` by regexes, too." Gandalf picked up his infamous pipe, and smoked the first grep's output into a new charm: `grep suspicious /moria/log | grep -e "mwa\(ha\)*"`.

"The Kleene star operator `*` we used searches any number of the group before it."

"And those backslashes?"

"Escaping. Parentheses are special words in spell charms, you need to use backslashes to prevent them from accidentally burning a Hobbit-subdirectory or something."

```
3:12:18 saruman 'mwahahahaha!!' suspicious
3:12:18 azogorc 'mwahahaha....' suspicious
3:12:18 urukhai 'mwahahahahaha' suspicious
```

"Gandalf, I've got to hand it to you, you are the greatest—"

"—no time for that," interrupted Gandalf, "we've got to stop them before they get to Rivendell!"

"They'll never guess the password. We're safe for a bit."

"With all due respect, Elrond, it's trivial to guess it."

Elrond choked. "What?!"

"Shush. Knowing you, it's probably not Elvish—you're too clever for that. It's probably English."

"And knowing your memory, probably not more than a word." He got up and started pacing.

(`cat /usr/share/dict/words`, he chanted under his breath.)

"Gandalf, I swear upon sword, this password was forged by the high elves of—"

"—and between six and eight characters, I would guess…"

(`grep "^\w\{6,8\}$"`, he chanted. "This one's tricky. `^` means start of the word, `\w` means an alphabet, and `{6,8}$` mean 6-8 of those until the end.")

"Now we can be a bit clever. Elvish uses the `ui` sound a lot, I bet that's in there. Can't teach an old orc new tricks."

(`grep ui`, he chanted)

"Oh, and you've always been partial to vowels before words (your kids are Arwen, Aragorn, Elladan and Elrohir)"

(`grep "^\(a\|e\)"`, he chanted. "Start-of-word and then a or e. The `|` means or.")

"so that narrows it down to about…" He waved his wand about rapidly. "…Sixty-six."

"GANDALF!" Elrond's ears were turning red. MAybe his hair was, too. "You only get one chance at guessing, though," he added with a wry smile.

"Let's go through that list. Which one fits an Elf-king? It must be… yes…" Gandalf got up and whispered: "Altruism."

To be continued.
