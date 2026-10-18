from django.db import models
from django.db.models import ForeignKey, Model
from wagtail.admin.panels import FieldPanel
from wagtail.blocks import RichTextBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock

from wagtail.models import Page
from wagtail.snippets.models import register_snippet

from .blocks import FigCaptionBlock


class NewsPage(Page):
    # db
    body = StreamField(
        [
            ('rtfblock', RichTextBlock(
                features=['h1', 'bold', 'italic', 'link', 'ol', 'ul'],
                label="Текст"
            )),
            ('imgblock', ImageChooserBlock(
                label="Изображение",
                help_text="Изображение для страницы",
                template='blocks/imgblock.html',
            )),
            ('youtubeblock', EmbedBlock(label="Видео")),
            ('figcaptionblock', FigCaptionBlock(label="Изображение с подписью"))
        ],
        block_counts={
            'imgblock': {'max_num': 2},
        },
        blank=True,
    )

    # user input
    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]


class HomePage(Page):
    parent_page_types = []
    subpage_types = ['home.NewsPage', 'equipment.EquipmentIndexPage']

    max_count = 1

    # db
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

    body = StreamField(
        [
            ('rtfblock', RichTextBlock(
                features=['h1', 'bold', 'italic', 'link', 'ol', 'ul'],
                label="Текст"
            )),
            ('imgblock', ImageChooserBlock(
                label="Изображение",
                help_text="Изображение для страницы",
                template='blocks/imgblock.html',
            )),
            ('youtubeblock', EmbedBlock(label="Видео")),
            ('figcaptionblock', FigCaptionBlock(label="Изображение с подписью"))
        ],
        block_counts={
            'imgblock': {'max_num': 2},
        },
        blank=True,
    )

    # user input
    content_panels = Page.content_panels + [
        FieldPanel('subtitle'),
        FieldPanel('rtf_body'),
        FieldPanel('bg_image'),
        FieldPanel('body')
    ]


@register_snippet
class Footer(Model):
    # db
    bodytext = RichTextField(
        null=True,
        blank=True,
    )

    # user input
    panels = [
        FieldPanel('bodytext')
    ]

    def __str__(self):
        return "Footer"

    class Meta:
        verbose_name = "Футер"
        verbose_name_plural = "Футеры"