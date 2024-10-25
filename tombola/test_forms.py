# Import necessary Django form functionalities.
from django import forms
# Import TestCase from Django's testing framework to create unit tests.
from django.test import TestCase
# Import the ParticipantForm from the local forms module for testing.

from .forms import ParticipantForm
# Import the Participant model from the local models module.
from .models import Participant


class ParticipantFormTest(TestCase):
    """Unit tests for the ParticipantForm, ensuring it behaves correctly
    with valid and invalid input data.
    """

    def test_form_valid_data(self):
        """Test the form's behavior when provided with valid data."""
        # Define a dictionary with valid participant information, including
        # name and email fields.
        form_data = {
            'name': 'John Doe',
            'email': 'john.doe@example.com'
        }
        # Create an instance of ParticipantForm with the valid data.
        form = ParticipantForm(data=form_data)
        # Assert that the form is valid as the provided data meets all
        # the requirements.
        self.assertTrue(form.is_valid())
        # Verify that the cleaned data for 'name' matches the input data.
        self.assertEqual(form.cleaned_data['name'], 'John Doe')
        # Verify that the cleaned data for 'email' matches the input data.
        self.assertEqual(form.cleaned_data['email'],
                         'john.doe@example.com')

    def test_form_invalid_data_missing_name(self):
        """Test the form's behavior when the 'name' field is missing."""
        # Define form data that only includes an email, omitting the name.
        form_data = {
            'email': 'john.doe@example.com'
        }
        # Create an instance of ParticipantForm with the incomplete data.
        form = ParticipantForm(data=form_data)
        # Assert that the form is invalid because the 'name' field is required.
        self.assertFalse(form.is_valid())
        # Check if an error for the 'name' field is present in the form's
        # errors dictionary.
        self.assertIn('name', form.errors)
        # Assert that the error message indicates that the field is required.
        self.assertEqual(form.errors['name'], ['This field is required.'])

    def test_form_invalid_data_missing_email(self):
        """Test the form's behavior when the 'email' field is missing."""
        # Define form data that only includes a name, omitting the email.
        form_data = {
            'name': 'John Doe'
        }
        # Create an instance of ParticipantForm with the incomplete data.
        form = ParticipantForm(data=form_data)
        # Assert that the form is invalid because 'email' field is required.
        self.assertFalse(form.is_valid())
        # Check if an error for the 'email' field is present in the form's
        # errors dictionary.
        self.assertIn('email', form.errors)
        # Assert that the error message indicates that the field is required.
        self.assertEqual(form.errors['email'], ['This field is required.'])

    def test_form_invalid_email_format(self):
        """Test the form's behavior when an invalid email format is provided"""
        # Define form data that includes an invalid email format.
        form_data = {
            'name': 'John Doe',
            'email': 'not-an-email'
        }
        # Create an instance of ParticipantForm with the invalid email.
        form = ParticipantForm(data=form_data)
        # Assert that the form is invalid due to the incorrect email format.
        self.assertFalse(form.is_valid())
        # Check if an error for the 'email' field is present in the form's
        # errors dictionary.
        self.assertIn('email', form.errors)
        # Assert that the error message indicates the email format is invalid.
        self.assertEqual(form.errors['email'],
                         ['Enter a valid email address.'])

    def test_form_with_existing_email(self):
        """Test the form's behavior when an existing email is submitted."""
        # Create a participant with an email to test against existing entries.
        Participant.objects.create(name='Jane Doe',
                                   email='jane.doe@example.com')
        # Define form data that includes the existing email.
        form_data = {
            'name': 'John Doe',
            'email': 'jane.doe@example.com'  # same email as existing
        }
        # Create an instance of ParticipantForm with the data containing
        # the existing email.
        form = ParticipantForm(data=form_data)
        # Note: Add assertions to check the form's behavior regarding
        # duplicate emails as needed.

    def test_form_empty_data(self):
        """Test the form's behavior when no data is provided."""
        # Create an instance of ParticipantForm with empty data.
        form = ParticipantForm(data={})
        # Assert the form is invalid because both required fields are empty.
        self.assertFalse(form.is_valid())
        # Check if an error for the 'name' field is present in the form's
        # errors dictionary.
        self.assertIn('name', form.errors)
        # Check if an error for the 'email' field is present in the form's
        # errors dictionary.
        self.assertIn('email', form.errors)
