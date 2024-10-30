from django.test import TestCase  # Import TestCase class for writing tests
from .forms import CommentForm  # Import the CommentForm from current package


class TestCommentForm(TestCase):
    # A test case class for testing the CommentForm functionality

    def test_form_is_valid(self):
        # Test that the form is valid when a valid body is provided
        # Create a CommentForm instance with a valid body
        comment_form = CommentForm({'body': 'This is a great post'})
        # Check that the form is valid and assert if it's not
        self.assertTrue(comment_form.is_valid(), msg="Form is invalid")

    def test_form_is_invalid(self):
        # Test that the form is invalid when no body is provided
        # Create a CommentForm instance with an empty body
        comment_form = CommentForm({'body': ''})
        # Check that the form is invalid and assert if it is
        self.assertFalse(comment_form.is_valid(), msg="Form is valid")
