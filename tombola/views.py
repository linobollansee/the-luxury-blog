from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Participant
from .forms import ParticipantForm


def tombola_view(request):
    if request.method == 'POST':
        form = ParticipantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Your Tombola participation has been successfully registered!'
            )
            return redirect('tombola')
    else:
        form = ParticipantForm()

    # Fetch all participants and apply pagination
    participants_list = Participant.objects.all().order_by('-created_at')
    paginator = Paginator(participants_list, 10)  # Show 10 participants per page
    page_number = request.GET.get('page')
    participants = paginator.get_page(page_number)

    return render(request, 'tombola/tombola.html', {
        'form': form,
        'participants': participants
    })
