from django.urls import path, include
from . import views

urlpatterns = [
    path('registration/', views.login, name='login'),
    path('Home/', views.index2, name = 'index2'),
    path('Instruction/', views.Instruction, name='Instruction'),
    path('Menu/', views.Menu, name="Menu"),
]

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]