/**
 * THIS IS THE MAIN MAP SCRIPT FOR THE MAIN MAPPING APPLICATION. IT IS SUBJECT TO CHANGE 
 * AND MODIFICATION.
 */


$.ajax({
  beforeSend: function (xhr) {
    if (xhr.overrideMimeType()) {
      xhr.overrideMimeType("application/json");
    }
  }
});

var baseLayers, groupedLayers, mapLink, map, osm, Esri_WorldImagery, cartoVoyager;
var cartoPositron;

var townsData, streetNetwork, IsioloBoundary;


var positronUrl = 'https://{s}.basemaps.cartocdn.com/rastertiles/light_all/{z}/{x}/{y}.png';
var cartoVoyagerUrl = 'https://{s}.basemaps.cartocdn.com/rastertiles/voyager_labels_under/{z}/{x}/{y}.png';

mapLink = '&copy;<a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>';
map = L.map('maparea').setView([0.646107, 38.201213], 8);

osm = L.tileLayer('http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: mapLink,
  maxZoom: 32,
}).addTo(map);


cartoPositron = L.tileLayer(positronUrl, {
  attribution: '<a href="https://carto.com/">Carto</a>',
  maxZoom: 30
}).addTo(map);

cartoVoyager = L.tileLayer(cartoVoyagerUrl, {
  attribution: '<a href="https://carto.com/">Carto Voyager</a>',
  maxZoom: 30,
});

Esri_WorldImagery = L.tileLayer('https://server.arcgisonline.com/ArcGIS/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}', {
  attribution: 'Tiles &copy; Esri &mdash; Source: Esri, i-cubed, USDA, USGS, AEX,GeoEye,UPR-EGP',
  maxZoom: 30,
}).addTo(map);

/// GEODATA URLS
var isioloUrl = '/isiolo/';
var controlsUrl = '/geodetic_controls/';
var townsUrl = '/towns/';
var stationControls;



// ADDING TOWNS DAYA WIH Ajax requests -------->>>>

townsData = L.geoJSON(null, {
  style: function (feature) {
    return {
      fillOpacity: 1.0,
    };
  },
  pointToLayer: function (feature, latlng) {
    return L.marker(latlng, {
      icon: L.icon({
        iconUrl: '/static/images/town.png',
        iconSize: [25, 20],
        iconAnchor: [2, 3],
        popupAnchor: [0, 1]
      }),
      riseOnHover: true,
    });
  },
  onEachFeature: function (feature, marker) {
    marker.bindPopup('<h3 style="font-weight:normal;font-size:1.0em;text-transform:uppercase;letter-spacing:0.1em;color:#222f3e;margin-bottom:0">' +
      feature.properties.town_name.toString() + '</h3>' + '<br/>' + '<span style="font-size:0.8em;position:relative;top:-1.5em;letter-spacing:0.1em">' + '</span>');
  }
}).addTo(map);

$.ajax({
  beforeSend: function (xhr) {
    if (xhr.overrideMimeType()) {
      xhr.overrideMimeType("application/json");
    }
  },
  url: townsUrl,
  async: true,
  success: function (data) {
    townsData.addData(data);
    map.addLayer(townsData);
  }
});



/// --------- Controls Data with AJAX

stationControls = L.geoJSON(null, {
  style: function (feature) {
    return {
      fillOpacity: 0.8,
    };
  },
  pointToLayer: function (feature, latlng) {
    return L.marker(latlng, {
      icon: L.icon({
        iconUrl: '/static/images/triangle.png',
        iconSize: [20, 20],
        iconAnchor: [2, 3],
        popupAnchor: [0, 1]
      }),
      riseOnHover: true,
    });
  },
  onEachFeature: function (feature, marker) {
    marker.bindPopup('<h3 style="font-weight:normal;font-size:1.0em;text-transform:uppercase;letter-spacing:0.1em;color:#222f3e;margin-bottom:0">' + 'Name:' +
      feature.properties.name.toString() + '</h3>' + '<br/>' + '<span style="font-size:0.8em;position:relative;top:-1.5em;letter-spacing:0.1em">' + 'Order:' +
      feature.properties.order_field.toString() + '</span>' + '<br/>' + '<span style="font-size:0.8em; position:relative;top:-1.5em; letter-spacing:0.1em">' + 'Status:' +
      feature.properties.status.toString() + '</span>' + '<br/>' + '<span style="font-size:0.8em;position:relative;top:-1.5em;letter-spacing:0.1em">' + 'Northings:' +
      feature.properties.n.toString() + '</span>' + '<br/>' + '<span style="font-size:0.8em;position:relative;top:-1.5em;letter-spacing:0.1em">' + 'Eastings:' +
      feature.properties.e.toString() + '</span>');
  }
}).addTo(map);

