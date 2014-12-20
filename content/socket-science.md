I like protocols. The Internet is like being in a party, and trying to have a
conversation with the person across the room by passing post-it notes. Except
you can only fit a couple of words onto a post-it note (of which you have, of
course, a limited supply). And people take as long as they want to pass along
the note. Or they could just forget about it. Some of them might read the
notes, others may replace your notes with their own. And the person across the
room only speaks Finnish.

Despite these hostile conditions, the Internet works. It works because we have
protocols--rules that computers in a network obey so that they can all get
along.

And you can understand these protocols. It's not rocket science: it's socket
science! (I promise that was the only pun in this post.)

Protocols fit onto other protocols. The lowest-level protocol you should really
care about is TCP: the Transmission Control Protocol. TCP handles taking a
large message, dividing it among many post-it notes, and then reassembling the
message at the other end. If some notes get lost along the way, TCP sends
replacements. Each post-it is called a "packet".

Of course, TCP fits on top of another protocol, the Internet Protocol (IP, as
in IP Address), which handles even messier things like ensuring a packet gets
passed on from its source to its destination. There are other protocols that
live on IP: UDP is like TCP, except it doesn't care whether packets get there.
If you're writing a video conferencing service, you don't need to ensure that
each packet makes it, because they'll be out of date. So you use UDP.

TCP is handled at the kernel level, so when you send out a message, it's
wrapped in TCP automatically. In fact, you need administrator privileges on
UNIX to send out "raw" packets (there are occasionally reasons to do this).

