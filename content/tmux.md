[tmux](http://tmux.sourceforge.net) is a *terminal multiplexor*, which is
nerdspeak for a program that runs multiple processes simultaneously within a
single parent process. This lets you have, for example, a text editor and a
test server running in the same physical terminal window. Instead of opening
multiple `ssh` connections to your server, `tmux` allows you to maintain a
single connection and divide your screen up virtually into multiple panes.

Another nice thing about `tmux` is that the virtual panes are independent of
the processes running, so you can "detach" a process and leave it running in
the background without any terminal displaying the output. In face, a detached
`tmux` session lives on even if you disconnect the `ssh` session. When you log
back on, you can reattach to that process again.

Anyway, let's get started. You make a tmux session by typing `tmux` in bash.

Your screen should get a pretty green ribbon under it, saying `0:bash`. This
means you're currently in window 0, running `bash`. You can do normal bashey
things here (`ls`, `vim`, `irssi`, whatever): `tmux` simply feeds your user
input along to the bash process.

Well, almost. `tmux` listens in and intercepts any input that begins with a
special keypress, `^B`. You type this with the control character and 'B' the
way you would type `^C` to kill a bash process. We call `^B` the "prefix".

Let's detach from `tmux`! For the dramatic effect, feel free to leave some
process running--perhaps a Python session or even your IRC client. Type `^B D`
(that is, the prefix followed by the `D` character).

You should be back to the old bash. But the process you started is still
running in the background: just not getting any input from you (or showing you
any output). To reconnect to it, type `tmux attach` and you should get your
process again. The easiest way to kill a session is to simply exit all the
processes in it; if only `bash` is running, then type `exit`.

You can use and manipulate multiple different named sessions, by specifying
different command line arguments to `tmux`, such as `tmux new -s
name_of_new_session` to make a new session, `tmux attach -t name` to attach to
a named session, and `tmux kill-session -t name` to kill a session. `tmux ls`
lists sessions.

But the more interesting stuff is multiplexing. Open up a session and type `^B
%`. Your pane should split into two columns. You now essentially have two
virtual terminals. Use `^B arrow-keys` to switch between panes. To close a pane
you exit the process that was running in that pane (`exit` in bash).

You can use `^B "` to split the other way (horizontally, so the new pane is
below the old one). And there are a bunch of commands to resize and swap panes.

Instead of saying them all over again, I'm going to point you to [this
gist](https://gist.github.com/MohamedAlaa/2961058), which has all the
information you need.

In general, I use `tmux` as a way to keep my session as I left it when I logout
(for example, this post was written across a couple of days, but I didn't close
vim at all). Also, it's an easy way to leave a server or a bot running
perpetually.

Enjoy tmuxing!
