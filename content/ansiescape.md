Have you ever wondered how to print color to terminals? Or why on some CLI
interfaces, the arrow keys print out mysterious sequences like `^[[A`? Or why
sometimes the keyboard shortcut control-C becomes `^C`? Well, the answers to
these are all  based on ANSI escape codes.

In UNIX programs, there's the concept of 'raw' and 'canonical' mode for input.
'Raw' mode takes input character-by-character, while 'canonical' mode lets the
user write a line and hit enter to send the program the written line. Canonical
mode is generally more useful: it lets you go back and delete something if you
make a mistake. But applications that work on a per-keypress basis need to
bypass this. In node, you can enter raw mode with
`process.stdin.setRawMode(true);`.

CLI interactions also need the concept of control characters. When you type
control-C, you're sending the program the byte `0x3`, which is… 3. But that's
the ASCII **control character** which means 'end of text'. The program takes
this, by convention, as a signal to stop executing (`KeyboardInterrupt` in
Python, for example). We print control characters with a caret (`^`), followed
by the letter we type on the keyboard. There are 32 of them, which [Wikipedia
lists](http://en.wikipedia.org/wiki/ASCII#ASCII_control_code_chart). You might
be familiar with using `^D` ('end of transmission') to quickly exit Python or
nodejs.

ANSI escape codes are a way to output to a terminal with more capability than
just raw text (there *was*, for comparison, a time when computer output was
printed, physically on paper, line by line). You can move the cursor back and
overwrite or clear text. You can also color text or make it blink obnoxiously.

ANSI escape codes start with the CSI: the **Control Sequence Introducer**. The
most common one is `\e[`. `\e` is the ASCII escape character `0x1b`. You can
type it with the control character `^[` (that is, `control-[`).

Next, they have a sequence of numerical arguments, separated by semicolons, and
finally, they have a letter which indicates the command. Once more, [Wikipedia
lists](http://en.wikipedia.org/wiki/ANSI_escape_code#CSI_codes) these. As an
example, we can move the cursor to the top-left corner with `\e[1;1H` (H is the
command to move, and the arguments are 1 and 1).

Colors are just as easy. We use the `m` command, with an SGR ('Set Graphics
Rendition') parameter. 35 is the SGR parameter to set the text color to
magenta, while 42 makes the background green. So `\e[35;42m` would give us a
horrible magenta-on-green color scheme. (`\e[m` (no arguments) restores
everything).

This, by the way, explains the `^[[A` curiosity. When you press up-arrow, the
terminal sends the application the ANSI escape code to move the cursor up—the
command for this is `A`. So we get `\e[A`, and `\e` gets rendered as its
control code equivalent of `^[`. (You can, in fact, manually enter
control+[-[-A in Bash, and get the standard up-arrow behavior of pulling up the
last entered command.)

Some nodejs code to get you started—it's a utility to interactively display the
bytes sent from a terminal when you press a key(combination).

```javascript
process.stdin.resume();
process.stdin.setRawMode(true);

process.stdin.on("data", function(buffer) {
    if (buffer.length === 1 && buffer[0] === 3) {// detect ^C
        process.stdout.write("\n"); // A trailing \n prevents
                                         // the shell prompt from
                                         // messing up.

        process.exit(0);                 // die
    } else {
        process.stdout.write("\x1b[1J\x1b[1;1H");
                            // clear line and go to top
        process.stdout.write(
            require('util').inspect(buffer)
            // Nice output format
        );
    }
});
```

This should give you the tools to write shinier, interactive utilities. But keep in mind the UNIX philosophy—keep them simple, and make sure they cooperate as filters (you should be able to pipe stuff in and out of your utility).

P.S. I wrote this post—including the code sample—in vim running in tmux. Please pardon typos.
