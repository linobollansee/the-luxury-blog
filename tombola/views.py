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

    participants = Participant.objects.all()
    return render(request, 'tombola/tombola.html',
                  {'form': form, 'participants': participants})
