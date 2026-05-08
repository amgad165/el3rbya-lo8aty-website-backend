from django.db import models


class SiteSettings(models.Model):
	site_name = models.CharField(max_length=120, default='العربية لغتي')
	hero_title = models.CharField(max_length=255, default='نتعلّم ونلعب ونبني جيلاً مبدعاً')
	hero_subtitle = models.CharField(max_length=255, default='منال باسم بركات - حمادي')
	hero_description = models.TextField(default='منشدة تربوية ومعالجة تعليم ملائم وعسر تعليمي')
	cta_text = models.CharField(max_length=60, default='ابدأ الآن')
	phone = models.CharField(max_length=30, default='0522180851')
	whatsapp = models.CharField(max_length=30, default='0522180851')
	location_text = models.CharField(max_length=255, default='كابول - دوزيا شارع السهل')
	instagram_url = models.URLField(blank=True)
	facebook_url = models.URLField(blank=True)

	def __str__(self):
		return self.site_name


class IntroSection(models.Model):
	SECTION_KEY_CHOICES = [
		('about', 'من نحن'),
		('mission', 'رسالتنا'),
		
	]

	section_key = models.CharField(max_length=20, choices=SECTION_KEY_CHOICES, default='custom')
	title = models.CharField(max_length=160)
	content = models.TextField()
	image = models.ImageField(upload_to='intro_sections/', blank=True, null=True)
	image2 = models.ImageField(upload_to='intro_sections/', blank=True, null=True)
	order = models.PositiveIntegerField(default=1)
	is_published = models.BooleanField(default=True)

	class Meta:
		ordering = ['order', 'id']

	def __str__(self):
		return self.title


class Feature(models.Model):
	title = models.CharField(max_length=120)
	description = models.TextField()
	icon = models.ImageField(upload_to='feature_icons/', blank=True)
	order = models.PositiveIntegerField(default=1)
	is_published = models.BooleanField(default=True)

	class Meta:
		ordering = ['order', 'id']

	def __str__(self):
		return self.title
