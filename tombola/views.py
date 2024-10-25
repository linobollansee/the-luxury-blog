# Import the messages framework to display one-time notifications to the user.
from django.contrib import messages
# Import the Paginator class from Django to handle pagination.
from django.core.paginator import Paginator
# Import render and redirect functions to render templates, handle redirects.
from django.shortcuts import render, redirect


# Import the Participant model, it represents the participants in the database.
from .models import Participant
# Import the ParticipantForm form class for form submissions, validations.
from .forms import ParticipantForm


# Define a view function for handling the Tombola page.
# This view handles both form submissions and renders the participant list.
def tombola_view(request):
    # Check if the request is a POST request when the form is being submitted.
    if request.method == 'POST':
        # Create a form instance with the submitted data (request.POST).
        form = ParticipantForm(request.POST)

        # Check if the form is valid (passes all validated fields)
        if form.is_valid():
            # If the form is valid, save the participant to the database.
            form.save()

            # Add a success message that will be shown on the next page load
            messages.add_message(
                request, messages.SUCCESS,
                'Your Tombola participation has been successfully registered!'
            )

            # After saving the data and adding a success message, redirect the
            # user back to the tombola page. This prevents the form from being
            # resubmitted if the user refreshes the page.
            return redirect('tombola')

    # If the request is not a POST, create an empty form instance.
    # This is the case when the user first visits the page.
    else:
        form = ParticipantForm()

    # Fetch all participants from the database, in descending order.
    participants_list = Participant.objects.all().order_by('-created_at')

    # Create a paginator object that will divide the participants list into
    # pages, showing 10 participants per page.
    paginator = Paginator(participants_list, 10)  # 10 participants per page

    # Get the page number from the URL query parameters.
    # If not present, defaults to the first page.
    page_number = request.GET.get('page')

    # Use the paginator to retrieve the participants for the requested page.
    # If the page_number is not provided, it will return the first page.
    participants = paginator.get_page(page_number)

    # Render the 'tombola/tombola.html' template with the context data:
    # - 'form': the form instance to be displayed on the page.
    # - 'participants': the paginated list of participants.
    return render(request, 'tombola/tombola.html', {
        'form': form,
        'participants': participants
    })
