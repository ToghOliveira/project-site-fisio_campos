from django.urls import path

from FisioCampos_site_home.views import home_page

urlpatterns = [
    path('', home_page),  # home
]
