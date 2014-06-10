Whoa, it's been a really long time! If you've been following along, you may have noticed that this blog now lives on Github pages. Which means it must be static. That's cool.

In fact, I built the (static) Shock package, which compiles a set of templates and actual content into a nice little webpage you can host on anything smart enough to serve up static pages. That includes Github Pages, Dropbox, Google Drive, Amazon S3, etc. Shock lets you store posts as HTML or Markdown, and inserts them verbatim into templates of your choice---it doesn't try to control any of your web design.

Once you have a blog set up, the Shock workflow is as simple as:

    touch content/newpost.html
    $EDITOR newpost.html
    shock newpost
    shock compile
    git add .
    git commit
    git push
