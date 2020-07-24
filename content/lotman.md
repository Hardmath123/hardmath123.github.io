> "I do not know what 'poetical' is: is it honest in
> deed and word? Is it a true thing?" --- Lotman quoting Pushkin quoting Shakespeare in _As You like It, 3.3_.

How do I want to say this? Here is one way: Earlier this year, the world was _very surprised_ at a computer doing _very unsurprising_ things. The celebrated computer program, [OpenAI's GPT-3](https://arxiv.org/abs/2005.14165), is a _language model_, a machine learning model that (to simplify) outputs the statistically-likeliest completion of a sentence, much like the autocomplete on your iPhone keyboard. If we wrote the prefix

> The weather is warm and…

GPT-3 might output "sunny" or "humid" --- that would be probable and unsurprising. But it would likely not output "turtledove" --- that would be improbable and surprising. Of course, you can run this program again and again to sample more and more words, and thus generate long sequences of text.

- The weather is warm and [sunny]
- The weather is warm and sunny [so]
- The weather is warm and sunny so [let's]
- The weather is warm and sunny so let's [go]
- The weather is warm and sunny so let's go [to]
- The weather is warm and sunny so let's go to [the]
- The weather is warm and sunny so let's go to the [beach.]

In principle this is nothing new. There was a GPT-1 and a GPT-2, too, as you can imagine. But GPT-3 is bigger and better --- it has "read" an _enormous_ corpus of text to build up its database, and the model itself consists of _175 billion_ parameters (GPT-2 was a "mere" 1.5 billion parameters). Just training a model of this size is an exciting engineering accomplishment.

By virtue of its size, GPT-3 is extremely good at hallucinating text in this way. And this is where things begin to get uncanny. If you phrase your prompt as a question, GPT-3 reliably provides answers in complete sentences. If you phrase your prompt as a few coding examples, GPT-3 can generate software to build small user interfaces based on a description of what buttons you want. It can even generate convincing [hoax blog posts](https://maraoz.com/2020/07/18/openai-gpt3/). Don't worry, what you are reading right now is written by a human --- but it is probably not unreasonable to be a little concerned.

I think it is natural to ask whether it can generate "literary" text as well --- whether it is a kind of superintelligent monkey that _will_ generate _Hamlet_ if you ask it to. Now, it's pretty clear that GPT-3 is not quite a Great Automatic Grammatizer (I have written [in the past](fabula.html) about what _that_ may look like). But for short fragments, as lots of people have shown, it [isn't embarrassing either](https://www.gwern.net/GPT-3). And so, as we hurtle towards a future where statistically-sound "literary text" can be mass-produced, I have been thinking a lot about what "literature" is.

---

One set of thoughts comes from an unlikely (so to speak) source, which is the early-1970s literary theory of Yuri Lotman (or Jüri, or Jurij --- you choose how to spell it --- this becomes relevant soon). In _The Structure of the Artistic Text_ (1971, but I'm referencing Ronald Vroon's 1977 translation), Lotman connects Shannon's and Kolmogorov's quantitative theories of communication and entropy with the qualitative question _what is literature?_. At least, that is my understanding --- I'm not an expert in Russian literary theory or semiotics, but I'm trying my best.

Let's think back to one of Shannon's big ideas, which is that language is _redundant_, which means there are many ways to convey the same idea. Because of its redundancy, language is resilient to noise in the communication channel (such as loud music at a party). If I stprt intrdducinq mutnt1ons into my spellings, you can still more or less get the message. Similarly, most ideas can be paraphrased. Or, to put it differently, you can convey a concept in many different ways. That is, notions can be materialized into words in multiple fashions. If there were no redundancy in the language --- that is, if every combination of letters formed a different valid word, or if there were only one way to express each idea --- then this error-correction would be impossible. Imagine if each volume in Borges' Library of Babel was a meaningful masterpiece! Imagine spilling a teardrop on a page, only to change the meaning dramatically!

This redundancy is the reason why text is so _compressible_, why a ZIP file can be so small compared to the source it is compressing. You can just strip out the redundancy to get a smaller file: your disk's I/O channel has negligible noise compared to a loud party, and so the redundancy is not needed. (Any introductory theory-of-computation course touches on _Kolmogorov Complexity_, a kind of theoretical limit to compressibility in terms of computability: it turns out that Kolmogorov worked with language and literature as well.)

Perhaps this redundancy makes GPT-3's behavior a little less surprising (I hope that word "surprising" is accruing meaningfulness for you). The more redundancy a language has, the more about the statistical structure of language you can "learn" from data, and therefore the easier it is to predict likely completions. Indeed, [GPT models can be used to perform data compression](https://bellard.org/textsynth/sms.html).

Now, my understanding of Lotman's thesis is that _literature does not behave this way_. Literature is _more entropic_, which is to say, literature is _less redundant_. It is packed with meaning --- in fact, every choice is intentional and significant. Lotman argues that literature lives outside or above "ordinary" natural language; a work of literature creates its own "code," and each word takes on a heightened meaning in this code. To read literature is to learn to decipher this code. He writes, _The artistic text is an intricately constructed thought. All its elements are meaningful elements._ Once a text is composed, it is baked to an immutable, brittle crust. "The reader considers the text placed before him as the only possible text."

For example --- and this is my example, not Lotman's --- the repetition in a line from _Lear_

> No, no, no, no! Come, let's away to prison:

is exact and precise. Four times, no more, no less --- and each utterance of the word "no" is significant, dripping with intention. The raw sound "no" itself becomes a kind of meaningful sign, detached from its usual English-language semantics. You cannot, without losing meaning, compress that text as simply "4 x no."

Let me give you another example. Consider Roethke's "The Waking." It's a sestina, a poem built on repetition. Every other stanza ends with the same line.

> I wake to sleep, and take my waking slow.  
> I feel my fate in what I cannot fear.  
> **I learn by going where I have to go.**

This repeats.

> Of those so close beside me, which are you?  
> God bless the Ground! I shall walk softly there  
> **And learn by going where I have to go.**

Until, suddenly and jarringly (in the softest way possible), it doesn't.

> Great Nature has another thing to do  
> To you and me; so take the lively air,  
> **And, _lovely_, learn by going where to go.**

That word _lovely_ appears so deliberately in that line that its absence in the previous lines is conspicuous. As a result, those repeated lines, which seemed like repetitions, become conscious choices. Roethke could have said _whatever he wanted_ but he chose to repeat himself verbatim, without the word "lovely," in what Lotman might call a kind of "minus-device," a trembling vacuum, an absence with presence --- that in itself is meaning, that in itself holds entropy.

It would not do for Roethke to paraphrase those lines, either. "I educate myself by traveling where needed" has no impact. Because literary text is stripped of redundancy, even small mutations --- even semantics-preserving ones --- can dramatically affect the text. It's like compiling for embedded targets with `-O4`. Like `gcc`, Lotman does not believe you can paraphrase literature to get equivalent literature. You cannot re-tell a story, because there are no synonyms in the unique code of that particular work of literature. I am reminded of Borges' "Pierre Menard, Author of the Quixote," a short story wherein Menard _writes_ (not re-writes) _Don Quixote_.

> Pierre Menard did not want to compose _another_ Quixote, which surely is easy enough---he wanted to compose _the_ Quixote. Nor, surely, need one be obliged to note that his goal was never a mechanical transcription of the original; he had no intention of _copying_ it. His admirable ambition was to produce a number of pages which coincided---word for word and line for line---with those of Miguel de Cervantes.

Maybe, in light of the discussion above, these bizarre lines are a little less mystifying, a little more satisfying.

That brings me back to GPT-3, and the literary status of its output. Can we ever call a GPT-3-generated poem a work of literature? Well, following Lotman, let's instead ask this: how much information, really, does GPT-3 output? How entropic is GPT-3's output? And of course the answer is that GPT-3 is quite orderly in the grand scheme of things. "Whenever the text does not realize one of at least two possibilities," writes Lotman, "but automatically follows one, it loses its capacity to convey information." That is, every time GPT-3 argmaxes its way to a prediction predestined by its statistical model, which is really a synthesis of gigabytes and gigabytes of data, it is outputting --- well, nothing. No new information. The occasional choice made by the random sampling is the only "information" being produced, though it is hidden in the fluffy sheep-skin of statistically-unobjectionable prose. Indeed, if you were to measure the number of bytes read from `/dev/urandom` (or whatever RNG) by GPT-3 in the course of sampling, and analyze the relative probabilities predicted by the model, perhaps you would be able to compute a Shannon entropy --- or even a convincing literariness score --- for the output. I sense it would not be very high.

---

I want to end this piece with two notes.

First: I see a couple of problems with Lotman's theory --- again, I'm not a literary theorist by trade so I do not know whether he (or others) have addressed them.

1. How does Lotman account for the way early (oral) poetry, with its strict rhyme and metrical patterns, was designed to be memorized? Isn't the poetical form, in a very direct sense, optimizing itself for compression and therefore less entropic --- as if the redundancy were to harden the message against the noise of _time_ and _amnesia_? Or do these qualities themselves encode and exfiltrate information, like the [stress-patterns in Sanskrit verse](https://en.wikipedia.org/wiki/Sanskrit_prosody#Chandas_and_mathematics), or the knots knitted by the women in _A Tale of Two Cities_? Lotman spends some time at the beginning of Chapter 6 discussing how poetry removed itself from ordinary speech, and then prose removed itself from poetry, and therefore prose is twice-removed from ordinary speech. But that does not quite answer my question.
2. How does Lotman account for the fuzziness of texts --- for example, the many editions of _Hamlet_ that editors _to this day_ Frankenstein together to try to formulate a coherent whole? How does this theory stand in the absence of an original source text?

Second: Lotman means all this in a serious technical sense. As far as I can tell, he is not just borrowing scientific buzzwords to give legitimacy to an otherwise fuzzy theory. For example, he cites the quantitative work of Shannon and Kolmogorov directly, even though it was (even for the time) primitive. The preface to his book suggests rhetorically that the only way to test these theories would be to compute empirical metrics on an unthinkably large set of poems. Later Lotman suggests a kind of semantic analysis of poetry, but says

> The operations recounted above give only a general and deliberately rough semantic skeleton, since **a description of all connections arising in the text and of all extra-textual relations which could be ascertained would be an unrealistic task in terms of sheer volume.**

But today, we can do that --- take exactly those measurements that Lotman (and Kolmogorov and Shannon) could only have dreamed of! It is as if Lotman predicted the relativistic warping of the stars, and we had to wait decades for the eclipse to make the confirming observations. Practical technology has finally caught up to theory.

And so I think there is potential for unprecedented scholarship here. This is a question where deep learning enthusiasts and literary theorists and semioticians all have something valuable to say. I wonder what the conversation will be like? It is comforting to note that our hero Kolmogorov appeals as early as 1964,

> But real progress in this direction demands that cyberneticians [today's deep learning researchers?] take a greater interest in the humanities and learn more about them.
