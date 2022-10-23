from django.db import models

from modelcluster.fields import ParentalKey
from wagtail.models import Page, Orderable
from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel,MultiFieldPanel,InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel


class MinifigCarouselImages(Orderable):
    """Between 1 and 5 images for a HomePage carousel"""
    page = ParentalKey("minifigs.MinifigsDetailPage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )

    panels = [
        ImageChooserPanel("carousel_image")
    ]


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
    minifig_description = RichTextField(blank=True, null=True, help_text="Additional comments that may appear on the detail page.")
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
        FieldPanel("minifig_description"),
        FieldPanel("minifig_id"),
        ImageChooserPanel("minifig_image"),
        MultiFieldPanel([
            InlinePanel("carousel_images", max_num=5, label="Image"),
        ], heading="Additional Images"),
    
    ]
