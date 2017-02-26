# figureAltCaption

Generates a figurecaption each Image which stands alone in a paragraph,
similar to [pandoc’s handling of images/figures](http://pandoc.org/README.html#extension-implicit_figures)

## Installation

```
pip install git+git://github.com/grandgeorg/figureAltCaption.git
```

### Usage in markdown source:

    Some paragraph body text

    !![This is the caption](http://lorempixel.com/400/200/)

    Next paragraph starts here

will generate:

    <p>Some paragraph body text</p>

    <figure>
        <img alt="This is the caption" src="http://lorempixel.com/400/200/">
        <figcaption>This is the caption</figcaption>
    </figure>

    <p>Next paragraph starts here</p>

You can also use reference-style:

    Some paragraph body text

    !![This is the caption][g1]

    Next paragraph starts here

    [g1]: img/img.png "This is the title text"

will generate:

    <p>Some paragraph body text</p>

    <figure>
        <img alt="This is the caption" src="img/image.png"
            title="This is the title text">
        <figcaption>This is the caption</figcaption>
    </figure>

    <p>Next paragraph starts here</p>

## Usage width mkDocs
Just call the extension in your mkdocs.yml:
```
markdown_extensions:
  - figureAltCaption
```

## Improvements

Improvements over original from https://github.com/jdittrich/figureAltCaption:

-   Reference-style now works.
-   **Changed markdown trigger syntax.**

    If you want to have `figure` with `figcaption`, you now have to call it via:
    ```
    !![This is the caption](someimageurl.png)
    ```
    while the default image syntax from markdown will not generate figure and caption:
    ```
    ![This is the caption](someimageurl.png)
    ```
    This way one can decide to use this extension on a per image base.

---

Licensed under the GPL 2 (see LICENSE.md)

Copyright 2015 - Jan Dittrich by
building upon the [markdown-figures](https://github.com/helderco/markdown-figures) Plugin by
Copyright 2013 - [Helder Correia](http://heldercorreia.com) (GPL2)
Bugfix and improvements by Viktor Grandgeorg
Copyright 2017 - [Viktor Grandgeorg](http://grandgeorg.com) (GPL2)

---