'''portfolio/urls.py'''

# Imports
from django.urls import path
from . import views

# URLs patterns
urlpatterns = [
    path('portfolio/', views.portfolio, name='portfolio'),
    path('', views.landing, name='landing'),
    path('projects/', views.projects, name='projects'),
    path('blog/', views.blog, name='blog'),
]
