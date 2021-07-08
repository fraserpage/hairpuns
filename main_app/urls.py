from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('hairpuns/', views.hairpuns_index, name='index'),
  path('hairpuns/<int:pun_id>', views.hairpuns_details, name='details'),
  path('hairpuns/create', views.HairpunCreate.as_view(), name='hairpuns_create'),
  path('hairpuns/<int:pk>/update', views.HairpunUpdate.as_view(), name='hairpuns_update'),
  path('hairpuns/<int:pk>/delete', views.HairpunDelete.as_view(), name='hairpuns_delete'),
]