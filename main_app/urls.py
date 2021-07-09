from django.urls import path
from . import views

urlpatterns = [
  # Static Pages
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),

  # Hairpuns 
  path('hairpuns/', views.hairpuns_index, name='index'),
  path('hairpuns/<int:pun_id>', views.hairpuns_details, name='details'),
  path('hairpuns/create', views.HairpunCreate.as_view(), name='hairpuns_create'),
  path('hairpuns/<int:pk>/update', views.HairpunUpdate.as_view(), name='hairpuns_update'),
  path('hairpuns/<int:pk>/delete', views.HairpunDelete.as_view(), name='hairpuns_delete'),
  path('hairpuns/<int:pun_id>/assoc_category/<int:category_id>/', views.assoc_category, name='assoc_category'),
  path('hairpuns/<int:pun_id>/un_assoc_category/<int:category_id>/', views.un_assoc_category, name='un_assoc_category'),
  
  # Create POST route for visits
  path('visit/create', views.visit_create, name='visit_create'),

  # Categories
  path('categories/', views.categories_index, name='categories_index'),
  path('category/<int:category_id>', views.category_details, name='category_details'),
  path('category/create', views.CategoryCreate.as_view(), name='category_create'),
  path('category/<int:pk>/update', views.CategoryUpdate.as_view(), name='category_update'),
  path('category/<int:pk>/delete', views.CategoryDelete.as_view(), name='category_delete'),
  path('category/deleted', views.category_deleted, name='category_deleted')
]