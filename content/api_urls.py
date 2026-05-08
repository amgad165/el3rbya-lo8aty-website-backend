from django.urls import path

from content.views import PublicHomeView

urlpatterns = [
    path('public/home/', PublicHomeView.as_view(), name='public-home'),
]
