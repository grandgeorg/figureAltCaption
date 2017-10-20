"""
Generates a Caption for Figures for each Image
which stands alone in a paragraph,
similar to pandoc#s handling of images/figures

--------------------------------------------

Licensed under the GPL 2 (see LICENSE.md)

Copyright 2015 - Jan Dittrich by
building upon the markdown-figures Plugin by
Copyright 2013 - [Helder Correia](http://heldercorreia.com) (GPL2)
Bugfix and improvements by Viktor Grandgeorg
Copyright 2017 - [Viktor Grandgeorg](http://grandgeorg.com) (GPL2)

--------------------------------------------

Examples:
    Some paragraph body text

    !![this is the caption](http://lorempixel.com/400/200/)

    Next paragraph starts here

would generate a figure like this:

    <figure>
        <img src="http://lorempixel.com/400/200/">
        <figcaption>this is the caption</figcaption>
    </figure>
"""


from __future__ import unicode_literals
from markdown import Extension
from markdown.inlinepatterns import IMAGE_LINK_RE, IMAGE_REFERENCE_RE, NOBRACKET, BRK
from markdown.blockprocessors import BlockProcessor
from markdown.util import etree
# re Support for Regular Expressions
import re

# for tests only:
# import pprint

import logging
logger = logging.getLogger('MARKDOWN')

FIGURES = [
    u'^\s*\!' + IMAGE_LINK_RE + u'\s*$',
    u'^\s*\!' + IMAGE_REFERENCE_RE + u'\s*$'
]


# This is the core part of the extension
class FigureCaptionProcessor(BlockProcessor):
    FIGURES_RE = re.compile('|'.join(f for f in FIGURES))
    COUNTER = 0

    def test(self, parent, block):
        isImage = bool(self.FIGURES_RE.search(block))
        isOnlyOneLine = (len(block.splitlines()) == 1)
        isInFigure = (parent.tag == 'figure')
        if (isImage and isOnlyOneLine and not isInFigure):
            return True
        else:
            return False

    def run(self, parent, blocks):
        self.COUNTER += 1
        raw_block = blocks.pop(0)
        # Let's get rid of the first exclamation mark
        clean_rb = raw_block[1:]
        # pprint.pprint(clean_rb)
        captionText = self.FIGURES_RE.search(raw_block).group(1)
        # If captionText is empty it's a reference
        # and we have to search in that regex:
        if not captionText:
            captionText = re.search(IMAGE_REFERENCE_RE, clean_rb).group(1)
            # pprint.pprint(captionText)

        # create figure
        figure = etree.SubElement(parent, 'figure', {'id' : 'figure-' + str(self.COUNTER) })

        # render image in figure
        figure.text = clean_rb

        # create caption
        figcaptionElem = etree.SubElement(figure, 'figcaption')
        # Commant by Jan Dittrich:
        # no clue why the text itself turns out as html again and not raw.
        # Anyhow, it suits me, the blockparsers annoyingly wrapped everything
        # into <p>.
        figcaptionElem.text = captionText


class FigureCaptionExtension(Extension):
    def extendMarkdown(self, md, md_globals):
        """ Add an instance of FigcaptionProcessor to BlockParser. """
        md.parser.blockprocessors.add('figureAltcaption',
                                      FigureCaptionProcessor(md.parser),
                                      '<ulist')


def makeExtension(configs={}):
    return FigureCaptionExtension(configs=configs)
