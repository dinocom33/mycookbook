from django.core.exceptions import ValidationError


def recipe_title_validator(value):
    for char in value:
        if not char.isalpha() and char != '(' and char != ')':
            raise ValidationError('Title can contain letters, underscores and brackets only!')
