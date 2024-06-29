from django.urls import path,include
from .import views

urlpatterns = [
    path('web_scrapping_content/',views.scrape_web_content,name='scrap_web_content')
]
