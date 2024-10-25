# Import the 'path' function from Django's 'urls' module.
# The 'path' function is used to define URL patterns for the application.
from django.urls import path

# Import the 'tombola_view' from the current app's 'views' module.
# The dot (.) indicates a relative import, from the current directory.
from .views import tombola_view

# Create a list of URL patterns for the app.
urlpatterns = [
    # Define a single URL pattern:

    # The 'path' function takes three arguments:
    # 1. The first argument ('') defines the URL pattern.
    # An empty string ('') means the root of the app.
    # When the base URL of this app is visited, the view will be executed.

    # 2. The second argument ('tombola_view') is the view function that will be
    # called when the user navigates to the URL. This view function will handle
    # the request and return a response.

    # 3. The third argument ('name="tombola"') is an optional name for the URL.
    # This 'name' allows you to refer to this URL in your templates, views, or
    # anywhere in your app, instead of hardcoding the actual URL.
    path('', tombola_view, name='tombola'),
]
