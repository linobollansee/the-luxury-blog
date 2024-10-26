# Importing models from Django's ORM library, which provides tools for
# creating, manipulating, and querying database structures using Python objects
from django.db import models


# Defining a Django model, which represents a table structure in the database.
class Participant(models.Model):
    # Creating a character field to store the participant's name.
    # max_length=100 sets maximum number of characters for this field to 100.
    name = models.CharField(max_length=100)

    # Defining an email field with Django's built-in EmailField, which
    # automatically validates that values entered into this field are formatted
    # as email addresses. Setting unique as True ensures that each email in the
    # table is unique, preventing duplicates.
    email = models.EmailField(unique=True)

    # Adding a DateTime field that records when each participant was created.
    # The auto_now_add=True argument automatically sets the field to the
    # current timestamp when a record is created.
    created_at = models.DateTimeField(auto_now_add=True)

    # Defining a string representation for instances of this model.
    # When a Participant object is printed or converted to a string, it will
    # display the participant's name.
    def __str__(self):
        return self.name
