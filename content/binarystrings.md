One of the things I had to do for PicoCTF was learn how to wrangle binary
strings in various languages. The idea is that you think of a string as an
array of numbers instead of an array of characters. It's only coincidental that
some of those numbers have alternate representations, such as "A". The
alphabet-number correspondence is an established table. Look up
[ASCII](http://wikipedia.org/wiki/ASCII).

Each number is a byte (aka an `unsigned char`), so it ranges from 0 to 255.
This means it's convenient to express them in hex notation--each number is two
hex digits, so `0xff` is 256.

Using this, we can turn strings into hex sequences (by doubling the number of
printed characters), and then turn the hex sequence into a decimal number. This
is great for crypto, because many algorithms (including RSA) can encrypt a
single number.

We can also use [base64](http://en.wikipedia.org/wiki/Base64) scheme to turn
binary strings into printable strings. It uses case-sensitive alphabet (52),
numbers (10), `+`, and `/` (2) as the 64 symbols. Each set of three bytes is
represented by four base64 symbols. Note that this means we need to pad the
string if it isn't a multiple of 3 bytes. The padding is indicated with `=` or
`==` at the end of the encoded message.

This post summarizes some really useful functions for working with binary
strings.

### Python

You can use hexadecimal literals in Python strings with a `\x` escape code:

```python
s = '\x63\x6f\x77'
```

To get this representation of a string that's already in memory, use `repr`. It
will turn unprintable characters into their escape codes (though it will prefer
abbreviations like `\n` over hex if possible).

You can use `ord` to turn a character into a number, so `ord('x') == 120` (in
decimal! It's equal to `0x78`). The opposite function is `chr`, which turns a
number into a character, so `chr(120) == 'x'`. Python allows hex literals, so
you can also directly say `chr(0x78) == 'x'`.

To convert a number to a hex string, use the (guesses, anyone?) `hex` function.
To go the other way, use `int(hex_number, 16)`:

```python
hex(3735928559) == '0xdeadbeef'
int('deadbeef', 16) == 3735928559
```

To convert a string to or from hex, use `str.encode` and `str.decode`:

```python
>>> 'cow'.encode('hex')
'636f77'
>>> '636f77'.decode('hex')
'cow'
```

The pattern `hex(number).decode('hex')` is quite common (for example, in RSA
problems). Keep in mind that you need to strip the leading `0x` and possibly a
trailing `L` from the output of `hex`, and also make sure to pad with a leading
`0` if there are an odd number of characters.

Finally, Python handles base64 with the `base64` module, but you can also just
use `str.encode('base64')` and `str.decode('base64')`. Keep in mind that it
tacks on trailing `\n`s. I don't know why.


### JavaScript

JavaScript is pretty similar. It supports `\x12` notation, and `0x123` hex
literals. The equivalent of `ord` and `chr` are `"a".charCodeAt(0)` and
`String.fromCharCode(12)`, respectively.

You can convert a hex string to decimal with `parseInt(hex_string, 16)`, and go
the other way with `a_number.toString(16)`:

```javascript
parseInt("deadbeef", 16) == 3735928559
3735928559.toString(16) == 'deadbeef'
```

Note the lack of `0x`.

Unfortunately, there isn't a built-in string to hex string encoding or decoding
built into JavaScript, but it isn't too hard to do on your own with some clever
Regexes. The tricky part is knowing when to pad.

Browser JS has `atob` and `btoa` for base64 conversions (read them as
"ascii-to-binary" and "binary-to-ascii"). You can install both of those as
Node modules from npm: `npm install atob btoa`.

### Bash

For the sake of completeness, I wanted to mention how to use Bash to input
binary strings to programs. Use the `-e` flag to parse hex-escaping in string
literals, and `-n` to suppress the trailing `\n` (both of these are useful to
feed a binary a malformed string):

```bash
$ echo "abc\x78"
abc\x78
$ echo -e "abc\x78"
abcx
$ echo -ne "abc\x78"
abcx$ # the newline was suppressed so the prompt ran over
```

Alternatively, `printf` does pretty much the same thing as `echo -ne`.

Sometimes you want to be able to write more data after that, but the binary is
using `read()`. In those cases, it's helpful to use `sleep` to fool `read` into
thinking you finished typing:

```bash
{ printf "bad_input_1\x00 mwahaha";
                     #  the zero char signals end-of-string
                     #  in C, which can be used to wreak all
                     #  sorts of havoc. :)
    sleep 0.1;
    printf "bad_input_2";
    sleep 0.1;
    cat -; # arbitrary input once we have shell or something
} | something
```

Or, if you're intrepid, you can use Python's `subprocess` or Node's
`child_process` to pipe input to the binary manually.

UNIX comes with the `base64` command to encode the standard input. You can use
`base64 -D` to decode.

### Parting tips

Use `hex` when your binary string is a giant number, and use `base64` when
you're simply turning a binary string into a printable one.

Use `wc -c` to get the character count of a binary file.

Use `strings` to extract printable strings from a binary file, though ideally
[not on trusted files](https://sourceware.org/bugzilla/show_bug.cgi?id=17512).

Finally, use `od` or `xxd` to pretty-print binary strings along with their hex
and plaintext representations.
