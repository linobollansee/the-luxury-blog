from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """
    Form class for users to request a collaboration
    """
    class Meta:
        """
        Specify the django model and order of the fields
        """
        model = CollaborateRequest
        # Added luxury_category variable
        fields = ('name', 'luxury_category', 'email', 'message')