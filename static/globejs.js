var world;
const colorScale = d3.scaleSequentialSqrt(d3.interpolateViridis);
// Other color scales: d3.interpolateViridis, d3.interpolateYlOrRd, d3.interpolateRdBu
// GDP per capita (avoiding countries with small population)

const getVal = feat => feat.properties.GDP_MD_EST / Math.max(1e5, feat.properties.POP_EST);
fetch('https://raw.githubusercontent.com/vasturiano/globe.gl/master/example/datasets/ne_110m_admin_0_countries.geojson')
  .then(res => res.json())
  .then(countries => {
    const maxVal = Math.max(...countries.features.map(getVal));
    colorScale.domain([0, maxVal]);

    world = Globe()
      .globeImageUrl('https://cdn.jsdelivr.net/npm/three-globe/example/img/earth-night.jpg')
      .polygonsData(countries.features)
      .polygonAltitude(0.05)
      .polygonCapColor(feat => colorScale(getVal(feat)))
      .polygonSideColor(() => 'rgba(0, 100, 0, 0.15)')
      .polygonStrokeColor(() => '#111')
      .polygonLabel(({ properties: d }) => `
        <b>${d.ADMIN} (${d.ISO_A2}):</b> <br />
      `)
      .onPolygonHover(hoveredPolygon => {
        if (!world.clickedPolygon || world.clickedPolygon !== hoveredPolygon) {
          world.polygonCapColor(d => d === hoveredPolygon ? 'steelblue' : colorScale(getVal(d)));
        }
      })
      .onPolygonClick(clickedPolygon => {
        world.clickedPolygon = clickedPolygon;
        const countryName = clickedPolygon.properties.ADMIN;

        document.getElementById('modal-text').innerHTML = `You clicked on: ${countryName}` ;

        var modal = document.getElementById("myModal");
        modal.style.display = "block";
      });

    var modal = document.getElementById("myModal");
    var span = document.getElementsByClassName("close")[0];

    span.onclick = function() {
      modal.style.display = "none";
    };

    window.onclick = function(event) {
      if (event.target == modal) {
        modal.style.display = "none";
      }
    };

    world.polygonsTransitionDuration(300)(document.getElementById('globeViz'));

    document.addEventListener('DOMContentLoaded', (event) => {
      const submitButton = document.getElementById('submitButton');
      submitButton.addEventListener('click', function(event) {
        // Prevent the default form submission if your button is inside a form
        event.preventDefault();
        
        // Call your function with the required parameters
        fetchHistorySummary('Japan', 1936);
      });
    });
    
    function fetchHistorySummary(country, startYear) {
      const url = `/get_history_summary?country=${encodeURIComponent(country)}&start_year=${encodeURIComponent(startYear)}`;
      fetch(url)
        .then(response => response.json())
        .then(data => {
          const summary = data.summary;
          // Find the div and populate it with fetched content
          const contentDiv = document.getElementById('fetchedContent');
          contentDiv.innerHTML = `<p>${summary}</p>`;
          
          // Now that the content is ready, display the div as a popup
          contentDiv.style.display = 'block';
        })
        .catch(error => {
          console.error('Error fetching history summary:', error);
          
          // In case of an error, inform the user
          const contentDiv = document.getElementById('fetchedContent');
          contentDiv.innerHTML = `<p>Error fetching history summary. Please try again later.</p>`;
          
          // Display the div with the error message
          contentDiv.style.display = 'block';
        });
    }
    
  });
