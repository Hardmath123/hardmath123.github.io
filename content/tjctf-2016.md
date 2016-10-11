I just realized that TJCTF happened a really long time ago, and so it's
probably okay for me to share these writeups. Enjoy.

# curvature2

> A CTF is a rough road 
>
> When you play on hard mode 
>
> My tactics are frugal 
>
> My weapon is Google 
>
> All I do is search for code 

The time is 2:00am. In the distance, you can hear the city breathe softly. It
is the sound of night: when the hackers like you rise from their sleeping bags
to reclaim what is rightly theirs.

You unholster your keyboard and turn off the safety.

You're trying to take a discrete log in an elliptic curve's group: a gnarly
beast so powerful, it is used by the Browsers to protect User Privacy. You
wonder briefly who put you up to this gig, and make a mental note to charge
them overtime. Discrete log? What are you, some sort of lumberjack?

There are two kinds of hackers: those that hack in style and those that get the
job done. You are the latter.

You rev up the ol' browser and go on a wild-Google-hunt for attacks on elliptic
curve discrete logs. Cryptographic protocols come and go, you say to nobody in
particular, but Google is here to stay. You swerve past some lecture notes and
duck a Wikipedia article; before anyone can say "Pollard Rho", you find Matthew
Musson's paper[0] which mentions a whole variety of attacks on the elliptic
curve discrete log. "Sweetheart," you say, pointing to the bean-shooter in your
holster, "me and my friend here think you'd better start talking."

The pages read like molasses; progress is slower than Windows XP. But just as
the rays of dawn begin to reach over the netscape to reveal golden cloud
computers, your luck changes. Turns out that there's an attack on the elliptic
curve discrete log problem which works when the size of the elliptic group is
equal to the size of the field over which the elliptic curve lives (a so-called
"anomalous" curve). The attack's by someone who thinks they're Smart---and you
ain't complaining.

You call up your friend Sage; you need to pull a favor. Sage confirms that your
curve is in fact anomalous. You tell him you owe him a drink and hang up. What
are friends for?

You don't mind a reasonable amount of trouble. But soon you realize that this
is not a reasonable amount of trouble. This is a downright unreasonable amount
of trouble, and you ain't takin' it. You're way too lazy to implement this
attack on your own. But you know someone down at Github's probably knows how to
whip it up. You order an "elliptic anomalous curve attack", and Github
obliges[1]. You tip the guy a star and drive off in the boiler before anyone
can ask any questions.

Back at the office, you substitute in your curve's parameters, and turn the
crank. Out comes a hex-encoded string shaped suspiciously like a flag.

"What is it?" asks Sage.

"Oh," you say, "just the stuff that dreams are made of."

You're good. You're very good.

[0] https://www.researchgate.net/file.PostFileLoader.html?id=5583faed6225ff040e8b458b&assetKey=AS%3A273804985602059%401442291603545

[1] https://gist.github.com/elliptic-shiho/e76e7c2a2aff228d7807

# luvmarkdown

Flag à la Grandma's Cookies

Preparation time: 3 hours
Serves: A team of 4

Ingredients:
- 1 vulnerable website, not too large
- 1 simulated user, freshly instantiated
- 1 pound of fresh XSS exploits

Step 1. Prepare a fresh exploit payload in JavaScript for the user to execute.
You want the flag's address. Poisoning the user's cookie to be yours would work
because the "recent" beacon would update when the user navigates away from the
flag page.

Step 2. Insert the exploit payload in a script tag, knowing that showdown
doesn't sanitize HTML. Report it so that the simulated user views it. See
nothing. Realize that there's a very strict CSP in place that prevents inline
JavaScript.

Step 3. Realize that the only way to inject the payload is by having it loaded
by existing code on the same origin. Realize that the "raw" url allows you to
serve an XSS payload on the same origin.

Step 4. Submit your payload to the markdown renderer, then save the URL. Create
a fresh submission that creates a script element whose source is that URL.
Submit and report. See nothing. Realize that inserting an element counts as
inline JavaScript, which the CSP hates.

Step 5. Notice that the client-side viewer code loads the markdown
renderer dynamically based on the value of a DOM element. Create a doppelganger
element with the same ID as the renderer-selection dropdown. Since this element
is spliced in before the actual dropdown, it gets selected by the viewer code.
Set this element's value property to the URL of your payload from (4). Submit
and report.

Step 6. Copy the URL that appears in the list of recently viewed pages. Visit
the URL to obtain the flag.

Step 7. Serve flag while hot (do not hoard). Bon appétit.

# tsundere

Once upon a time, there was a piece of Java bytecode. That Java bytecode felt
incomplete and unloved, but then she met a CTF team willing to help it. Though
busy seeking flags in foreign lands and CPU architectures, the CTF team felt a
moral obligation to help, and so it tried to help the Java bytecode discover
her true identity. However, it was too difficult to understand her in her
current form. So, the CTF team converted her to a format recognized by the
Jasmin assembler [0] and found her source.

Looking at the source, the CTF team knew exactly where she came from: even
without the four magic numbers she had forgotten, the team recognized the
undeniable signs of her being an md5 implementation which chunked input
matching [a-z0-9] in blocks of 5 and concatenated the checksums.

Happy at last with her new identity, it sent off the Java bytecode to find new
adventures in an exciting, beautiful world. But one task remained.

In under an hour, a parallelized md5 cracker revealed each of the twenty
cleartext blocks that produced the hash embedded within the Java bytecode's
soul. It was, unmistakably, the Flag the team had sought for so long.

Moral: Kindness is always repayed.

[0] http://jasmin.sourceforge.net/
