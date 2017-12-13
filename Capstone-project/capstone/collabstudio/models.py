from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
import datetime as dt
from django.db.models import Sum
from liked.models import Like
from django.contrib.contenttypes.fields import GenericRelation


Gender_Choices = (
		('Female', 'female'),
		('Male', 'male'),
		('Both', 'both'),
		('None', 'non-specified'),
	)

DEFAULT = 'profile/'

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)#USER Models
	bio = models.TextField(max_length=500, blank=True)
	website = models.CharField(max_length=30,blank=True)
	email = models.EmailField()
	phone_number = PhoneNumberField(max_length=10, blank=True)
	photo = models.ImageField(upload_to = 'profile/',blank=True,default=False)
	gender = models.CharField(max_length=30,choices=Gender_Choices,default='None',blank=True)

	@classmethod
	def retrieve_profiles(cls):
		all_profiles = Profile.objects.all().order_by('-id')
		return all_profiles

	@classmethod
	def retrieve_other_profiles(cls,user_id):
		profiles = Profile.objects.all()

		other_profiles = []

		for profile in profiles:

			if profile.user.id != user_id:
				other_profiles.append(profile)

		return other_profiles

	@receiver(post_save, sender=User)
	def create_user_profile(sender, instance, created, **kwargs):
		if created:
			Profile.objects.create(user=instance)

	@receiver(post_save, sender=User)
	def save_user_profile(sender, instance, **kwargs):
		instance.profile.save()
	@property 
	def photo_url(self):
		if self.photo and hasattr(self.photo, 'url'):
			return self.photo.url	


class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()

class Tags(models.Model):
	title = models.CharField(max_length=30, unique=True)

	def __str__(self):
		return self.title
	class Meta:
		ordering = ['title']#ordering data everytime can be tedious meta subclass to specify model-specific options 

	def save_tag(self):
		self.save()

	def delete_tag(self):
		self.delete()

	@classmethod
	def retrieve_tags(cls):
		tags = Tags.objects.all()
		return tags

class Post(models.Model):
	post_time = models.DateTimeField(auto_now_add=True)
	tags = models.ManyToManyField(Tags, blank=True)
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
	photo = models.ImageField(upload_to = 'photos/',blank=True,default=False)
	caption = models.TextField(blank=True)
	likes = GenericRelation(Like)
	
	def __str__(self):
		return self.user.username
	class Meta:
		ordering = ['-post_time']#orders with the most recent at the top
	
	@classmethod
	def retrieve_profile_posts(cls,profile_id):
		prof_posts = Post.objects.filter(profile=profile_id).all()
		return prof_posts

	@classmethod
	def retrieve_posts(cls):
		posts = Post.objects.all()
		return posts

	@classmethod
	def retrieve_single_post(cls,pk):
		post = cls.objects.get(pk=pk)
		return post

	@property
	def image_url(self):
		if self.photo and hasattr(self.photo, 'url'):
			return self.photo.url

class Follow(models.Model):
	user = models.ForeignKey(User)
	profile = models.ForeignKey(Profile)

	def __str__(self):
		return self.user.username

	@classmethod
	def retrieve_following(cls,user_id):
		following = Follow.objects.filter(user=user_id).all()
		return following 


class Comments(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	post = models.ForeignKey(Post,on_delete=models.CASCADE)
	comment = models.TextField(blank=True)

	def __str__(self):
		return self.user.username

	@classmethod
	def retrieve_post_comments(cls,post_id):
		post_comments = Comments.objects.filter(post=post_id)
		return post_comments

