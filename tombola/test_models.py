# Import necessary modules and classes
from datetime import datetime  # Import datetime for date/time checks

from django.core.exceptions import ValidationError  # For validation errors
from django.db import IntegrityError  # For database integrity errors
from django.test import TestCase  # For creating test cases in Django

# Import the Participant model from the current application
from .models import Participant


class ParticipantModelTest(TestCase):
    """
    A test case class for testing the Participant model's functionality.

    This class inherits from Django's TestCase, providing methods for
    testing database models and their behavior.
    """

    def setUp(self):
        """
        Set up the test case environment before each test method runs.

        This method creates a sample Participant instance for use in
        multiple test methods.
        """
        self.participant = Participant.objects.create(
            name="John Doe",  # Set the name of the participant
            email="johndoe@example.com"  # Set the email of the participant
        )

    def test_participant_creation(self):
        """
        Test that a Participant instance is created correctly.

        This method checks if the attributes of the created Participant
        match the expected values.
        """
        # Assert that the name of the participant matches the expected value
        self.assertEqual(self.participant.name, "John Doe")
        # Assert that the email of the participant matches the expected value
        self.assertEqual(self.participant.email, "johndoe@example.com")
        # Check that the created_at field is a datetime instance
        self.assertIsInstance(self.participant.created_at, datetime)

    def test_string_representation(self):
        """
        Test the string representation of the Participant instance.

        This method checks if the string representation of the
        Participant instance returns the correct name.
        """
        # Assert that converting the participant to a string returns the name
        self.assertEqual(str(self.participant), "John Doe")

    def test_unique_email_constraint(self):
        """
        Test that email addresses for Participants are unique.

        This method verifies that attempting to create a second
        Participant with the same email raises an IntegrityError.
        """
        # Use a context manager to assert that IntegrityError is raised
        with self.assertRaises(IntegrityError):
            Participant.objects.create(
                name="Jane Doe",  # Create new participant with the same email
                email="johndoe@example.com"  # Same email
            )

    def test_max_length_name(self):
        """
        Test that the maximum length for the Participant's name is enforced.

        This method checks that trying to create a Participant with a
        name longer than the allowed maximum length raises a
        ValidationError.
        """
        # Create a string that exceeds the maximum length for the name
        max_length_name = 'a' * 101  # Assuming max length is 100
        # Use a context manager to assert that ValidationError is raised
        with self.assertRaises(ValidationError):
            # Create a participant with an excessively long name
            participant = Participant(
                name=max_length_name,
                email="test@example.com"
            )
            # Trigger model validation
            participant.full_clean()  # This will validate all fields

    def test_valid_email(self):
        """
        Test that an invalid email format raises a ValidationError.

        This method verifies that creating a Participant with an
        improperly formatted email address triggers a validation error.
        """
        # Use a context manager to assert that ValidationError is raised
        with self.assertRaises(ValidationError):
            # Create a participant with an invalid email format
            participant = Participant(
                name="Invalid Email",
                email="invalidemail.com"
            )
            # Trigger model validation
            participant.full_clean()  # This will check the email format