$.ajax({
  beforeSend: function (xhr) {
    if (xhr.overrideMimeType()) {
      xhr.overrideMimeType("application/json");
    }
  },
  url: controlsUrl,
  async: true,
  success: function (data) {
    stationControls.addData(data);
    map.addLayer(stationControls);
  }
});

//--------- >>>>>>>>>> ISIOLO COUNTY layer with Ajax request

IsioloBoundary = L.geoJSON(null, {
  style: function (feature) {
    return {
      color: 'green',
      weight: 4,
      fillOpacity: 0
    };
  }
});

$.ajax({
  beforeSend: function (xhr) {
    if (xhr.overrideMimeType()) {
      xhr.overrideMimeType("application/json");   // Override the MimeType and set it to json
    }
  },
  url: isioloUrl,
  async: true,
  success: function (data) {
    IsioloBoundary.addData(data);
    map.addLayer(IsioloBoundary);
  }
});

//ADD THE LAYERS TO THE MAP

IsioloBoundary.addTo(map);
townsData.addTo(map);


// GROUP THE LAYERS AND ADD TO MAP
baseLayers = {
  "Esri World Imagery": Esri_WorldImagery,
  "Carto Positron": cartoPositron,
  "OSM": osm,
}

groupedLayers = {
  "Layers": {
    "Towns": townsData,
    "County Boundary": IsioloBoundary,
    "Geodetic Control": stationControls,
  }
}

L.control.groupedLayers(baseLayers, groupedLayers, { collapsed: true }).addTo(map);

/**
 * -------ADDING PLUGINS-------- 
 */

//-------MOUSE POSITION
L.control.mousePosition({
  position: 'bottomright',
}).addTo(map);

//------DRAWING TOOLS
var drawnItems = new L.FeatureGroup().addTo(map);
map.addLayer(drawnItems);
var drawControl = new L.Control.Draw({
  draw: {
    polygon: {
      shapeOptions: {
        color: 'green'
      },
      allowIntersection: false,
      drawError: {
        color: 'orange',
        timeout: 100
      },
      showArea: true,
      metric: true,
      repeatMode: true
    },
    polyline: {
      shapeOptions: {
        color: 'blue'
      },
      allowIntersection: false
    },
    rect: {
      shapeOptions: {
        color: 'blue'
      },
    },
  },
  edit: {
    featureGroup: drawnItems
  }
});
map.addControl(drawControl);
map.on('draw:created', function (e) {
  var type = e.layerType,
    layer = e.layer;
  drawnItems.addLayer(layer);
});

//-----SEARCH  GEOJSON OBJECTS
var searchControl = new L.Control.Search({
  layer: stationControls,
  propertyName: 'name',
  marker: false,
  moveToLocation: function (latlng, title, map) {
    var zoom = map.getBoundsZoom(latlng.layer.getBounds());
    map.setZoomAround(latlng, zoom);
  }
});

searchControl.on('search:locationfound', function (e) {
  //e.layer.setStyle({fillColor:'#3f0',color:'#0f0'});
  if (e.layer._popup)
    e.layer.openPopup();
}).on('search:collapsed', function (e) {
  stationControls.eachLayer(function (layer) {
    stationControls.resetStyle(layer);
  });
});
map.addControl(searchControl);

/**
 * 
 LEAFLET ROUTING MACHINE PLUGINS -------- >>>>>>>
 */


var routingcontrol = L.Routing.control({
  waypoints: [
    L.latLng(0.89605, 38.6481),
    L.latLng(0.518025236, 38.50727824)
  ],
  geocoder: L.Control.Geocoder.nominatim(),
  routeWhileDragging: true,
  reverseWaypoints: true,
  showAlternatives: true,
  altLineOptions: {
    styles: [
      { color: 'black', opacity: 0.15, weight: 9 },
      { color: 'green', opacity: 0.8, weight: 6 },
      { color: 'blue', opacity: 0.5, weight: 2 }
    ]
  }
}).addTo(map);
L.Routing.errorControl(routingcontrol).addTo(map);