from django.db import models


class Course(models.Model):
	title = models.CharField(max_length=160)
	short_description = models.CharField(max_length=220)
	image = models.ImageField(upload_to='courses/', blank=True, null=True)
	age_range = models.CharField(max_length=60, blank=True, default='من 6 أشهر حتى 9 سنوات')
	cta_text = models.CharField(max_length=60, default='ابدأ الآن')
	order = models.PositiveIntegerField(default=1)
	tag = models.CharField(max_length=120, blank=True, help_text='مثال: نشاط, لغة',default='لغة')
	is_published = models.BooleanField(default=True)

	class Meta:
		ordering = ['order', 'id']

	def __str__(self):
		return self.title
