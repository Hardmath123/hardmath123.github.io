> I've been cleaning out my computer for the past few days, and late last night
> I came across this README. I have no memory of writing this, and to be honest
> I'm kind of frightened that it works (why are there regexes?).

### What is Inferno?

Inferno is a JavaScript library that provides [dynamic
scoping](http://c2.com/cgi/wiki?DynamicScoping) for JavaScript.

### Usage

First, install Inferno using our one-line cross-platform installer script,

``` eval("var $ = function(name) { var caller = arguments.callee.caller; while (caller !== null) { var names = caller.toString().replace(/\\/\\*.+\\*\\//g, ' ').replace(/\\/\\/.*\\n/g, ' ').match(/^function\\s+(?:\\w+\\s*)?\\((.*?)\\)/)[1].split(',').map(function(a) { return a.trim(); }); if (names.indexOf(name) !== -1) return caller.arguments[names.indexOf(name)]; caller = caller.arguments.callee.caller; } };")```.  

Then, use `$('name')` to dynamically search for a name.

### Example

Suppose you want to write a function that prints a story, but you want to be
able to specify where the output goes. It would be clumsy to thread an argument
through every subroutine, and for some reason people always get mad at you when
you use global variables. With Inferno, you can simply write a wrapper function
that binds the name `output` dynamically.

```javascript
function tell_beginning() {
    $('output').write("Once upon a time...");
}
function tell_ending() {
    $('output').write("...and they all lived happily ever after.");
}


function print_story(output) {
    tell_beginning();
}
if (typeof(window) !== 'undefined') {
    print_story(document);
} else {
    print_story(process.stdout);
}
```

By some miracle, Inferno works in both node and the browser.

### Bugs

- This not work on recursive functions, partly because browsers don't support
  traversing the stack, and partly because dynamically-scoped recursion makes
  everyone's head hurt.
- We are currently in denial about the existence of the `var` keyword, arrow
  functions, and pretty much anything that isn't bound via function arguments.
- Does not work in strict mode. This is actually a feature.
