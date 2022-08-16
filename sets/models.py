from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class SetsListingPage(Page):
    """List all the Sets"""

    template = "sets/sets_listing_page.html"

    def get_context(self, request, *args, **kwargs):
        context=super().get_context(request, *args, **kwargs)
        context["sets"]=SetsDetailPage.objects.live().public()
        return context

class SetsDetailPage(Page):
    """Brick Sets Detail Page"""

    template = "sets/sets_detail_page.html"

    set_id = models.CharField(max_length=10, blank=False, null=False, help_text="The Set or Box ID of the given set.")
    set_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text="The main image of this set i.e. the one you want displayed as Thumbnails, in searches etc."
    )
    set_pieces = models.IntegerField(blank=True, null=True, help_text="The piece count of this set.")

    content_panels = Page.content_panels + [
        FieldPanel("set_id"),
        FieldPanel("set_pieces"),
        ImageChooserPanel("set_image")
    ]