To create a TCP connection, we use *sockets*. Most languages provide socket
bindings: I'll use Python's API (which is very similar to C's), but Node.js's
`net` module does the same thing.

A quick way to get a socket working is to use `netcat` (it's called `nc` on
most UNIX shells). There's also `telnet`, but telnet listens for its own
protocol (for instance, if your connection sends a specific string, `telnet`
will automatically send back your screen width).

Alternatively, you can use `ncat`, which comes bundled with `nmap`. I prefer
`ncat`; I'll explain why in a little bit. This command-line utility is pretty
much a UNIX stream that sends out stdin by TCP, and writes incoming messages to
stdout.

Once you have TCP working, you can do all sorts of stuff, because now message
length and integrity has been abstracted away. For example, you explore the web
by abiding by the HyperText Transfer Protocol (HTTP, as in http://something).

In fact, it's worth trying right now. HTTP has the concept of a "request" and a
"response". HTTP requests look sort of like `GET /index.html HTTP/1.1`. GET is
the "method", you can also POST, PUT, or DELETE (or even
[BREW](http://en.wikipedia.org/wiki/Hyper_Text_Coffee_Pot_Control_Protocol)).

`/index.html` is the path (the stuff you would type after `www.google.com` in
the address bar), and `HTTP/1.1` is the protocol (you could, in theory, have
another protocol running--HTTP 2.0 is being drafted as I write this).

Let's do it. Open up a shell and try `nc google.com 80`. You're now connected
to Google. Try sending it `GET /index.html HTTP/1.1`. You'll need to hit
"enter" *twice* (it's part of the protocol!).

You'll be greeted by a huge mess of symbols, which is the HTML code that makes
up the Google homepage. Note that the connection doesn't close, so you can send
another request if you want. In fact, let's do that: if you only want to check
out the protocol, you can send a `HEAD` request, which is identical to `GET`
except it doesn't send back an actual message. In the real world, `HEAD` is
useful to efficiently check if a file exists on a server. If you try `HEAD
/index.html HTTP/1.1`, you get:

```
HTTP/1.1 200 OK
Date: Sat, 29 Nov 2014 19:40:02 GMT
Expires: -1
Cache-Control: private, max-age=0
Content-Type: text/html; charset=ISO-8859-1
Set-Cookie: PREF=ID=67a496862b9f3c29:FF=0:TM=1417290002:LM=1417290002:S=8UjQDBRWYSa1y9tA; expires=Mon, 28-Nov-2016 19:40:02 GMT; path=/; domain=.google.com
Set-Cookie: NID=67=NnwRLRx4JVz-x3lWFTSxzV_ZxLi_TLVmbw8oDifyhzT2iuWwQ0mVveS15bE8jI28kI-p8cMIEXmmwDmwlxojTY07azz6XzcmeRD7mHerDLuVjPwjV180AxNqWBHqJrfp; expires=Sun, 31-May-2015 19:40:02 GMT; path=/; domain=.google.com; HttpOnly
P3P: CP="This is not a P3P policy! See http://www.google.com/support/accounts/bin/answer.py?hl=en&answer=151657 for more info."
Server: gws
X-XSS-Protection: 1; mode=block
X-Frame-Options: SAMEORIGIN
Alternate-Protocol: 80:quic,p=0.02
Transfer-Encoding: chunked
```

This looks messy, but it really isn't. You can see how the protocol works: you
start with the protocol name and `200 OK`, which is the *response code*. You
are probably familiar with another response code, `404 NOT FOUND`.

Then each line begins with some header, a colon, and then information. For
instance, you get the date, you get the content type (`text/html`), etc.

The Cookie headers instruct the browser to save those values in a local file.
When the web browser sends further requests, the protocol instructs it to send
the saved cookies as a part of the request. This lets websites track you--and
is the reason Gmail keeps you logged in even when you close the window.

So far, so good. One thing that may have bothered you was the `80` you typed
as an argument for `nc`. That's the *port number*. The idea is that a computer
can serve multiple websites by having multiple active sockets. To allow this,
TCP has a port argument: your computer has 65,536 ports and it delivers packets
to the right one.

As I said, `ncat` comes bundled with `nmap`. `nmap` is a *port scanner*, a
script that checks every port of a computer to see if anything is listening
(this is one of those places where raw sockets make things much more
efficient). Running port scans lets an attacker find vulnerable programs
running, and then exploit them (for instance, test servers or outdated services
that have known security issues are easy targets).

Don't run port scans on computers you don't own. `nmap` is designed to be used
by professional network security people, who keep huge sites like Google up and
running safely.

`80` is the conventional port for HTTP, but you can serve a website on any
port. To access it from a web browser, you append the port after the domain
name, like `http://example.com:81/index.html`.

The other thing that may have bothered you was how the computer know who
`google.com` was. The answer to that is another protocol: the DNS protocol,
which is used to ask a DNS server to resolve a domain name (like Google.com)
into an IP address. You can try this with the `host` command:

```
$ host google.com
google.com has address 74.125.239.135
google.com has address 74.125.239.129
google.com has address 74.125.239.134
google.com has address 74.125.239.131
google.com has address 74.125.239.133
google.com has address 74.125.239.142
google.com has address 74.125.239.128
google.com has address 74.125.239.137
google.com has address 74.125.239.136
google.com has address 74.125.239.130
google.com has address 74.125.239.132
google.com has IPv6 address 2607:f8b0:4005:800::1009
google.com mail is handled by 30 alt2.aspmx.l.google.com.
google.com mail is handled by 40 alt3.aspmx.l.google.com.
google.com mail is handled by 10 aspmx.l.google.com.
google.com mail is handled by 20 alt1.aspmx.l.google.com.
google.com mail is handled by 50 alt4.aspmx.l.google.com.
```

Once you choose an IP address, the protocol lets you track down that computer
and establish a connection.

Now, you're often told to always use HTTPS, because it's secure. You can
probably already tell how insecure HTTP is: any guest at the party can read
your post-it packets and know everything.

A fun thing to try is to run `tcpdump`: it'll dump packets from your computer
as they're sent out or received (you may like the `-X` option). Mess around
with the options a bit, and you can read the raw contents of HTTP packets as
you surf the web. You'll need to be an administrator to run it, but if you
think about it, that's probably a good thing.

Anyhow, back to HTTPS: it's just HTTP, except sitting on top of another
protocol called SSL (or TLS--it's sort of complicated). SSL handles finding an
encryption that both you and your connection agree is secure, negotiating a
shared secret key, and then sending encrypted messages. It also lets you
authenticate people by passing around certificates that are cryptographically
signed by authorities.

HTTPS runs on port 443, which is the other default port that your browser
doesn't need to be told. You can try the above HTTP fun on port 443: most
websites will get mad at you and kill the connection.

This is the reason I like `ncat`: the `--ssl` option wraps your connection in
the SSL negotiations and encrypts what you send (you can't viably do this
manually). Try `ncat --ssl google.com 443`: things should work as normal now,
but `tcpdump` will show you gibberish.

At this point we've foiled almost all the hurdles in our initial party analogy,
so I'm going to take a break.

In [Part II](socket-science-2.html) of this series, we'll explore some more
protocols and write clients using Python. We'll talk about how protocols are
established, and why it's important that it works the way it does right now.

In Part III (yet-to-be-written), we'll explore four recent showstopper
exploits, all of which make plenty of sense once you understand protocols: Goto
Fail, Heartbleed, Shellshock, and POODLE.
