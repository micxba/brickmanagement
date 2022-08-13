""" Flexible Pages """
from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel

class FlexPage(Page):
    template = "flex/flex_page.html"

    # @todo add streamFields
    #content = StreamField()

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel("subtitle"),
    ]

    class Meta:
        verbose_name = "Flexible Page"
        verbose_name_plural = "Flexible Pages"
