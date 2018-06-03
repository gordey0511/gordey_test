L.mapbox.accessToken = 'pk.eyJ1IjoiaGFubGV5d29vZCIsImEiOiJZcVlldnlRIn0.BHYD98R8UQQoUBLsNd8ksg';
  var geojson = [
      {
        "type": "FeatureCollection",
        "features": [
          {
            "type": "Feature",
            "geometry": {
              "type": "Point",
              "coordinates": [
                27.517552,
                53.9263428
              ]
            },
            "properties": {
              "image": "",
              "websiteText": "вернуться на сайт",
              "url":"",
              "property": "Dream club",
              "firm": "Минск",
              "country": "USA",
              "crossStreet": "Проспект Победителей 65<br>Торговый комплекс «ЗАМОК»",
              "ran": "2",
              "ora": "97",
              "state": "South Carolina",
               "icon": "http://images.hw.net/Brightspot/Architect/Interactives/2015/15May/Atlanta_Locator_Map/store-locator-final/markerblue.png"
            }
          },



        ]
      }
  ];
  var map = L.mapbox.map('mfe-top100', 'hanleywood.kv1s8aor')
  .setView([39.868196,-98.802562], 4);

//      var map = L.mapbox.map('map', 'examples.map-i80bb8p3')
//  .setView([33.7677129, -84.4006039], 13);

  map.scrollWheelZoom.disable();

  var listings = document.getElementById('listings');
  var locations = L.mapbox.featureLayer().addTo(map);

  locations.setGeoJSON(geojson);

  function setActive(el) {
    var siblings = listings.getElementsByTagName('div');
    for (var i = 0; i < siblings.length; i++) {
      siblings[i].className = siblings[i].className
      .replace(/active/, '').replace(/\s\s*$/, '');
    }

    el.className += ' active';
  }

  locations.eachLayer(function(locale) {

    // Shorten locale.feature.properties to just `prop` so we're not
    // writing this long form over and over again.
    var prop = locale.feature.properties;

    // Each marker on the map.
    var popup ='<img src="' + prop.image + '" />' +'<h3>'+ prop.property + '</h3>';

    var listing = listings.appendChild(document.createElement('div'));
    listing.className = 'item';

    var link = listing.appendChild(document.createElement('a'));
    link.href = '#';
    link.className = 'title';

    link.innerHTML = prop.property;
    if (prop.crossStreet) {
      link.innerHTML += '</br><small class="quiet">' + prop.crossStreet + '</small>';
      popup += '<small class="quiet boxtop">' + prop.crossStreet + '</small>' + '<br>' + '<small class="box">Время работы: ' + prop.ora + '</small>' + '<br>' + '<h4 class="box">' + prop.firm + '</h4>'+ '<br>'+'<a target="_blank" class="url" href="' + prop.url + '">' + prop.websiteText + '</a>';
    }

    var details = listing.appendChild(document.createElement('div'));
    details.innerHTML = prop.firm;
    if (prop.websiteURL) {
      details.innerHTML;
    }

    link.onclick = function() {
      setActive(listing);

      // When a menu item is clicked, animate the map to center
      // its associated locale and open its popup.
      map.setView(locale.getLatLng(), 16);
      locale.openPopup();
      return false;
    };

    // Marker interaction
    locale.on('click', function(e) {
      // 1. center the map on the selected marker.
      map.panTo(locale.getLatLng());

      // 2. Set active the markers associated listing.
      setActive(listing);
    });

    popup += '</div>';
    locale.bindPopup(popup);

    locale.setIcon(L.icon({
    iconUrl: prop.icon,
    iconSize: [50, 50],
    iconAnchor: [28, 28],
    popupAnchor: [0, -34]
    }));
});