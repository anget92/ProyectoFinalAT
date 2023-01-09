from django.urls import path
from appPasteleria.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', inicio, name='inicio'),
    path('register/', register, name='register'),
    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name='appPasteleria/index.html'), name='logout'),
    path('sobreMi/', sobreMi, name='sobreMi')
    
]