from django.shortcuts import render
from django.contrib.gis.geos import GEOSGeometry, MultiPolygon, MultiPoint
from .models import Pendidikan, Ibadah, Kabupaten, Kab_Point, Rumahsakit
from django.http import HttpResponse
from django.core.serializers import serialize

# Create your views here.

def maps(request):
	return render(request, 'papua/maps.html')

#RELIGION
def religion(request):
	data_ibadah = serialize('geojson', Ibadah.objects.all())

	return HttpResponse(data_ibadah, content_type='json')
#Pendidikan

def pendidikan(request):
	data_pendidikan = serialize('geojson', Pendidikan.objects.all())

	return HttpResponse(data_pendidikan, content_type='json')

#Kabupaten
def kabupaten(request):
	data_kabupaten = serialize('geojson', Kabupaten.objects.all())

	return HttpResponse(data_kabupaten, content_type='json')

#Rumahsakit
def rumahsakit(request):
	data_rumahsakit = serialize('geojson', Rumahsakit.objects.all())

	return HttpResponse(data_rumahsakit, content_type='json')

#Kabupaten point
def kab_point_big(request):
	kab_big = serialize('geojson', Kab_Point.objects.filter(kode_ibk='1'))

	return HttpResponse(kab_big, content_type='json')
