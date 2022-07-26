"""The template method use case example"""

from text_document import TextDocument
from html_document import HTMLDocument

TEXT_DOCUMENT = TextDocument
TEXT_DOCUMENT.create_document("Some Text")

HTML_DOCUMENT = HTMLDocument
HTML_DOCUMENT.create_document("Line 1\n Line 2")

