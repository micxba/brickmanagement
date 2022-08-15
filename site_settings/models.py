from atexit import register
from django.db import models

from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.images.edit_handlers import ImageChooserPanel

@register_setting
class GlobalSiteSettings(BaseSetting):
    """Global Settings for this site used all over"""

    websitename = models.CharField(max_length=30,blank=False, null=True, help_text="The Website name (Title)")
    site_subtitle = models.CharField(max_length=60,blank=True, null=True, help_text="A subtitle or Slogan you would like to appear under the sitename in some cases")
    site_banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,      #No Cascading
        related_name="+"
    )

    panels = [
        MultiFieldPanel([
            FieldPanel("websitename"),
            FieldPanel("site_subtitle"),
            ImageChooserPanel("site_banner_image")
        ],"GLobal Site Settings")
    ]

@register_setting
class SocialMediaSettings(BaseSetting):
    """Social Media Settings for Site"""
    
    facebook = models.URLField(blank=True, null=True, help_text="Facebook URL")
    twitter = models.URLField(blank=True, null=True, help_text="Twitter URL")
    youtube = models.URLField(blank=True, null=True, help_text="YouTube Channel URL")
    instagram = models.URLField(blank=True, null=True, help_text="Instagram Profile URL")
    github = models.URLField(blank=True, null=True, help_text="GitHub URL")

    panels = [
        MultiFieldPanel([
            FieldPanel("facebook"),
            FieldPanel("twitter"),
            FieldPanel("youtube"),
            FieldPanel("instagram"),
            FieldPanel("github"),
        ], heading="Social Media Settings")
    ]
