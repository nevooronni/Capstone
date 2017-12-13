from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

Gender_Choices = (
		('Female', 'female'),
		('Male', 'male'),
		('Both', 'both'),
		('None', 'non-specified'),
	)

class Creator(models.Model):
	first_name = models.CharField(max_length = 50)
	last_name = models.CharField(max_length = 50)
	email = models.EmailField()
	phone = models.PositiveIntegerField()
	profession = models.CharField(max_length = 30)
	password = models.CharField(max_length=30)
	
	@classmethod
	def creators_list(cls):
		creators = Creator.objects.all()
		return creators

class CreatorProfile(models.Model):
	creator = models.OneToOneField(Creator,on_delete=models.CASCADE)
	prof_pic = models.ImageField(blank=True,upload_to='Rider/prof_pic',default="Rider/prof_pic/prof_pic.png")
	email = models.EmailField()
	gender = models.CharField(max_length=30,choices=Gender_Choices,default='None',blank=True)
	general_location = models.CharField(blank=True,max_length=255)

	def __str__(self):
		return self.creator.first_name + '' + self.creator.last_name	

	@classmethod
	def creators_profile_list(cls):
		creators_profiles = CreatorProfile.objects.all()
		return creators_profiles

	@receiver(post_save,sender=Creator)
	def create_profile(sender,instance,created,**kwargs):
		if created:
			CreatorProfile.objects.create(creator=instance)

	@receiver(post_save,sender=Creator)
	def save_profile(sender,instance,**kwargs):
		instance.creatorprofile.save()