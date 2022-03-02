from django.urls import path, re_path

from .views_ajax import get_dni
from .views import LoginNuevo
from .views_plans import checkout

urlpatterns = [
    
    path('login-nuevo/', LoginNuevo.as_view(), name='login-nuevo'),
    path('dni/', get_dni, name='dni'),
    path('checkout/', checkout, name='checkout'),

]