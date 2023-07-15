from django.core.exceptions import ValidationError


def contact_names_validator(value):
    if len(value) < 3 and value != '':
        raise ValidationError('First or last name must be at least 3 characters long.')

    if value != '':
        for char in value:
            if not char.isalpha():
                raise ValidationError('First or last name can only contain letters.')

    if not value[0].isupper():
        raise ValidationError('First or last name must start with a capital letter.')
