from django.db import models


class Teacher(models.Model):
	full_name = models.CharField(max_length=120)
	title = models.CharField(max_length=120, blank=True)
	bio = models.TextField(blank=True)
	image = models.ImageField(upload_to='teachers/', blank=True, null=True)
	order = models.PositiveIntegerField(default=1)
	is_published = models.BooleanField(default=True)

	class Meta:
		ordering = ['order', 'id']

	def __str__(self):
		return self.full_name
