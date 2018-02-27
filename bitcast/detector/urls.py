from django.urls import path
from . import views
app_name='detector'
urlpatterns = [
    path('', views.main, name='main'),
    path('<int:pk>/', views.keyword_detail, name='keyword_detail'),

    path('new/<int:pk>/', views.keyword_new, name='keyword_new'),
]