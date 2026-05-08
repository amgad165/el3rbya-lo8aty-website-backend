from django.contrib import admin
from .models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
	list_display = ('title', 'age_range', 'order', 'is_published')
	list_filter = ('is_published',)
	search_fields = ('title', 'short_description')
	ordering = ('order', 'id')
