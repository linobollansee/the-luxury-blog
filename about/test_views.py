from django.test import TestCase  # Import TestCase to create test cases
from django.urls import reverse  # Import reverse to generate URLs by own name
# Import About model to interact with about content in the test
from .models import About
# Import CollaborateForm to verify form existence in the view context
from .forms import CollaborateForm


class TestAboutView(TestCase):
    """Test case for the 'About' view"""

    def setUp(self):
        """Sets up initial test data for the About view."""
        # Create an instance of About model with sample 'About Me' content
        self.about_content = About(
            title="About Me", content="This is about me.")
        self.about_content.save()  # Save the instance to the test database

    def test_render_about_page_with_collaborate_form(self):
        """Tests rendering of the About page, checking for a form."""
        # Simulate a GET request to the 'about' URL
        response = self.client.get(reverse('about'))

        # Verify the response status is 200 (successful)
        self.assertEqual(response.status_code, 200)

        # Check if the content 'About Me' is present in the response
        self.assertIn(b'About Me', response.content)

        # Verify 'collaborate_form' is an instance of CollaborateForm
        self.assertIsInstance(
            response.context['collaborate_form'], CollaborateForm)

    def test_successful_collaboration_request_submission(self):
        """Tests submission of a collaboration request via POST."""
        # Define POST data to simulate a form submission
        post_data = {
            'name': 'test name',
            'luxury_category': 'Diamonds',
            'email': 'test@test.com',
            'message': 'test message'
        }

        # Simulate a POST request to the 'about' URL with the post_data
        response = self.client.post(reverse('about'), post_data)

        # Verify the response status is 200 (successful)
        self.assertEqual(response.status_code, 200)

        # Check if a success message is in the response content
        self.assertIn(
            b'Form received! Thank you for your interest.', response.content)
