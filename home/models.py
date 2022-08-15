from django.db import models

from modelcluster.fields import ParentalKey

from wagtail.models import Page, Orderable
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, PageChooserPanel, InlinePanel
from wagtail.core.fields import RichTextField, StreamField
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.admin.edit_handlers import FieldPanel, StreamFieldPanel

from streams import blocks

class HomePageCarouselImages(Orderable):
    """Between 1 and 5 images for a HomePage carousel"""
    page = ParentalKey("home.HomePage", related_name="carousel_images")
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,      #No Cascading
        related_name="+"
    )

    panels = [
        ImageChooserPanel("carousel_image")
    ]


class HomePage(Page):
    """Home page model"""

    templates = "home/home_page.html"
    # Allow only one page
    max_count = 1

    banner_sitename = models.CharField(max_length=60, blank=False, null=True)
    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(blank=True, null=True)
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,      #No Cascading
        related_name="+"
    )
    banner_cta = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,      #No Cascading
        related_name="+"

    )

    content = StreamField(
        [
            ("cta", blocks.CTABlock()),
        ],
        null=True,
        blank=True
    )

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel("banner_sitename"),
            FieldPanel("banner_title"),
            FieldPanel("banner_subtitle"),
            ImageChooserPanel("banner_image"),
            PageChooserPanel("banner_cta"),
        ], heading="Banner Options"),
        MultiFieldPanel([
            InlinePanel("carousel_images", max_num=5, label="Image"),
        ], heading="Carousel Images"),
        StreamFieldPanel("content"),
        
    ]
    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


