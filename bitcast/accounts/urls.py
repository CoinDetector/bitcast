from django.urls import path
from django.contrib.auth.views import login,logout
from . import views
app_name='accounts'

urlpatterns = [
    path('login/', login,  name='login', kwargs={

            'template_name': 'accounts/login_form.html',
        }),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.profile, name='logout', kwargs={
        'next_page': 'login'}),
]