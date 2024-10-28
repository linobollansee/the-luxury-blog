# Importing the TestCase class from Django's test framework,
# which provides tools for creating unit tests for Django applications.
from django.test import TestCase

# Importing the CollaborateForm class from the forms module.
from .forms import CollaborateForm

# Defining a test case class for the CollaborateForm.
# This class inherits from TestCase, allowing us to create tests for the form.


class TestCollaborateForm(TestCase):

    # Test method to check if the form is valid with all required fields.
    def test_form_is_valid(self):
        """Test for all fields to ensure the form is valid."""

        # Creating an instance of the CollaborateForm with valid data.
        form = CollaborateForm(
            {
                'name': 'test',  # Providing a name
                'luxury_category': 'Diamonds',  # Providing a luxury category
                'email': 'test@test.com',  # Providing a valid email address
                'message': 'Hello!'  # Providing a message
            }
        )

        # Asserting that the form is valid. If not, show an error message.
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    # Test method to check if the 'name' field is required.
    def test_name_is_required(self):
        """Test for the 'name' field to ensure it is mandatory."""

        # Creating an instance of CollaborateForm with an empty 'name' field.
        form = CollaborateForm(
            {
                'name': '',  # Empty name field
                'luxury_category': 'Diamonds',  # Provide valid luxury category
                'email': 'test@test.com',  # Providing valid email address
                'message': 'Hello!'  # Providing a message
            }
        )

        # Asserting that the form is invalid because the name field is empty.
        self.assertFalse(
            form.is_valid(),
            msg="Name was not provided, but the form is valid"
        )

    # Test method to check if the 'luxury_category' field is required.
    def test_luxury_category_is_required(self):
        """Test for the 'luxury_category' field to ensure it is mandatory."""

        # Create an instance of CollaborateForm with empty 'luxury_category'.
        form = CollaborateForm(
            {
                'name': 'Matt',  # Provide a valid name
                'luxury_category': '',  # Empty luxury category
                'email': 'test@test.com',  # Provide a valid email address
                'message': 'Hello!'  # Provide a message
            }
        )

        # Asserting form is invalid because the luxury category field is empty.
        self.assertFalse(
            form.is_valid(),
            msg="Luxury category was not provided, but the form is valid"
        )

    # Test method to check if the 'email' field is required.
    def test_email_is_required(self):
        """Test for the 'email' field to ensure it is mandatory."""

        # Create instance of the CollaborateForm with an empty 'email' field.
        form = CollaborateForm(
            {
                'name': 'Matt',  # Provide a valid name
                'luxury_category': 'Diamonds',  # Provide valid luxury category
                'email': '',  # Empty email field
                'message': 'Hello!'  # Provide a message
            }
        )

        # Asserting that the form is invalid because the email field is empty.
        self.assertFalse(
            form.is_valid(),
            msg="Email was not provided, but the form is valid"
        )

    # Test method to check if the 'message' field is required.
    def test_message_is_required(self):
        """Test for the 'message' field to ensure it is mandatory."""

        # Create an instance of CollaborateForm with an empty 'message' field.
        form = CollaborateForm(
            {
                'name': 'Matt',  # Provide a valid name
                'luxury_category': 'Diamonds',  # Provide valid luxury category
                'email': 'test@test.com',  # Provide valid email address
                'message': ''  # Empty message field
            }
        )

        # Asserting the form is invalid because the message field is empty.
        self.assertFalse(
            form.is_valid(),
            msg="Message was not provided, but the form is valid"
        )
