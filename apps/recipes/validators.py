from django.core.exceptions import ValidationError
import re


def recipe_title_validator(value):
    if not re.match(r"^[a-zA-Zа-яА-Я_() -]*$", value):
        raise ValidationError('Ensure title contains only letters(latin or cyrillic), '
                              'numbers, underscores, dashes and parentheses.')


def file_size_validator(image):
    filesize = image.file.size
    megabyte_limits = 5.0
    if filesize > megabyte_limits * 1024 * 1024:
        raise ValidationError(f'Max image size is {megabyte_limits}MB')
