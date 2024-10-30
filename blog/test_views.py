from django.test import TestCase  # Import Django's test framework
# Import the User model for authentication
from django.contrib.auth.models import User
from django.urls import reverse  # Import reverse to resolve URLs by name
from .forms import CommentForm  # Import the CommentForm for testing
from .models import Post  # Import the Post model


class TestBlogViews(TestCase):
    """Unit tests for blog views"""

    def setUp(self):
        """Set up test data: create a superuser and a sample blog post"""
        # Create a superuser for testing
        self.user = User.objects.create_superuser(
            username="myUsername", password="myPassword",
            email="test@test.com")
        # Create a sample blog post linked to the superuser
        self.post = Post(title="Blog title", author=self.user,
                         slug="blog-title", excerpt="Blog excerpt",
                         content="Blog content", status=1)
        self.post.save()  # Save the blog post to the test database

    def test_render_post_detail_page_with_comment_form(self):
        """Verify the post detail page renders correctly with a comment form"""
        # Get the detail page for the created blog post
        response = self.client.get(reverse('post_detail', args=['blog-title']))
        # Check if the page returns a status code of 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Verify that the post title and content are present in the response
        self.assertIn(b"Blog title", response.content)
        self.assertIn(b"Blog content", response.content)
        # Confirm that the page includes an instance of the CommentForm
        self.assertIsInstance(response.context['comment_form'], CommentForm)

    def test_successful_comment_submission(self):
        """Test posting a comment to a post"""
        # Log in the superuser to simulate an authenticated request
        self.client.login(username="myUsername", password="myPassword")
        # Define the post data for a comment submission
        post_data = {
            'body': 'This is a test comment.'
        }
        # Post the comment data to the post detail page
        response = self.client.post(
            reverse('post_detail', args=['blog-title']), post_data)
        # Ensure the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)
        # Check for a success message confirming comment submission
        self.assertIn(b'Comment submitted and awaiting approval',
                      response.content)
