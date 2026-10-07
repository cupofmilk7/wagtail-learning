from django.db import models
from wagtail.admin.panels import FieldPanel

from wagtail.models import Page


class HomePage(Page):

    #db
    subtitle = models.TextField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Подзаголовок'
    )

    #user input
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
    ]
