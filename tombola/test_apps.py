# Import TestCase from Django's testing framework
from django.test import TestCase

# Import the Tombola application configuration
from .apps import TombolaAppConfig


class TombolaAppConfigTest(TestCase):
    """Test case for the Tombola application configuration."""

    def test_app_config(self):
        """Test that the application name is set correctly."""
        # Assert that the name of the application matches the expected value
        self.assertEqual(TombolaAppConfig.name, 'tombola')

    def test_default_auto_field(self):
        """Test that the default auto field is set correctly."""
        # Assert that the default_auto_field is set to BigAutoField
        self.assertEqual(
            TombolaAppConfig.default_auto_field,
            'django.db.models.BigAutoField'
        )
