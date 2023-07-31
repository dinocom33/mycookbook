from django.core.exceptions import ValidationError
from django.test import TestCase
from django.utils import timezone

from apps.common.models import Contact


class ContactModelTest(TestCase):
    def test_contact_model_creation_with_required_fields(self):

        contact = Contact.objects.create(
            email='test@example.com',
            subject='Test Subject',
            message='This is a test message.',
        )

        self.assertEqual(contact.email, 'test@example.com')
        self.assertEqual(contact.subject, 'Test Subject')
        self.assertEqual(contact.message, 'This is a test message.')
        self.assertIsInstance(contact.date_sent, timezone.datetime)

    def test_contact_model_creation_with_optional_fields(self):

        contact = Contact.objects.create(
            first_name='John',
            last_name='Doe',
            email='test@example.com',
            subject='Test Subject',
            message='This is a test message.',
        )

        self.assertEqual(contact.first_name, 'John')
        self.assertEqual(contact.last_name, 'Doe')
        self.assertEqual(contact.email, 'test@example.com')
        self.assertEqual(contact.subject, 'Test Subject')
        self.assertEqual(contact.message, 'This is a test message.')
        self.assertIsInstance(contact.date_sent, timezone.datetime)

    def test_contact_model_str_representation_with_full_name(self):

        contact = Contact.objects.create(
            first_name='John',
            last_name='Doe',
            email='test@example.com',
            subject='Test Subject',
            message='This is a test message.',
        )

        self.assertEqual(str(contact), 'John Doe')

    def test_contact_model_str_representation_with_email_only(self):

        contact = Contact.objects.create(
            email='test@example.com',
            subject='Test Subject',
            message='This is a test message.',
        )

        self.assertEqual(str(contact), 'test@example.com')

    def test_contact_model_validation_with_invalid_email(self):
        # Attempt to create a contact form with an invalid email address
        with self.assertRaises(ValidationError) as context:
            Contact.objects.create(
                email='invalidemai@l',
                subject='Test Subject',
                message='This is a test message.',
            )

        # Check that the correct validation error is raised
        self.assertEqual(context.exception.messages[0], 'Please, enter a valid email address!')

    def test_contact_model_validation_with_short_subject(self):
        # Attempt to create a contact form with a subject that is too short
        with self.assertRaises(ValidationError) as context:
            Contact.objects.create(
                email='test@example.com',
                subject='Hi',
                message='This is a test message.',
            )

        # Check that the correct validation error is raised
        self.assertEqual(context.exception.messages[0], 'Subject must be at least 5 characters long!')

    def test_contact_model_validation_with_short_message(self):
        # Attempt to create a contact form with a message that is too short
        with self.assertRaises(ValidationError) as context:
            Contact.objects.create(
                email='test@example.com',
                subject='Test Subject',
                message='Short',
            )

        # Check that the correct validation error is raised
        self.assertEqual(context.exception.messages[0], 'Message must be at least 10 characters long!')
