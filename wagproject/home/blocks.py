from wagtail.blocks import StructBlock, CharBlock
from wagtail.images.blocks import ImageChooserBlock


class FigCaptionBlock(StructBlock):
    caption = CharBlock(
        label="Подпись"
    )

    figure = ImageChooserBlock(
        label="Изображение",
        help_text="Изображение для страницы"
    )

    class Meta:
        icon = 'image'
        template = 'blocks/fig_caption_block.html'
