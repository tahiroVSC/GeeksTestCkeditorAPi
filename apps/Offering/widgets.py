from django.forms.widgets import Select
from django.utils.html import format_html

class ImageSelectWidget(Select):
    def render_option(self, selected_choices, option_value, option_label):
        option_value = str(option_value)
        option_label = option_label or option_value
        selected_html = (
            format_html(' selected="selected"')
            if option_value in selected_choices
            else ''
        )
        image_path = f'/media/images_icon/{option_value}.jpg'  # Путь к вашему изображению
        image_preview = format_html('<img src="{}" style="max-height: 30px; max-width: 30px;" />', image_path)
        return format_html(
            '<option value="{}"{}>{}</option>',
            option_value,
            selected_html,
            f'{image_preview} {option_label}',  # Добавлен предварительный просмотр изображения
        )
