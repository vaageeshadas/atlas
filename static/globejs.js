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

        document.getElementById('modal-text').innerHTML = `You clicked on: ${countryName}`;

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
  });
