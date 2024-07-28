from django.urls import path
from . import views

urlpatterns = [    
    path('entry/', views.OperacionesListView.as_view(), name='operation_changelist'),           
    path('entry/add/', views.OperacionesCreateView.as_view(), name='operation_add'),    
    path('entry/<int:pk>/', views.OperacionesUpdateView.as_view(), name='operation_change'),
    path('entry/ajax/load_subcategories/', views.load_subcategories, name='ajax_load_subcategories'),
    path('gd/entry/', views.GastoDiarioListView.as_view(), name='gastodiario_changelist'),
    path('gd/entry/add/', views.GastoDiarioCreateView.as_view(), name='gastodiario_add'),
    path('gd/entry/<int:pk>/', views.GastoDiarioUpdateView.as_view(), name='gastodiario_change'),     
    ]