from django.db import models

class Subscribers(models.Model):
    """A subscriber Model for Blog etc."""

    email_address = models.CharField(blank=False, null=False, max_length=100, help_text="Email Address")
    full_name = models.CharField(max_length=100, blank=False, null=False, help_text="First and Last name")
    
    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Subscribers"
        verbose_name_plural = "Subscribers"
    
