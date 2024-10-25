# Import necessary modules from Django
from django.urls import reverse  # Allows us to reverse resolve URLs
from django.test import SimpleTestCase  # Provides a way to create simple tests


# Define a test case class for URL testing, inheriting from SimpleTestCase
class UrlsTestCase(SimpleTestCase):

    # Define a test method to check the URL for the tombola view
    def test_tombola_url(self):
        """
        Test that the tombola URL resolves correctly to the tombola_view.

        This method checks if the URL associated with the name 'tombola' can
        be correctly resolved to the expected path. It ensures that the URL
        configuration is set up correctly in the Django project.
        """

        # Use Django's reverse function to get the URL for the tombola view
        url = reverse('tombola')

        # Assert that the resolved URL matches the expected URL pattern
        self.assertEqual(url, '/tombola/')
