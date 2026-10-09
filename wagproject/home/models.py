from django.db import models
from django.db.models import ForeignKey
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.images.blocks import ImageChooserBlock

from wagtail.models import Page


class HomePage(Page):

    #db
    subtitle = models.TextField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Подзаголовок'
    )
    rtf_body = RichTextField(
        null=True,
        blank=True,
    )
    bg_image = ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    #user input
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('rtf_body'),
        FieldPanel('bg_image'),
    ]
