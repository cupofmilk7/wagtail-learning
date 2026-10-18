from django.db import models
from wagtail.models import Page, Orderable
from modelcluster.fields import ParentalKey
from wagtail.fields import RichTextField
from wagtail.admin.panels import MultiFieldPanel, FieldPanel, InlinePanel


class EquipmentOperator(Orderable):
    """Оператор оборудования."""

    name = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField()

    equipment = ParentalKey(
        'equipment.EquipmentPage',
        on_delete=models.CASCADE,
        related_name='operators'
    )


class EquipmentPage(Page):
    """Старница с информацией о единице оборудования."""

    description = RichTextField(
        blank=True,
        null=True,
        features=['h1', 'h2', 'h3', 'h4', 'h5', 'h6',
                  'hr', 'bold', 'italic', 'ol', 'ul', 'link'],
    )

    content_panels = Page.content_panels + [
        FieldPanel('description'),
        MultiFieldPanel([
            InlinePanel('operators', label="Оператор"),
        ], heading="Операторы"),
    ]

    subpage_types = []
    parent_page_types = ['equipment.EquipmentIndexPage']

    class Meta:
        verbose_name = "Оборудование"
        verbose_name_plural = "Оборудование"


class EquipmentIndexPage(Page):
    """Страница для выведения списка оборудования."""

    max_count = 1

    subpage_types = ['equipment.EquipmentPage']
    parent_page_types = ['home.HomePage']
