from django.urls import path
from . import views
urlpatterns = [
    path('', views.sign_in, name='sign_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('logout/', views.sign_out, name='sign_out'),
    path('edit/<int:id>/',views.edit_transactions, name='edit'),
    path('home/',views.home_page, name='home'),
    path('add/', views.add_transactions, name='add'),
    path('filter/',views.filter_items , name='filter')
]