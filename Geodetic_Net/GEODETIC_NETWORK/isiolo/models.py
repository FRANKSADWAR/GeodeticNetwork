from django.db import models
from django.contrib.gis.db import models as gis_models
from django.contrib.auth.models import User
from django.utils import timezone
from django.conf import settings

STATUS = (
    ('Destroyed','Destroyed'),
    ('Missing','Missing'),
    ('Existing','Existing'),
    ('Re-Established','Re-Established'),
    ('New control','New control'),
)


class County(models.Model):
    objectid = models.IntegerField()
    area = models.FloatField()
    perimeter = models.FloatField()
    county3_field = models.FloatField()
    county3_id = models.FloatField()
    county = models.CharField(max_length=20)
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    geom = gis_models.MultiPolygonField(srid=4326)

    class Meta:
        verbose_name_plural ='Isiolo'

class Towns(models.Model):
    area = models.FloatField()
    perimeter = models.FloatField()
    town_name = models.CharField(max_length=254)
    town_id = models.FloatField()
    town_type = models.CharField(max_length=254)
    geom = gis_models.MultiPointField(srid=4326)
    class Meta:
        verbose_name_plural = 'Towns'

class Isiolo_Towns(models.Model):
    id = models.BigIntegerField(primary_key=True)
    area = models.FloatField()
    perimeter = models.FloatField()
    town_name = models.CharField(max_length=254)
    town_id = models.FloatField()
    town_type = models.CharField(max_length=254)
    geom = gis_models.MultiPointField(srid=4326)
    class Meta:
        verbose_name_plural = 'Isiolo Towns'


class Geodetic_Controls(models.Model):
    objectid = models.BigIntegerField()
    name = models.CharField(max_length=254)
    lat = models.FloatField()
    long = models.FloatField()
    e = models.FloatField()
    n = models.FloatField()
    order_field = models.CharField(max_length=254)
    status = models.CharField(max_length=254)
    geom = gis_models.PointField(srid=4326)

    class Meta:
        verbose_name_plural  =' Geodetic Controls Isiolo'



###---------- USER MODEL ---------- ###

class StaffProfiles(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    telnumber = models.CharField(max_length=10,verbose_name='Phone Number')
    address = models.CharField(max_length=200,verbose_name='Address')
    photo = models.ImageField(verbose_name='Profile Picture')
    def __str__(self):
        return 'User is {}'.format(self.user.username)


class ReportIncidence(models.Model):
    issue_id = models.AutoField(primary_key=True)
    station_name = models.CharField(max_length=50,verbose_name='Station name',null=False)
    status = models.CharField(null=False,choices=STATUS,max_length=20)
    username = models.CharField(max_length=50,null=False)
    organization = models.CharField(max_length=50)
    phone_no = models.CharField(max_length=15,null=False)
    email = models.EmailField(max_length=40,null=False)
    coordinates = gis_models.PointField(srid=4326)

    class Meta:
        verbose_name_plural = 'Report Incidences'
    def __str__(self):
        return '[Station Name: %s, issue_id: %s]' % (self.station_name, self.issue_id) 


