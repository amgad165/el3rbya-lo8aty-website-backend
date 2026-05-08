from django.contrib import admin
from .models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
	list_display = ('full_name', 'title', 'order', 'is_published')
	list_filter = ('is_published',)
	search_fields = ('full_name', 'title', 'bio')
	ordering = ('order', 'id')
