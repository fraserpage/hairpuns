from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('hairpuns/', views.hairpuns_index, name='index'),
  path('hairpuns/<int:pun_id>', views.hairpuns_details, name='details')
]