"""Streamfields live in here"""

from wagtail.core import blocks
from wagtail.images.blocks import ImageChooserBlock

class TitleAndTextBlock(blocks.StructBlock):
    """Title and text and nothing else"""

    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add additonal text")

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        lable = "Title & Text"

class CardBlock(blocks.StructBlock):
    """Cards with image and text and button(s)"""

    title = blocks.CharBlock(required=True, help_text="Add your title")
    
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, masx_lenght=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                ("button_page", blocks.PageChooserBlock(required=False)),
                ("button_url", blocks.URLBlock(required=False, help_text="If the button text above is selected, it will be used.")),
            ]
        )
    )

    class Meta:
        template = "streams/cards_block.html"
        icon = "placeholder"
        lable = "Cards"

class RichTextBlock(blocks.RichTextBlock):
    """Richtext with all the features"""

    class Meta:
        template = "streams/richtext_block.html"
        icon="doc-full"
        label = "Full Richtext"