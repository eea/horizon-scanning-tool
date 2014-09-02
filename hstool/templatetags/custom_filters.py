from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='label')
def render_label(field):
    return mark_safe(
        field.label_tag() + (
            '<span class="required_field">*</span>' if field.field.required
            else ''
        )
    )