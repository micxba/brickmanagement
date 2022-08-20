from django.db import models

from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel

class MinifigsListingPage(Page):
    """List all the Minifigs"""

    template = "minifigs/minifigs_listing_page.html"

    def get_context(self, request, *args, **kwargs):
        context=super().get_context(request, *args, **kwargs)
        context["minifigs"]=MinifigsDetailPage.objects.live().public()
        return context

class MinifigsDetailPage(Page):
    """Brick Minifigs Detail Page"""

    template = "minifigs/minifigs_detail_page.html"
    minifig_variant = models.CharField(max_length=30, blank=False, null=False, help_text="Variant e.g. \"Green Torso with blue buttons\"")
    minifig_id = models.CharField(max_length=10, blank=False, null=False, help_text="The Minifig ID.")
    minifig_image = models.ForeignKey(
        "wagtailimages.Image",
        blank=True,
        null=True,
        related_name="+",
        on_delete=models.SET_NULL,
        help_text="The main image of this MiniFig i.e. the one you want displayed as Thumbnails, in searches etc."
    )
    
    content_panels = Page.content_panels + [
        FieldPanel("minifig_variant"),
        FieldPanel("minifig_id"),
        ImageChooserPanel("minifig_image")
    ]
