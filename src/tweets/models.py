from django.conf import settings
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.db import models

from .validators import validate_content

# Create your models here.

class Tweet(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1)
	content = models.CharField(max_length = 140, validators = [validate_content])
	updated = models.DateTimeField(auto_now = True)
	timestamp = models.DateTimeField(auto_now_add = True)

	def __str__(self):
		#Can use other fields such as id.
		return str(self.content)

	# def clean(self, *args, **kwargs):
	# 	content = self.content
	# 	if content == "abc":
	# 		raise ValidationError("Content cannot be ABC")
	# 	return super(Tweet, self).clean(*args, **kwards)

	def get_absolute_url(self):
		return reverse("tweet:detail", kwargs = {"pk": self.pk})
