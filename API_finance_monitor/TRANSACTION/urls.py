from django.urls import include, path
from . import views

urlpatterns = [    
    path('', views.OperacionesListView.as_view(), name='operation_changelist'),
    path('add/', views.OperacionesCreateView.as_view(), name='operation_add'),
    path('<int:pk>/', views.OperacionesUpdateView.as_view(), name='operation_change'),
    path('ajax/load_subcategories/', views.load_subcategories, name='ajax_load_subcategories'),
    ]