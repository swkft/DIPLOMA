from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  
    path('about/', views.about, name='about'),  
    path('log_in/', views.log_in, name='log_in'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('blog/', views.blog, name='blog'),
    path('for_therapist/', views.for_therapist, name='for_therapist'),
    path('help_center/', views.help_center, name='help_center'),
    path('article/', views.article, name='article'),
    path('all_therapist/', views.all_therapist, name='all_therapist'),
    path('user/', views.user, name='user'),
    path('therapist/', views.therapist, name='therapist'),



]
