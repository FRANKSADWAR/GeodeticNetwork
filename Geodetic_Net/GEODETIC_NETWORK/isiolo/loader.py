from django.contrib.gis.utils import LayerMapping
from isiolo.models import County, Towns, Isiolo_Towns, Geodetic_Controls
import os


### COUNTY MAPPING AND SAVING TO DATABASE
county_mapping = {
    'objectid': 'OBJECTID',
    'area': 'AREA',
    'perimeter': 'PERIMETER',
    'county3_field': 'COUNTY3_',
    'county3_id': 'COUNTY3_ID',
    'county': 'COUNTY',
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'geom': 'MULTIPOLYGON',
}
county_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data','County.shp'),)
def county_run(verbose=True):
    lm = LayerMapping(County,county_shp,county_mapping, transform=False)
    lm.save(strict=True,verbose=verbose)

## TOWNS MAPPING AND SAVING TO DATABASE
towns_mapping = {
    'area': 'AREA',
    'perimeter': 'PERIMETER',
    'town_name': 'TOWN_NAME',
    'town_id': 'TOWN_ID',
    'town_type': 'TOWN_TYPE',
    'geom': 'MULTIPOINT',
}
towns_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data','isiolo_towns.shp'),)
def towns_run(verbose=True):
    lm = LayerMapping(Towns,towns_shp,towns_mapping,transform=False)
    lm.save(strict=True, verbose=verbose)


isiolo_towns_mapping = {
    'id': 'id',
    'area': 'area',
    'perimeter': 'perimeter',
    'town_name': 'town_name',
    'town_id': 'town_id',
    'town_type': 'town_type',
    'geom': 'MULTIPOINT',
}
isiolo_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data','towns.shp'),)
def town_runs(verbose=True):
    lm = LayerMapping(Isiolo_Towns,isiolo_shp,isiolo_towns_mapping,transform=False)
    lm.save(strict=True, verbose=verbose)    



## Controls mapping for final stations
# Auto-generated `LayerMapping` dictionary for Geodetic_Controls model
geodetic_controls_mapping = {
    'objectid': 'OBJECTID',
    'name': 'NAME',
    'lat': 'LAT',
    'long': 'LONG',
    'e': 'E',
    'n': 'N',
    'order_field': 'ORDER_',
    'status': 'Status',
    'geom': 'POINT',
}    
stations_shp = os.path.abspath(os.path.join(os.path.dirname(__file__),'data','Final_geodetic_control.shp'),)
def map_controls(verbose=True):
    lm = LayerMapping(Geodetic_Controls,stations_shp,geodetic_controls_mapping)
    lm.save(strict=True, verbose=verbose)