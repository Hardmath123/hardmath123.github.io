Almost any metric of work I've done---homework submitted, emails answered, hours
spent playing piano, number of Github commits---show a sharp drop in the past
two weeks. I pretty much spent every moment on a computer solving
[PicoCTF](http://picoctf.com) problems.

Pico was wonderful. It was an opportunity to do stuff I couldn't (legally) do
before, and learn stuff that many adults would hesitate to teach teenagers. I
also got to hang out with cool hackers on their IRC channel, and had an excuse
to stay up till 2am hacking.

I'm planning on putting up some quick writeups of the problems I loved. If you
haven't spent an hour or so with these problems, you won't have any clue what
I'm talking about (and chances are that I myself won't grok any of this a year
from now). Nevertheless, here goes.

### OBO

This problem caused too many people too many hours of pain.

The basic idea is that the programmer used `<=` instead of `<` wherever he was
iterating, so he has lots of off-by-one errors. In particular, when populating
his hex table, he has:

```c
for (i = 0; i <= 6; ++i) {
    hex_table['a' + i] = 10 + i;
}
```

This allows `g` to be a valid hex character. Yay.

Now he goes around checking whether or not all the password characters are hex,
and he tries to make sure that all hex chars are used at least once by
populating the array `digits`. But we can input `g` in the password, so we can
set `digits[16]` which overflows into `password`:

```c
int digits[16] = {0};
char password[64];
```

So far, so good. A `char` is one byte, and an `int` (on this setup) is 4 bytes.
So when we overflow an `int` onto `password`, we set the first four characters
of the array to `\x01\x00\x00\x00` (the bytes are reversed because
Endianness!). With that zero byte, we've effectively reset `password` to
`\x01`. So now we can input `\x01` as the confirmation and cheat the password
changer. Yay again.

Now what? It uses `system()` to call a Python script. Yuck. On the bright side,
it uses a relative file path for the Python file (the author probably didn't
test it in another working directory). So we simply `cd` into our home
directory and make a new Python script with the same name, with contents:

```python
print open('/home/obo/flag.txt').read()
```

When we send OBO the overflowed password, it runs this with the right privs and we win.

### Make a Face

This was my favorite challenge (I have a thing for web exploitation). My first
reaction was "CGI! Shell! This must be Shellshock!" Turns out they've patched
their Bash, though, so that didn't work.

The legitimate solution relies on the fact that Perl's `open()` is unsafe: you
can call it with a `|` at the end, and it *evaluates the argument in a shell*,
sending back the result.

The webpage essentially asks the server to open the file `{body part
type}{index}`, where `body part type` is one of `head`, `nose`, etc. and
`index` looks like `1.bmp`. So, of course, we can cheat by sending it `1.bmp;
ls|` and instead of a bitmap file, the server gets a directory listing.

This is pretty easy to try out with `curl`...but we get back gibberish. It
looks like there's some bitwise melding going on on the server that combines
the images. This dies when it gets `ls` output. So we just send *all* the body
part parameters the same bad index. It bitwise `&`s them together (i.e. nothing
happens) and we get the secret. Simple but beautiful.

### Steve's List

This was my other favorite challenge, because there were so many different
things you needed to simultaneously break to get shell. Also, I just love the
way they used CSS3 polyfills to make the `blink` tag work in non-ancient
browsers.

First, there's the cookie signing. Steve, in all his wisdom, is authenticating
cookies by maintaining a SHA1 signature of the cookie plus some secret nonce.
Turns out, this is pretty insecure because of a simple padding
message-extension hack. A quick Google search sends us [this blog
post](http://journal.batard.info/post/2011/03/04/exploiting-sha-1-signed-messages),
and they post some sample Python that gets the job done.

Though I recommend reading the blog post to actually understand what's going
on, the basic idea is that a SHA1 hash operates on an arbitrary number of
blocks. The state of the algorithm at the end of one block is the input to the
next block's hash (the input to the first block's hash is a well-known
constant).

You don't need to know the contents of the previous block to add another block.
So we manually pad the payload we have (that is, the cookie) and tack on our
own block. We can initialize the SHA state with the (known) hash of the first
block and then compute valid subsequent hashes without ever knowing the key.
Some quick modifications to the Python script given above let us forge
arbitrarily long messages.

And now for something completely different. The server reads each line of the
cookie, and unpacks it using PHP's `unserialize`:

```php
$settings_array = explode("\n", $custom_settings);
$custom_settings = array();
for ($i = 0; $i < count($settings_array); $i++) {
    $setting = $settings_array[$i];
    $setting = unserialize($setting);
    $custom_settings[] = $setting;
}
```

With forged objects, we can make it instantiate arbitrary objects at
will---PHP's serialization saves type information. Notice that the `Post` object
defines:

```php
function __destruct() {
    // debugging stuff
    $s = "<!-- POST " . htmlspecialchars($this->title);
    $text = htmlspecialchars($this->text);
    foreach ($this->filters as $filter)
        $text = $filter->filter($text);
    $s = $s . ": " . $text;
    $s = $s . " -->";
    echo $s;
}
```

So it will dump its contents in an HTML comment for debugging when it's
destroyed by the GC. Since we can instantiate arbitrary `Post` objects, we can
get their contents printed out at will. We're very close now.

We can also create `Filter`s that act on the `Post`s. `Filter`s use PHP's
`preg_replace`. That's insecure, because you can use the `e` flag to *evaluate
arbitrary code* based on the replacement text generated from regex captures.
Argh.

At this point, it was around 2am, my hands felt like rubber, and my eyes felt
like mozzerella balls. So I just copied `posts/steve.txt`, and modified one of
the filters to dump the contents of the flag, and went to sleep in peace.

There are several lessons to be learned here, but the most important are:

1. Don't roll your own crypto.
2. If you do, don't use PHP.
3. If you do, read the docs.

### Block

Block uses a Substitution Permutation Network to encrypt the string---but it
does it twice. I pretty much brute-forced this one. But I did it tastefully, so
it merits a writeuplet.

We know that the message begins with `message:<space>`, and we know the first 9
bytes of the output. This lets us mount a known-plaintext attack. Here's how:
we encrypt the plaintext with *all* possible keys (there are
$2^{24}=16777216$ of them) and we *decrypt* the ciphertext with all possible
keys. Turns out that for the correct pair of keys, we'll get the exact same
result (the intermediate encryption). This is a 'meet-in-the-middle' attack
(not to be confused with 'man-in-the-middle' or 'Malcolm-in-the-Middle'), and
can be read about [on
Wikipedia](http://en.wikipedia.org/wiki/Meet-in-the-middle_attack). This is
good---now all we need to do is find the intersection of two massive lists.

Once I'd compiled these lists manually (it took over an hour), I realized that
I would be graduating high school by the time a naive Python intersection
search finished. Fortunately, Python's `set` type has ridiculously fast
member-checking, so it took all of 5 minutes to find the keypair, and I was
done.

---

That's all for now. I'll probably write a couple more, depending on the amount
of homework I need to make up this week&hellip;
