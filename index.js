import { GOOGLE_MAP_APIKEY } from "./config.js";

let map;

// Load Google Map API script with API Key.
(function (d, script) {
  script = d.createElement("script");
  script.type = "text/javascript";
  script.src = `https://maps.googleapis.com/maps/api/js?key=${GOOGLE_MAP_APIKEY}&v=beta&callback=initMap`;
  d.getElementsByTagName("head")[0].appendChild(script);
})(document);

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    zoom: 2,
    center: { lat: -33.865427, lng: 151.196123 },
    mapId: "3585812c6f0ff87a", // A map ID using a style with one or more feature layers enabled.
  });

  let metadata = {};
  var xmlhttp = new XMLHttpRequest();
  xmlhttp.onreadystatechange = function () {
    if (xmlhttp.status == 200 && xmlhttp.readyState == 4) {
      let rows = xmlhttp.responseText.split("\n");

      // Set meatadata
      metadata.total = rows.length;

      rows.forEach((row, idx) => {
        if (idx != 0) {
          let locs = row.split("|");

          if (locs.length < 2) return;

          // Conent string in Infowindow
          let contentString = `
          <div>
            <div style="font-weight:bold;"}>${locs[0]}</div><br>

            <div>ip : ${locs[1]}</div>
            <div>country : ${locs[2]}</div>
            <div>city : ${locs[3]}</div>
            <div>org : ${locs[4]}</div>
            
          </div>
          `;
          const infowindow = new google.maps.InfoWindow({
            content: contentString,
          });

          const marker = new google.maps.Marker({
            position: { lat: parseFloat(locs[5]), lng: parseFloat(locs[6]) },
            map,
            title: locs[0],
          });

          marker.addListener("mouseover", () => {
            infowindow.open({
              anchor: marker,
              map,
              shouldFocus: false,
            });
          });

          marker.addListener("mouseout", () => {
            infowindow.close();
          });
        }
      });
    }
  };
  xmlhttp.open("GET", "./locations.dat", true);
  xmlhttp.send();
}

window.initMap = initMap;
