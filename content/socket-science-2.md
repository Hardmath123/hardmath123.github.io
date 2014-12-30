A quick recap: in [Part I](socket-science.html), we learned about how protocols
are really awesome, and how they stack onto each other to build abstractions.
We learned to use `netcat` to create TCP connections, and then played with HTTP
and HTTPS.

Let's write some protocol code (finished product available [on
Github](https://github.com/Hardmath123/jokebot)). We're going to use Python to
build a bot for [IRC](http://en.wikipedia.org/wiki/Internet_Relay_Chat), a
beautiful and
[historic](http://www.ibiblio.org/pub/academic/communications/logs/report-ussr-gorbatchev)
protocol for chatting over the Internet.

IRC bots are all over the place. Some do routine tasks like moderate channels.
Others let you play games like Mafia, or perhaps provide simple services like
spelling correction (or "make me a haiku"). Yet others simply keep logs of what
is said and then try to say relevant things at the right times. Perhaps the
most famous one is [Bucket](https://github.com/zigdon/xkcd-Bucket), who manages
`#xkcd`.

Our IRC bot is going to provide a utility which tells a joke when someone says
`!joke` in a particular channel.

---

The IRC protocol is specified in [this
document](https://tools.ietf.org/html/rfc2812) (that document updates [this
one](https://tools.ietf.org/html/rfc1459), as listed in the header)). That
document is called an RFC, or *Request For Comments*.

I think the RFC system is beautiful. RFCs are documents that standardize the
important messy details that hold the Internet together. They were 'invented'
by Stephen D. Crocker when he was [assigned the task to document
ideas](http://www.nytimes.com/2009/04/07/opinion/07crocker.html?_r=2&em&) in
the early days of the Internet. An RFC is supposed to be a memo; a technical
note or idea that is published for anyone to read, review, and (ha!) comment
on. Everyone [can write](http://www.rfc-editor.org/rfc/rfc4846.txt) an RFC.

This is how standards come about. Once I have published a sensible RFC that
standardizes some means of sharing files (for instance, the File Transfer
Protocol or FTP, which people still use from time to time
([RFC](http://tools.ietf.org/html/rfc114))), I can put it out there for smart
people all over the world to review. If it's *really* exciting, someone may
write an implementation. Future implementations would abide by the rules, and
so your FTP server and my FTP client would cooperate.

Notice how this is decentralized. It's not Google saying "Ok, folks, this is
how we're going to transfer files. Deal with it." RFCs specify the consensus of
many experts--when you see an RFC describing a protocol that has many
implementations, you know that many people agree that that's the best way of
doing things (and even if it isn't, it's a reasonable compromise).

Of course, if you have a completely different way of transferring files which
would use a brand new super-secure hyper-compressed protocol, you can write
your own RFC and implementations, and hope that it catches on.

There are a lot of RFCs around, some
[fascinating](http://www.livinginternet.com/i/ia_rfc_interesting.htm), some
[funny](http://www.livinginternet.com/i/ia_rfc_fun.htm). To us, however, they
are simply documentation for the protocol we will use to build our IRC bot.

But I digress.

---

The RFC isn't hard to read, but I'll just tell you the important parts here.
IRC works over the standard port `6667`, or port `6697` if it's secure
(SSL-wrapped).

Let's experiment on Freenode. I'm going to assume you have some idea of how IRC
works (that is, you know what I mean when I say "channel" and "nick"). You may
want to log into Freenode with another IRC client (an online one like KiwiIRC
would suffice), just to see stuff happen.

Now, start with `nc irc.freenode.net 6667`.

You might get some messages that look sort of like this:

    :wilhelm.freenode.net NOTICE * :*** Looking up your hostname...
    :wilhelm.freenode.net NOTICE * :*** Couldn't look up your hostname

That just means that Freenode's servers hoped you were logging in from an IP
address with a registered domain, so that it can display your username as
"user@hostname" in a `whois` query (and some other uses as well). But you're at
home, and your home's IP probably doesn't have a domain name pointing to it
(unless you're running a server at home!). So it just complains.

Anyway.

Type `NICK an-irc-explorer` and hit enter. Then type `USER an-irc-explorer * *
:Mr. IRC`. You should be greeted with a huge block of text that starts with
something like:

    :wilhelm.freenode.net 001 an-irc-explorer :Welcome to the freenode Internet Relay Chat Network an-irc-explorer
    :wilhelm.freenode.net 002 an-irc-explorer :Your host is wilhelm.freenode.net[37.48.83.75/6667], running version ircd-seven-1.1.3
    :wilhelm.freenode.net 003 an-irc-explorer :This server was created Sat Mar 8 2014 at 15:57:41 CET

Basically, it's telling you that you've successfully connected to the server,
and identified yourself with the nickname `an-irc-explorer`.

You can now converse with server by sending it more commands (type `HELP` to
list commands). Perhaps the most exciting one is `JOIN`: type `JOIN #bots` to
join Freenode's channel for bots.

Your normal IRC client should show that `an-irc-explorer` joined.

To say things, use `PRIVMSG #bots :Hello, world.` (The colon is a
separator character, not part of the actual text that will be displayed on a
client. Its purpose is to allow the last argument to contain spaces,
which--unsurprisingly--show up quite a lot in chat messages.)

If you say something from your client, you should get some scary text like this:

    :hardmath123!hardmath123@gateway/web/cgi-irc/kiwiirc.com/ PRIVMSG #bots :Hi

The first bit tells you who said something, and is of the form
`nickname!username@hostname` (remember the hostname lecture above?). `PRIVMSG`
means you're getting a message, `#bots` is the channel, and `Hi` is the
message.

Not too hard.

There's one last thing you need to know. IRC checks if you're there
periodically by sending out a `PING` message. All you need to do is send the
server `PONG` and it'll be happy. If you don't, the server assumes something
bad happened, and kills the connection based on a "Ping Timeout" (generally 120
seconds ish). It's the protocol version of "if I'm not back in an hour, call
the police."

And now you're ready for some code.

---

Fire up Python.

Python gives you sockets with the `socket` module, which corresponds rather
well with C's sockets.

```python
import socket
```

Let's create a socket and connect it to Freenode.

```python
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("irc.freenode.net", 6667))
```

The first line has two magic constants. `AF_INET` is best
[explained](http://beej.us/net2/html/syscalls.html) by Brian "Beej" Hall:

> In some documentation, you'll see mention of a mystical "PF_INET". This is a
> weird etherial beast that is rarely seen in nature, but I might as well
> clarify it a bit here. Once a long time ago, it was thought that maybe a
> address family (what the "AF" in "AF_INET" stands for) might support several
> protocols that were referenced by their protocol family (what the "PF" in
> "PF_INET" stands for).  That didn't happen. Oh well. So the correct thing to
> do is to use AF_INET in your struct sockaddr_in and PF_INET in your call to
> socket(). But practically speaking, you can use AF_INET everywhere. And,
> since that's what W. Richard Stevens does in his book, that's what I'll do
> here.

`SOCK_STREAM` means `TCP`. The alternative is `SOCK_DGRAM`, which means
`UDP`--User *Datagram* Protocol. There's also `SOCK_RAW`, which requires root
privileges and makes (you guessed it) a raw IP socket. We discussed these in
the previous installment.

The `connect` line, of course, connects to a remote socket somewhere in the
Freenode network. It's important to realize that that remote socket is the same
thing as the one you just created. The server/client-ness is an abstraction.
Your own socket has a host and port, too, which you can find with
`s.getsockname()`. You'll get something like `('192.168.0.4', 60694)`.

Getting data from a socket is kind of messy, because of how TCP works. You
don't really ever know if the server wants to send more data or not. So, UNIX
sockets work like this: you specify how many bytes you want to read, and the
process will be paused ("blocked") until the server sends you stuff (it could,
in theory, just sit there forever). When something is sent, at most that number
of bytes is given to you as a string.

In practice, this looks like:

```python
data = s.recv(1024)
```

to read at most 1024 bytes from the server.

There is a problem here. A chat client doesn't want to just freeze until a new
message is sent, it wants to do other things and occasionally carry out actions
if there's a new message.

The hard solution is to use Python threads. You have multiple bits of code
running around doing stuff at the same time, and you're very careful about the
socket's state. If you're not, you might end up reading and writing at the same
time and bad things will ensue.

That will end in a mess.

The easy solution is the `select` module. It's used as such:

```python
import select
readables, writables, exceptionals = select.select([s], [s], [s])
```

`select.select` will return three lists: a list of sockets that are readable,
a list of sockets that are writable, and a list of sockets that are in a bad
situation and erroring/broken/eating your laundry.

Now we can check:

```python
if len(readables) == 1:
    data = s.recv(1024) # won't block
```

Note that we still don't know *how much* data there is. In fact, we have no way
of knowing how much data there is, because the server may have sent another 20
bytes which TCP hasn't reassembled yet.

So, it's generally advisable for protocols to specify a maximum message length
and some signal that a message has been terminated. Section 2.3 of RFC 2812
very helpfully tells us how IRC handles this:

> IRC messages are always lines of characters terminated with a CR-LF (Carriage
> Return - Line Feed) pair, and these messages SHALL NOT exceed 512 characters
> in length, counting all characters including the trailing CR-LF. Thus, there
> are 510 characters maximum allowed for the command and its parameters.  There
> is no provision for continuation of message lines.

We can put that all together as follows:

```python
import select
import time
def read_loop(callback):
    data = ""
    CRLF = '\r\n'
    while True:
        time.sleep(1) # prevent CPU hogging :)
        readables, writables, exceptionals = select.select([s], [s], [s]) 
        if len(readables) == 1:
            data += s.recv(512);
            while CRLF in data:
                message = data[:data.index(CRLF)]
                data = data[data.index(CRLF)+2:]
                callback(message)
```

`callback` is called every time a complete message has been received. Also,
when it's being called, no other socket operations are happening (reads or
writes). As we discussed above, this is a major win.

Writing to the socket is much easier, it's literally `s.sendall('data')`.
(There's also `s.send('data')`, which isn't guaranteed to actually send all of
the data, but returns the number of bytes that actually made it (based on TCP
acknowledgements). `sendall` is an abstraction on top of this.)

Guess what? You know enough to write a bot now!

```python
import random
jokes = [
    # populate me with some good ones!
    # this might be the hardest part of writing the bot.
    "You kill vegetarian vampires with a steak to the heart.",
    "Is it solipsistic in here, or is it just me?",
    "What do you call two crows on a branch? Attempted murder."
]
s.sendall("NICK funnybot\r\n")
s.sendall("USER funnybot * * :hardmath123's bot\r\n")
connected = False
def got_message(message):
    global connected # yes, bad Python style. but it works to explain the concept, right?
    words = message.split(' ')
    if 'PING' in message:
        s.sendall('PONG\r\n') # it never hurts to do this :)
    if words[1] == '001' and not connected:
        # As per section 5.1 of the RFC, 001 is the numeric response for
        # a successful connection/welcome message.
        connected = True
        s.sendall("JOIN #bots\r\n")
    elif words[1] == 'PRIVMSG' and words[2] == '#bots' and '!joke' in words[3] and connected:
        # Someone probably said `!joke` in #bots.
        s.sendall("PRIVMSG #bots :" + random.choice(jokes) + "\r\n")
read_loop(got_message)
```

This is actually all you need. If you concatenate all the snippets in this blog
post, you will have a working bot. It's surprisingly terse (yay Python?).

We can actually make this secure with just two more lines of code. Remember how
I said SSL was 'wrapped' around a normal protocol?

```python
import ssl
secure_socket = ssl.wrap_socket(plain_old_socket)
```

`secure_socket` has all the methods of a normal socket, but the `ssl` module
handles the SSL negotiations and encryption behind the scenes. Abstraction at
its finest.

You can play around with [reading the
documentation](https://docs.python.org/2/library/ssl.html) and integrating this
into your bot (remember to use the new secure port, 6697).

If you end up deploying a bot, make sure you read the channel or server's bot
policy. For instance, Foonetic provides these instructions:

> Bot Policy: Well behaved bots are allowed. Annoying bots or bots which are
> insecure or poorly behaved are not allowed. Channel owners may have their own
> policy for public bots; it is advised you check with a channel operator
> before bringing a bot into a channel. Excessive bots from a single network
> address may exceed the session limit and/or be considered cloning. Please
> mark your bot with user mode +B and your nick in the "Real Name" field so
> that an oper can locate you if your bot malfunctions. Absolutely no "botnets"
> are allowed and any illegal activity will be reported to your ISP!

If you're lazy, you can get a slightly refined version of this code from [my
Github](https://github.com/Hardmath123/jokebot).

---

So. We learned about how RFCs work, and we read the RFC on IRC. Then we used
that knowledge to built an IRC bot on top of Python's low-level `socket`
library.

The techniques you learned in this blog posts are useful for all sorts of
things. For instance, SMTP is a simple email protocol (port 25), and it's an
easy way to send from a script (Python ships with `smtplib`, a module that
wraps around the protocol). Similarly, `telnet` is a very lightweight protocol
that adds some terminal-specific frills to netcat (screen size, raw mode, etc.)
Even bitcoin needs [documented
protocols](https://en.bitcoin.it/wiki/Protocol_specification) to work. It's
definitely worth learning how these things work.

Enjoy, and happy botwriting.
