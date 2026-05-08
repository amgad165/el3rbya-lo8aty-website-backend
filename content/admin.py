from django.contrib import admin
from .models import Feature, IntroSection, SiteSettings


@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
	list_display = ('site_name', 'phone', 'location_text')


@admin.register(IntroSection)
class IntroSectionAdmin(admin.ModelAdmin):
	list_display = ('title', 'section_key', 'is_published')
	list_filter = ('section_key', 'is_published')
	search_fields = ('title', 'content')
	ordering = ('order', 'id')
	exclude = ('order',)

	def has_add_permission(self, request):
		return False


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
	list_display = ('title', 'order', 'is_published')
	list_filter = ('is_published',)
	search_fields = ('title', 'description')
	ordering = ('order', 'id')
