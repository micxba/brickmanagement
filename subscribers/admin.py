from wagtail.contrib.modeladmin.options import (
    ModelAdmin,
    modeladmin_register
)
from .models import Subscribers

class SubscriberAdmin(ModelAdmin):
    """Subscriber Administration"""

    model = Subscribers
    menu_label = "Subscribers"
    menu_icon = "placeholder"
    menu_order = 290
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("email_address", "full_name")
    search_fields = ("email_address", "full_name")

modeladmin_register(SubscriberAdmin)