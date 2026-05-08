from django.templatetags.static import static
from rest_framework.response import Response
from rest_framework.views import APIView

from content.models import Feature, IntroSection, SiteSettings
from courses.models import Course
from people.models import Teacher


def _image_url(request, image_field):
	if image_field:
		return request.build_absolute_uri(image_field.url)
	return None


class PublicHomeView(APIView):
	def get(self, request):
		settings_obj = SiteSettings.objects.first()

		data = {
			'site': {
				'site_name': settings_obj.site_name if settings_obj else 'العربية لغتي',
				'hero_title': settings_obj.hero_title if settings_obj else 'نتعلّم ونلعب ونبني جيلاً مبدعاً',
				'hero_subtitle': settings_obj.hero_subtitle if settings_obj else '',
				'hero_description': settings_obj.hero_description if settings_obj else '',
				'cta_text': settings_obj.cta_text if settings_obj else 'ابدأ الآن',
				'phone': settings_obj.phone if settings_obj else '',
				'whatsapp': settings_obj.whatsapp if settings_obj else '',
				'location_text': settings_obj.location_text if settings_obj else '',
				'instagram_url': settings_obj.instagram_url if settings_obj else '',
				'facebook_url': settings_obj.facebook_url if settings_obj else '',
				'logo_url': request.build_absolute_uri(static('logo.png')),
			},
			'intro_sections': [
				{
					'id': item.id,
					'section_key': item.section_key,
					'title': item.title,
					'content': item.content,
					'image_url': _image_url(request, item.image),
					'image2_url': _image_url(request, item.image2),
				}
				for item in IntroSection.objects.filter(is_published=True)
			],
			'features': [
				{
					'id': item.id,
					'title': item.title,
					'description': item.description,
					'icon_url': _image_url(request, item.icon),
				}
				for item in Feature.objects.filter(is_published=True)
			],
			'courses': [
				{
					'id': item.id,
					'title': item.title,
					'short_description': item.short_description,
					'age_range': item.age_range,
					'cta_text': item.cta_text,
					'image_url': _image_url(request, item.image),
					'tag': item.tag,
				}
				for item in Course.objects.filter(is_published=True)
			],
			'teachers': [
				{
					'id': item.id,
					'full_name': item.full_name,
					'title': item.title,
					'bio': item.bio,
					'image_url': _image_url(request, item.image),
				}
				for item in Teacher.objects.filter(is_published=True)
			],
			'brand': {
				'primary': '#A89546',
				'primary_dark': '#6F6533',
				'heading': '#7B1E2B',
				'teal': '#1F6D88',
				'accent': '#E58A2C',
				'rose': '#C94E6A',
				'bg': '#F4ECDA',
				'text': '#2E3440',
				'font_family': 'Cairo',
			},
		}
		return Response(data)
