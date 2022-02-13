from django.contrib import admin
from django.contrib.gis.admin import OSMGeoAdmin
from leaflet.admin import LeafletGeoAdmin
from isiolo.models import Isiolo_Towns, County, ReportIncidence, Geodetic_Controls



@admin.register(Isiolo_Towns)
class TownsAdmin(OSMGeoAdmin):
    list_display = ('id','town_name','town_type','town_id')
    list_filter =   ('id','town_name','town_type','town_id')
    search_fields = ('id','town_name','town_type','town_id')


@admin.register(County)
class CountyAdmin(OSMGeoAdmin):
    list_display = ('objectid','county')
    list_filter = ('objectid','county')
    search_fields = ('objectid','county')

@admin.register(ReportIncidence)
class ReportIncidencesAdmin(OSMGeoAdmin):
    list_display = ('station_name','status','username','coordinates')    
    list_filter = ('station_name','status','username','coordinates') 
    search_fields = ('station_name','status','username','coordinates') 

@admin.register(Geodetic_Controls)
class GeodeticControlsAdmin(LeafletGeoAdmin):
    list_display = ('name','order_field','status','e','n')
    list_filter = ('name','order_field','status','e','n')
    search_fields = ('name','order_field','status','e','n')
        