from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

Gender_Choices = (
		('Female', 'female'),
		('Male', 'male'),
		('Both', 'both'),
		('None', 'non-specified'),
	)

