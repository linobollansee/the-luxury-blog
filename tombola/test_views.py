# Import necessary modules for testing
from django.contrib.messages import get_messages  # For testing messages
from django.test import TestCase  # Base class for creating test cases
from django.urls import reverse  # Utility for reversing URL patterns

from .forms import ParticipantForm  # Import the form used in the view
from .models import Participant  # Import the Participant model


class TombolaViewTests(TestCase):
    """
    Test suite for the Tombola view functionality.

    This class contains various test cases to ensure the Tombola view
    behaves as expected. It tests GET and POST requests, form validation,
    and pagination.
    """

    def setUp(self):
        """
        Set up the initial conditions for the test cases.

        This method is called before every test method to set up any state
        that's shared across tests. Here, we define the URL and valid
        participant data for testing.
        """
        # Define the URL for the tombola view using reverse lookup
        self.url = reverse('tombola')

        # Define valid participant data for testing the form
        self.participant_data = {
            'name': 'Test Participant',  # Valid name for the participant
            'email': 'test@example.com',  # Valid email address
            # Other required fields for the ParticipantForm can be added here
        }

    def test_tombola_view_get(self):
        """
        Test tombola view returns correct template and context on GET request.

        This test ensures that when the tombola view is accessed via a GET
        request, it returns the correct HTTP status code, template, and
        context variables.
        """
        # Simulate a GET request to the tombola view
        response = self.client.get(self.url)

        # Check that the response has a status code of 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Ensure that the correct template is used for rendering the response
        self.assertTemplateUsed(response, 'tombola/tombola.html')

        # Verify that 'form' and 'participants' are included in the response
        self.assertIn('form', response.context)
        self.assertIn('participants', response.context)

        # Ensure the form in context is an instance of ParticipantForm
        self.assertIsInstance(response.context['form'], ParticipantForm)

    def test_tombola_view_post_valid(self):
        """
        Test tombola view processes valid form data correctly.

        This test checks that when valid participant data is posted to the
        tombola view, it processes the data correctly and creates a new
        participant.
        """
        # Simulate a POST request with valid participant data
        response = self.client.post(self.url, self.participant_data)

        # Check that the response redirects after successful submission
        self.assertEqual(response.status_code, 302)  # 302 means a redirect

        # Verify that a new participant has been created in the database
        self.assertEqual(Participant.objects.count(), 1)

        # Ensure that the created participant's name matches the expected name
        self.assertEqual(
            Participant.objects.first().name,
            'Test Participant'
        )

        # Check that a success message was added to the request
        messages = list(get_messages(response.wsgi_request))  # Retrieve msgs
        self.assertEqual(len(messages), 1)  # Ensure one message exists
        self.assertEqual(
            messages[0].message,
            'Your Tombola participation has been successfully registered!'
        )

    def test_tombola_view_post_invalid(self):
        """
        Test tombola view handles invalid form data correctly.

        This test ensures that when invalid data is submitted to the tombola
        view, it returns to the form without creating a new participant.
        """
        # Define invalid participant data (missing required name field)
        invalid_data = {
            'name': '',  # Invalid: name is required and cannot be empty
            'email': 'test@example.com',  # Valid email, but data is invalid
        }

        # Simulate a POST request with invalid participant data
        response = self.client.post(self.url, invalid_data)

        # Check that the response returns a status code of 200
        self.assertEqual(response.status_code, 200)

        # Verify that no new participants were created in the database
        self.assertEqual(Participant.objects.count(), 0)

    def test_tombola_view_pagination(self):
        """
        Test pagination works correctly in the tombola view.

        This test ensures that when there are more participants than can
        fit on one page, the pagination correctly displays the participants
        across multiple pages.
        """
        # Create 25 participant instances for testing pagination
        for i in range(25):
            Participant.objects.create(
                name=f'Participant {i}',
                email=f'participant{i}@example.com'
            )

        # Simulate a GET request to retrieve the second page of participants
        response = self.client.get(self.url + '?page=2')

        # Check that the response status is OK
        self.assertEqual(response.status_code, 200)

        # Verify that the response contains exactly 10 participants (per page)
        self.assertEqual(len(response.context['participants']), 10)

        # Ensure that the participants object is on the second page
        self.assertEqual(response.context['participants'].number, 2)
