from django.urls import path
from . import views

app_name = 'papua'

urlpatterns = [
	path('', views.maps, name='maps_view'),
	path('data/ibadah/', views.religion, name='ibadah'),
	path('data/pendidikan/', views.pendidikan, name='pendidikan'),
	path('data/kabupaten/', views.kabupaten, name='kabupaten'),
	path('data/kab-point/big', views.kab_point_big, name='kab_big'),
	path('data/rumahsakit/', views.rumahsakit, name='rumahsakit'),
 ]
