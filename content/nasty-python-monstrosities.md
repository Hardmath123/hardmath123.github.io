**Scenario:** I've written a simple Python command-line tool. It consists of
more than one file, because separation of code is important. It only needs to
run on UNIX systems and shouldn't require sudo to install. How do I distribute
this code in a safe, user-friendly way? How do I teach my intro CS class how to
proudly share their creations with the world?

**Answer:** You don't.

Distributing Python code should be a solved problem. It's not. Or, rather, it's
a [standards problem](http://xkcd.com/927/). There are too many tools out
there, and there's no clear roadmap that explains which subset does what. I'm
talking about Pip, Virtualenv, PyPi, wheels, eggs, distutils, distribute,
setuptools, easy_install, and twine. Some of these have been incorporated into
others, and are therefore obsolete. Some of these are endorsed by a PEP.
(What's a PEP? Do I care?)

There is certainly not one obvious way to do it.  Even if you're Dutch.

Assuming you have picked out a subset of tools to use, though, there's no
guarantee that they will cooperate. A Pip flag, for instance, might work. It
might not work. It might do stuff that you didn't expect. It might create files
without telling you (correction: it'll be noted cryptically in the Pip log). It
might pass it on to `setup.py`, or it might not, or it might reject a valid
`setup.py` argument because it doesn't understand it, or it might pass it on to
Python erroneously.

My Pip log contains monstrosities such as:

(Enumeration of all the things here that make me cry is left as an exercise to
the reader.)

    Running command /usr/bin/python -c "import setuptools, tokenize;
    __file__='/path/to/setup.py'; exec(compile(getattr(tokenize, 'open',
    open)(__file__).read().replace('\r\n', '\n'), __file__, 'exec'))" develop
    --no-deps --user

In short, it might eat your laundry depending on local atmospheric conditions,
and then it'll flip a coin to decide whether or not to tell you.

---

Let's talk about publishing. PyPi is the "standard" repository. But it makes you
host your own tarballs, so essentially all it does is match package names to
URLs (all other information is duplicated in the tarball itself).

Uploading to PyPi happens *over an insecure connection*. [They recognize this
in the
docs](https://packaging.python.org/en/latest/distributing.html#upload-your-distributions),
and recommend installing a *separate* client that lets you publish over SSL.

They also keep telling users to use OpenID. The OpenID that [Google is
deprecating](https://developers.google.com/accounts/docs/OpenID#shutdown-timetable)
in a couple of months. Of course, [trying to log in with
Google](https://pypi.python.org/pypi?:action=login&provider=Google) throws an
internal server error.

Apparently, the whole system is so confusing that every time you upload, you
are encouraged to do a dry run on the test repository just to make sure you
understand it.

Now, my Python program was not a module, but a command-line tool. [The way you
specify a command-line
tool](http://blog.habnab.it/blog/2013/07/21/python-packages-and-you/) in Python
looks like this:
  
```python
# ...
entry_points={
    'console_scripts': ['name_to_link = packagename.submodule:function_name'],
},
# ...
```

Here's what setuptools does. It parses that monstrous string and extracts
information. It then creates a *new* Python script in a `$PATH`'d directory.
That script *imports* your script as a module, and then calls the function you
specify. It's anyone's guess whether important scriptey things such as
environment variables or command-line arguments are preserved.

This is all in complete ignorance of the whole `if __name__ == '__main__'`
infrastructure, for whatever reason. Of course, you can *also* make things
runnable with `python -m packagename.submodule` by including a `__main__` file.
Yum.

Even if it did the reasonable thing and symlinked your script directly, it
would actually *modify* your file. That's right. It [replaces shebang
lines](https://docs.python.org/2/distutils/setupscript.html#installing-scripts)
with the path to the currently-running Python interpreter. Because Explicit Is
Better Than Implicit (tm).

There is no reason to do this. UNIX provides a very helpful idiom: using
`#!/usr/bin/env python arguments...`. That'll search the $PATH for the
right interpreter and use it. No black magic needed, and you can provide flags
to the python interpreter if you so desire.

Only God---make that Guido---knows what'll happen if you're trying to install a
Python 3 script using a Python 2.7. Or want to distribute something runnable
with `ipython`.

---

By the way, if you think *installing* is bad: you would think uninstalling
should be a standardized, well-thought-out, documented process, right? You
wish. There setup.py-installed programs have no fixed uninstallation procedure.
If you Google around, you are led to [this highly-upvoted StackOverflow
answer](http://stackoverflow.com/a/1550235/3053429), which suggests using an
option that lists all generated files, and *piping the output* to `xargs rm
-rf`.

Let's hope they don't have a file with a space in it, or *bad* things are going
to happen. Keep in mind that Python is recommended for newbies, the kinds who
will gladly copy-and-paste shell commands from the Internet.

---

Here's the deal. Flat is *not* better than nested. Nested is better than flat.
There's a reason we use parsers to convert strings to abstract syntax trees.
There's a reason LISP is easier to write than x86 assembly. There's a reason
for the existence of the term "dependency tree". They are *literally* nested
structures. Importing from a sibling directory should not be the harrowing
experience it is in Python.

And that's why I love npm. Not because it's written in a beautiful language or
because it pretends to be easy-to-use, but because it's simple and elegant and
it doesn't do too much or too little. Modules are nested prettily in their
directories, and the *only* file npm touches is `package.json`.

Scripts are simply linked into npm's bin folder. Your "script" could be a Bash
program, for all it cares.

Installing is one command, uninstalling is one command, publishing is one
command, and everything is one tool operating on one repository.

npm is transparent. Python's plethora of packaging plakavacs are anything but.
