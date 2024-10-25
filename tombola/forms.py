# Import the necessary classes from Django forms and the Participant model
from django import forms  # Importing Django's forms module for creating forms
from .models import Participant  # Importing the Participant model


class ParticipantForm(forms.ModelForm):
    """
    A form for creating and updating Participant instances.

    This form is based on the Participant model and includes fields
    for participant's name and email.
    """

    class Meta:
        """
        Meta class to define additional properties for the form.
        """
        # Specify the model that this form is associated with
        model = Participant
     
        # Define the fields to be included in the form
        fields = ['name', 'email']  # Only the fields will be rendered.
