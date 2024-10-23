from django.test import TestCase
from .models import Participant


class ParticipantModelTest(TestCase):
    def setUp(self):
        Participant.objects.create(name="John Doe", email="john@example.com")

    def test_participant_str(self):
        participant = Participant.objects.get(id=1)
        self.assertEqual(str(participant), "John Doe")
