I'm back.

The new Comfortably Numbered runs on a new state-of-the art blogging platform,
developed (of course) by yours truly: shock. Shock brings together a lot of
powerful technologies written by smarter people, and bundles them up into a
command line tool to publish posts.

Shock generates an RSS feed, a homepage, a 404 page, and content pages, all
built on templates and CSS that *you* write yourself. Then it lumps those in a
directory that you can serve on anything clever enough to serve static
filesystems: Dropbox, Google Drive, Github Pages, Amazon S3, even your home
computer.

Shock uses Mustache's non-logical templating system (non-logical, in this
context, is a compliment). It was built on a rather simple idea: **if you're
using a node-based command-line platform to create a blog, chances are you want
control over every single aspect of presentation**. In fact, I consider that
one of the primary symptoms of being a hacker.

Hackers want control over everything that they use. It's why we prefer
extensible text editors and browser add-ons, and why we spend hours tinkering
with spacing equations in TeX. It's also part of the reason I migrated away
from Google; App Engine is a very closed non-hacker-friendly environment. The
hacker-control symptoms are what guide us subconsciously in choosing and
designing software. We prefer open-source projects and scriptable systems
because they conform to the pattern of software that gives control to the user.

The opposite is true for most nonhacker packages. Word and PowerPoint are
'merciful god' software: they give you features (for example, those dreadful
PowerPoint animations) which you may or may not use, but they retain complete
control over what can be done. Compare that to a hacker-friendly document
generation technology like TeX or CSS. Similarly, nonhacker image editors or
other similar applications try to hide the filesystem from you. The most recent
project you were working on magically appears, along with a list of other
recent projects. This is unaccaptable to a hacker.

I feel the easiest way to convey this message is: "don't be afraid to expose
your software's guts". Often, the best software is the kind that gives you as
many handles and hooks as possible. Make your command-line tools UNIX filters
wherever possible: read from `stdin` and write to `stdout`. Use a universally
usable format like JSON for storing data. Most importantly, *never* explicitly
disallow a user from doing anything.

Preventing stupid things also prevents clever things.
