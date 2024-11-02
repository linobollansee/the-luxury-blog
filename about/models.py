from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class About(models.Model):
    """
    Stores a single about me text
    """
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    # Added profile_image2 variable and field type
    profile_image2 = CloudinaryField('image2', default='placeholder2')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title


class CollaborateRequest(models.Model):
    """
    Stores a single collaboration request message
    """
    name = models.CharField(max_length=200)
    # Added luxury_category variable and field type
    luxury_category = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        return f"Collaboration request from {self.name}"