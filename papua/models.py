from django.db import models
from django.contrib.gis.db import models as geomodels
# Create your models here.

class Kabupaten(models.Model):
    kode = models.IntegerField()
    kab_id = models.FloatField(blank=True, null=True)
    kabupaten = models.CharField(max_length=25)
    pddk_2017 = models.FloatField(blank=True, null=True)
    luas_km = models.FloatField(blank=True, null=True)
    luas_src = models.CharField(max_length=30)
    geom = geomodels.MultiPolygonField(srid=4326)

    def __str__(self):
        return self.kabupaten

class Kab_Point(models.Model):
    kab = models.CharField(max_length=25)
    pddk_2017 = models.IntegerField()
    geom = geomodels.MultiPointField(srid=4326)
    kode_ibk = models.IntegerField()

class Pendidikan(models.Model):
    namobj = models.CharField(max_length=50, null=True)
    fggpdk = models.IntegerField()
    remark = models.CharField(max_length=50)
    geom = geomodels.MultiPointField(srid=4326)

    def __str__(self):
        return self.remark

class Ibadah(models.Model):
    namobj = models.CharField(max_length=50, null=True)
    fgsibd = models.IntegerField()
    remark = models.CharField(max_length=50)
    geom = geomodels.MultiPointField(srid=4326)

    def __str__(self):
        return self.remark

class Rumahsakit(models.Model):
    namobj = models.CharField(max_length=50, null=True)
    remark = models.CharField(max_length=50)
    geom = geomodels.MultiPointField(srid=4326)
