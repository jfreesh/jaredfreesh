from django.urls import path
from . import views

urlpatterns = [
	path('', views.crypto, name="crypto"),
	path('prices/', views.prices, name="prices"),
]