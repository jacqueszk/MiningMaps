import folium
from jinja2 import Template

mines = [
    {
        "name": "Cananea Copper Mine",
        "location": "Sonora",
        "coordinates": [30.967, -110.300],
        "company": "Grupo México",
        "mining_method": "Open-pit"
    },
    {
        "name": "Fresnillo Mine",
        "location": "Zacatecas",
        "coordinates": [23.176, -102.880],
        "company": "Fresnillo plc",
        "mining_method": "Underground"
    },
    {
        "name": "Peñasquito Mine",
        "location": "Zacatecas",
        "coordinates": [23.367, -103.885],
        "company": "Newmont Corporation",
        "mining_method": "Open-pit"
    },
    {
        "name": "San Dimas Mine",
        "location": "Durango",
        "coordinates": [24.336, -105.185],
        "company": "First Majestic Silver",
        "mining_method": "Underground"
    },
    {
        "name": "Los Filos Mine",
        "location": "Guerrero",
        "coordinates": [18.195, -99.781],
        "company": "Equinox Gold",
        "mining_method": "Open-pit"
    },
    {
        "name": "Pinos Altos Mine",
        "location": "Chihuahua",
        "coordinates": [27.431, -108.211],
        "company": "Agnico Eagle Mines",
        "mining_method": "Underground"
    },
    {
        "name": "Palmarejo Mine",
        "location": "Chihuahua",
        "coordinates": [28.381, -107.458],
        "company": "Coeur Mining",
        "mining_method": "Underground"
    },
    {
        "name": "La Herradura Mine",
        "location": "Sonora",
        "coordinates": [29.383, -110.515],
        "company": "Fresnillo plc",
        "mining_method": "Open-pit"
    },
    {
        "name": "El Chanate Mine",
        "location": "Sonora",
        "coordinates": [27.211, -109.956],
        "company": "AuRico Gold",
        "mining_method": "Open-pit"
    },

    {
        "name": "La Colorada Mine",
        "location": "Sonora",
        "coordinates": [28.789, -110.987],
        "company": "Pan American Silver",
        "mining_method": "Underground"
    },
    {
        "name": "San Francisco Mine",
        "location": "Sonora",
        "coordinates": [31.033, -112.214],
        "company": "Alio Gold",
        "mining_method": "Open-pit"
    },
    {
        "name": "Mulatos Mine",
        "location": "Sonora",
        "coordinates": [29.072, -108.941],
        "company": "Alamos Gold",
        "mining_method": "Open-pit"
    },
    {
        "name": "Ocampo Mine",
        "location": "Chihuahua",
        "coordinates": [28.395, -107.078],
        "company": "Argonaut Gold",
        "mining_method": "Open-pit"
    },
    {
        "name": "Saucito Mine",
        "location": "Zacatecas",
        "coordinates": [23.375, -102.703],
        "company": "Fresnillo plc",
        "mining_method": "Underground"
    },
    {
        "name": "Santa Elena Mine",
        "location": "Sonora",
        "coordinates": [31.720, -109.257],
        "company": "First Majestic Silver",
        "mining_method": "Open-pit"
    },
    {
        "name": "La Ciénega Mine",
        "location": "Durango",
        "coordinates": [24.071, -104.539],
        "company": "Fresnillo plc",
        "mining_method": "Underground"
    },
    {
        "name": "Guanaceví Mine",
        "location": "Durango",
        "coordinates": [24.881, -105.323],
        "company": "Endeavour Silver",
        "mining_method": "Underground"
    },
    {
        "name": "Parral Mine",
        "location": "Chihuahua",
        "coordinates": [26.930, -105.655],
        "company": "Southern Copper",
        "mining_method": "Underground"
    },

    {
        "name": "La Caridad Mine",
        "location": "Sonora",
        "coordinates": [28.383, -109.757],
        "company": "Grupo México",
        "mining_method": "Open-pit"
    },
    {
        "name": "Del Toro Mine",
        "location": "Zacatecas",
        "coordinates": [23.634, -103.100],
        "company": "First Majestic Silver",
        "mining_method": "Underground"
    },
    {
        "name": "Cusi Mine",
        "location": "Chihuahua",
        "coordinates": [26.424, -107.292],
        "company": "Sierra Metals",
        "mining_method": "Underground"
    },

    {
        "name": "Cerro de Mercado Mine",
        "location": "Durango",
        "coordinates": [24.029, -104.664],
        "company": "Grupo Peñoles",
        "mining_method": "Open-pit"
    },
    {
        "name": "La Encantada Mine",
        "location": "Coahuila",
        "coordinates": [27.778, -101.587],
        "company": "First Majestic Silver",
        "mining_method": "Underground"
    },
     {
        "name": "La Parrilla Mine",
        "location": "Durango",
        "coordinates": [24.341, -104.910],
        "company": "First Majestic Silver",
        "mining_method": "Underground"
    },
    {
        "name": "La Guitarra Mine",
        "location": "Mexico",
        "coordinates": [19.899, -100.030],
        "company": "Sierra Madre Gold & Silver",
        "mining_method": "Underground"
    },
    {
        "name": "Minaurum Gold",
        "location": "Oaxaca",
        "coordinates": [16.958, -96.538],
        "company": "Minaurum Gold",
        "mining_method": "Exploration"
    },
    {
        "name": "Camino Rojo Mine",
        "location": "Zacatecas",
        "coordinates": [23.307, -103.610],
        "company": "Orla Mining",
        "mining_method": "Open-pit"
    },
    {
        "name": "Los Gatos Mine",
        "location": "Chihuahua",
        "coordinates": [28.556, -107.852],
        "company": "Sunset Gold",
        "mining_method": "Underground"
    },
    {
        "name": "Pinos Mine",
        "location": "Zacatecas",
        "coordinates": [22.307, -101.523],
        "company": "Alamos Gold",
        "mining_method": "Underground"
    },
    {
        "name": "Tahuehueto Mine",
        "location": "Durango",
        "coordinates": [25.023, -104.255],
        "company": "Telson Mining",
        "mining_method": "Underground"
    },
    {
        "name": "Santana Mine",
        "location": "Sonora",
        "coordinates": [30.775, -111.708],
        "company": "Minera Alamos",
        "mining_method": "Open-pit"
    },
    {
        "name": "La Luz Mine",
        "location": "San Luis Potosí",
        "coordinates": [22.041, -101.638],
        "company": "Coeur Mining",
        "mining_method": "Underground"
    },
    {
        "name": "Ixtaca Mine",
        "location": "Puebla",
        "coordinates": [19.276, -98.517],
        "company": "Almaden Minerals",
        "mining_method": "Open-pit"
    },
    {
        "name": "San Jose Mine",
        "location": "Oaxaca",
        "coordinates": [16.502, -96.226],
        "company": "Fortuna Silver Mines",
        "mining_method": "Underground"
    },
    {
        "name": "Tayoltita Mine",
        "location": "Durango",
        "coordinates": [24.724, -104.798],
        "company": "Fresnillo plc",
        "mining_method": "Underground"
    },
    {
        "name": "San Felipe Mine",
        "location": "Baja California",
        "coordinates": [30.484, -115.930],
        "company": "Timberline Resources",
        "mining_method": "Open-pit"
    },
    {
        "name": "Mazapil Mine",
        "location": "Zacatecas",
        "coordinates": [24.530, -101.648],
        "company": "Frisco",
        "mining_method": "Open-pit"
    },
    {
        "name": "Cerro San Pedro Mine",
        "location": "San Luis Potosí",
        "coordinates": [22.196, -100.984],
        "company": "New Gold",
        "mining_method": "Open-pit"
    },
    {
        "name": "La Negra Mine",
        "location": "Querétaro",
        "coordinates": [20.752, -99.900],
        "company": "Arian Silver",
        "mining_method": "Underground"
    },
    {
        "name": "La Luz-Sierra Mojada Mine",
        "location": "Coahuila",
        "coordinates": [27.841, -101.530],
        "company": "Sierra Metals",
        "mining_method": "Underground"
    },
    {
        "name": "Los Juarez Mine",
        "location": "Chihuahua",
        "coordinates": [29.495, -105.899],
        "company": "U.S. Antimony",
        "mining_method": "Open-pit"
    },
    {
        "name": "Magistral Mine",
        "location": "Sinaloa",
        "coordinates": [25.383, -107.483],
        "company": "Canarc Resource",
        "mining_method": "Open-pit"
    },

    {
        "name": "La Choya Mine",
        "location": "Sonora",
        "coordinates": [28.267, -111.128],
        "company": "Alamos Gold",
        "mining_method": "Open-pit"
    },
    {
        "name": "La Trinidad Mine",
        "location": "Sinaloa",
        "coordinates": [24.335, -106.200],
        "company": "Marlin Gold Mining",
        "mining_method": "Open-pit"
    },
    {
        "name": "El Castillo Mine",
        "location": "Durango",
        "coordinates": [24.520, -104.926],
        "company": "Argonaut Gold",
        "mining_method": "Open-pit"
    },

    {
        "name": "Santa Gertrudis Mine",
        "location": "Sonora",
        "coordinates": [30.789, -111.472],
        "company": "GoGold Resources",
        "mining_method": "Open-pit"
    },
    {
        "name": "El Compas Mine",
        "location": "Zacatecas",
        "coordinates": [22.660, -102.615],
        "company": "Grupo México",
        "mining_method": "Underground"
    },
    {
        "name": "El Gallo Mine",
        "location": "Sinaloa",
        "coordinates": [25.618, -108.757],
        "company": "McEwen Mining",
        "mining_method": "Open-pit"
    },

    {
      "name": "Bolanitos Mine",
      "location": "Guanajuato",
      "coordinates": [21.122, -100.925],
      "company": "Endeavour Silver",
      "mining_method": "Underground"
    },
    
    {
      "name": "Terronera Mine",
      "location": "Jalisco",
      "coordinates": [20.672, -105.216],
      "company": "Endeavour Silver",
      "mining_method": "Underground"
    },
      {
    "name": "Naica Mine",
    "location": "Chihuahua",
    "coordinates": [27.870, -105.495],
    "company": "Industrias Peñoles",
    "mining_method": "Underground"
  },
  {
    "name": "El Cubo Mine",
    "location": "Guanajuato",
    "coordinates": [21.014, -101.250],
    "company": "Endeavour Silver Corp",
    "mining_method": "Underground"
  },
  {
    "name": "Mina Proaño",
    "location": "Hidalgo",
    "coordinates": [20.174, -99.109],
    "company": "Grupo México",
    "mining_method": "Underground"
  },
  {
    "name": "Milpillas Mine",
    "location": "Sonora",
    "coordinates": [30.938, -110.571],
    "company": "Industrias Peñoles",
    "mining_method": "Underground"
  },
  {
"name": "Herradura Mine",
"location": "Sonora",
"coordinates": [27.426, -110.015],
"company": "Fresnillo plc",
"mining_method": "Open-pit"
},
{
"name": "Noche Buena Mine",
"location": "Sonora",
"coordinates": [29.227, -110.080],
"company": "Fresnillo plc",
"mining_method": "Open-pit"
},
{
"name": "San Julián Mine",
"location": "Chihuahua",
"coordinates": [26.570, -105.460],
"company": "Fresnillo plc",
"mining_method": "Open-pit"
},
{
"name": "Juanicipio Mine",
"location": "Zacatecas",
"coordinates": [22.745, -102.569],
"company": "Fresnillo plc",
"mining_method": "Underground"
},
{
"name": "Buenavista del Cobre Mine",
"location": "Sonora",
"coordinates": [25.894, -110.927],
"company": "Grupo México",
"mining_method": "Open-pit"
},
{
"name": "Penasquito Mine",
"location": "Zacatecas",
"coordinates": [23.635, -103.879],
"company": "Newmont Goldcorp",
"mining_method": "Open-pit"
},
{
"name": "El Coronel Mine",
"location": "Zacatecas",
"coordinates": [23.339, -102.803],
"company": "Frisco",
"mining_method": "Open-pit"
},

{
"name": "Asientos Mine",
"location": "Aguascalientes",
"coordinates": [22.237, -102.079],
"company": "Frisco",
"mining_method": "Underground"
},
{
"name": "Ocampo Mine",
"location": "Chihuahua",
"coordinates": [28.483, -107.133],
"company": "Endeavour Silver Corp",
"mining_method": "Underground"
},

{
"name": "Concheno Mine",
"location": "Guanajuato",
"coordinates": [21.029, -101.268],
"company": "Frisco",
"mining_method": "Underground"
},

{
"name": "San Francisco del Oro Mine",
"location": "Chihuahua",
"coordinates": [26.121, -105.379],
"company": "Frisco",
"mining_method": "Underground"
},

{
"name": "Tayahua Mine",
"location": "Zacatecas",
"coordinates": [22.656, -101.759],
"company": "Frisco",
"mining_method": "Underground"
},

{
"name": "El Coronel Mine",
"location": "Zacatecas",
"coordinates": [24.337, -101.463],
"company": "Frisco",
"mining_method": "Underground"
},
{
"name": "Mina María",
"location": "Sonora",
"coordinates": [30.607, -110.957],
"company": "Grupo México",
"mining_method": "Underground"
},

{
"name": "Mina Porvenir",
"location": "Durango",
"coordinates": [24.510, -104.635],
"company": "Industrias Peñoles",
"mining_method": "Underground"
},
{
  "name": "Creston Mascota Deposit",
  "location": "Chihuahua",
  "coordinates": [28.970, -106.420],
  "company": "Agnico Eagle Mines",
  "mining_method": "Open-pit"
},

    {
      "name": "Dolores Mine",
      "location": "Chihuahua",
      "coordinates": [26.622, -105.583],
      "company": "Pan American Silver",
      "mining_method": "Open-pit, Underground"
    },
    {
      "name": "La Bolsa Mine",
      "location": "Sonora",
      "coordinates": [28.057, -109.477],
      "company": "Pan American Silver",
      "mining_method": "Open-pit"
    },
    {
      "name": "Alamo Dorado Mine",
      "location": "Sonora",
      "coordinates": [28.465, -109.762],
      "company": "Pan American Silver",
      "mining_method": "Open-pit, Underground"
    },
    {
      "name": "La Negra Mine",
      "location": "Querétaro",
      "coordinates": [20.768, -99.748],
      "company": "Pan American Silver",
      "mining_method": "Open-pit, Underground"
    },
    {
      "name": "San Vicente Mine",
      "location": "Zacatecas",
      "coordinates": [22.663, -102.554],
      "company": "Pan American Silver",
      "mining_method": "Underground"
    },
    
  {
    "name": "Cozamin Mine",
    "location": "Zacatecas",
    "coordinates": [22.663, -102.554],
    "company": "Capstone Copper",
    "mining_method": "Open-pit"
  },
  {
    "name": "San Martin Silver Mine",
    "location": "Jalisco",
    "coordinates": [20.686, -103.351],
    "company": "First Majestic Silver",
    "mining_method": "Underground"
  },
  {
    "name": "Mercedes Mine",
    "location": "Sonora",
    "coordinates": [29.609, -110.945],
    "company": "Equinox Gold",
    "mining_method": "Open-pit"
  },
  {
    "name": "El Limón-Guajes Mine",
    "location": "Guerrero",
    "coordinates": [17.669, -99.539],
    "company": "Torex Gold Resources",
    "mining_method": "Open-pit"
  },
  {
    "name": "Las Chispas Project",
    "location": "Sonora",
    "coordinates": [27.676, -109.903],
    "company": "SilverCrest Metals",
    "mining_method": "Underground"
  },
  {
    "name": "La Preciosa Project",
    "location": "Durango",
    "coordinates": [24.373, -104.750],
    "company": "Coeur Mining",
    "mining_method": "Open-pit"
  },
  {
    "name": "Aranzazu Mine",
    "location": "Zacatecas",
    "coordinates": [22.752, -102.338],
    "company": "Aura Minerals",
    "mining_method": "Underground"
  },
  {
    "name": "Los Ricos Project",
    "location": "Jalisco",
    "coordinates": [21.813, -104.502],
    "company": "GoGold Resources",
    "mining_method": "Open-pit"
  },
  {
    "name": "San Agustin Mine",
    "location": "Durango",
    "coordinates": [24.758, -104.847],
    "company": "Argonaut Gold",
    "mining_method": "Open-pit"
  },
  {
    "name": "Cordero Project",
    "location": "Chihuahua",
    "coordinates": [28.363, -105.815],
    "company": "Discovery Silver",
    "mining_method": "Open-pit"
  },
  {
    "name": "Los Reyes Project",
    "location": "Sinaloa",
    "coordinates": [25.924, -108.021],
    "company": "Prime Mining",
    "mining_method": "Open-pit"
  },
  {
    "name": "Santo Tomas Project",
    "location": "Sonora",
    "coordinates": [30.173, -111.211],
    "company": "Oroco Resource",
    "mining_method": "Open-pit"
  },

  {
    "name": "Rosario Mine",
    "location": "San Luis Potosi",
    "coordinates": [22.235, -100.961],
    "company": "Santacruz Silver",
    "mining_method": ""
  },
  {
    "name": "Zimapan Mine",
    "location": "Hidalgo",
    "coordinates": [20.770, -99.373],
    "company": "Santacruz Silver",
    "mining_method": ""
  },
  {
    "name": "Veta Grande Mine",
    "location": "Zacatecas",
    "coordinates": [22.784, -102.609],
    "company": "Santacruz Silver",
    "mining_method": ""
  },
  {
    "name": "Cosalá Operations",
    "location": "Sinaloa",
    "coordinates": [24.400, -106.679],
    "company": "Americas Gold and Silver",
    "mining_method": ""
  },
  {
    "name": "Avino Mine",
    "location": "Durango",
    "coordinates": [24.170, -104.689],
    "company": "Avino Silver & Gold Mines",
    "mining_method": ""
  },
  {
    "name": "Metates Project",
    "location": "Durango",
    "coordinates": [24.862, -107.947],
    "company": "Chesapeake Gold",
    "mining_method": ""
  },
  {
    "name": "Tepic Project",
    "location": "Nayarit",
    "coordinates": [21.499, -104.881],
    "company": "Sierra Madre Gold and Silver",
    "mining_method": ""
  },
  {
    "name": "El Tigre Project",
    "location": "Sonora",
    "coordinates": [28.532, -109.005],
    "company": "Silver Tiger Metals",
    "mining_method": ""
  },
  {
    "name": "San Diego Project",
    "location": "Durango",
    "coordinates": [24.494, -104.961],
    "company": "Golden Tag Resources",
    "mining_method": ""
  },
  {
    "name": "Cervantes Project",
    "location": "Sonora",
    "coordinates": [30.830, -109.877],
    "company": "Aztec Minerals",
    "mining_method": ""
  },
  {
    "name": "Plomosas Silver Project",
    "location": "Sinaloa",
    "coordinates": [25.791, -107.025],
    "company": "GR Silver Mining",
    "mining_method": ""
  },
  {
    "name": "Pilar Gold Project",
    "location": "Sonora",
    "coordinates": [29.449, -110.458],
    "company": "Tocvan Ventures",
    "mining_method": ""
  },
  {
    "name": "El Pinguico Mine",
    "location": "Guanajuato",
    "coordinates": [21.167, -101.097],
    "company": "Angel Wing Metals",
    "mining_method": ""
  },
  {
    "name": "Amalia Gold-Silver Project",
    "location": "Chihuahua",
    "coordinates": [27.008, -108.296],
    "company": "Radius Gold",
    "mining_method": ""
  },
  {
    "name": "La Joya Silver Project",
    "location": "Durango",
    "coordinates": [25.738, -104.905],
    "company": "Silver Dollar Resources",
    "mining_method": ""
  },
  {
    "name": "Miguel Auza Project",
    "location": "Zacatecas",
    "coordinates": [24.950, -103.270],
    "company": "Excellon Resources",
    "mining_method": ""
  },
  {
    "name": "Peñoles Project",
    "location": "Durango",
    "coordinates": [23.809, -104.606],
    "company": "Capitan Silver",
    "mining_method": ""
  },
  {
    "name": "Cerro Caliche Project",
    "location": "Sonora",
    "coordinates": [29.256, -110.351],
    "company": "Sonoro Gold",
    "mining_method": ""
  },
  {
    "name": "Cecilia Gold Project",
    "location": "Sonora",
    "coordinates": [29.670, -110.639],
    "company": "Riverside Resources",
    "mining_method": ""
  },
  {
    "name": "Sibila Project",
    "location": "Sonora",
    "coordinates": [30.664, -112.707],
    "company": "Vortex Metals",
    "mining_method": ""
  },
  {
    "name": "Batopilas Project",
    "location": "Chihuahua",
    "coordinates": [26.424, -107.255],
    "company": "Reyna Gold",
    "mining_method": ""
  },
  {
    "name": "Sierra Mojada Project",
    "location": "Coahuila",
    "coordinates": [27.524, -103.242],
    "company": "Silver Bull Resources",
    "mining_method": ""
  },
  {
    "name": "El Dorado Project",
    "location": "Nayarit",
    "coordinates": [21.916, -105.239],
    "company": "Xali Gold",
    "mining_method": ""
  },
  {
    "name": "Pilar Gold-Silver Project",
    "location": "Sonora",
    "coordinates": [29.432, -110.458],
    "company": "Colibri Resource",
    "mining_method": ""
  },
  {
    "name": "La Trini Project",
    "location": "Sinaloa",
    "coordinates": [25.379, -107.884],
    "company": "Kingsmen Resources",
    "mining_method": ""
  },
  {
    "name": "La Yesca Project",
    "location": "Nayarit",
    "coordinates": [21.024, -104.362],
    "company": "Silver Valley Metals",
    "mining_method": ""
  },
  {
    "name": "Pino de Plata Project",
    "location": "Chihuahua",
    "coordinates": [27.695, -106.862],
    "company": "Silver Spruce Resources",
    "mining_method": ""
  },
  {
    "name": "Momo Project",
    "location": "Sonora",
    "coordinates": [29.480, -110.446],
    "company": "Monumental Minerals",
    "mining_method": ""
  },
  {
    "name": "Tarachi Project",
    "location": "Sonora",
    "coordinates": [27.884, -109.614],
    "company": "Monumental Minerals",
    "mining_method": ""
  }
]

# Create a map centered on Mexico
map_mines = folium.Map(location=[23.634, -102.552], zoom_start=5)

# Define a color scheme for the mining methods
color_scheme = {
    "Open-pit": "blue",
    "Underground": "red",
    "Exploration": "green",
    "Open-pit, Underground": "orange",
    "": "purple"
}

# Create a feature group for each company
company_groups = {}

# Add markers for each mine to the corresponding company group
for mine in mines:
    name = mine["name"]
    location = mine["location"]
    coordinates = mine["coordinates"]
    company = mine["company"]
    mining_method = mine["mining_method"]

    # Determine the marker color based on the mining method
    color = color_scheme.get(mining_method, "gray")

    # Create a marker
    marker = folium.Marker(
        location=coordinates,
        popup=f"{name}<br>{location}<br>{company}<br>{mining_method}",
        icon=folium.Icon(color=color),
        data_company=company  # Add a data attribute to the marker for filtering
    )

    # Create a feature group for the company if it doesn't exist
    if company not in company_groups:
        company_groups[company] = folium.FeatureGroup(name=company)

    # Add the marker to the corresponding company group
    marker.add_to(company_groups[company])

# Add the company groups to the map
for company_group in company_groups.values():
    company_group.add_to(map_mines)

# Create a dropdown filter
dropdown_template = """
<label for="company-filter">Company:</label>
<select id="company-filter">
  <option value="all">All Companies</option>
  {% for company in companies %}
  <option value="{{ company }}">{{ company }}</option>
  {% endfor %}
</select>
"""

# Get the distinct list of companies
companies = list(company_groups.keys())

# Add the dropdown filter to the map
dropdown_html = Template(dropdown_template).render(companies=companies)
dropdown_script = """
<script>
    var dropdown = document.getElementById('company-filter');
    var markers = [];

    // Function to show or hide markers based on selected company
    function updateMarkers() {
        var selectedCompany = dropdown.value;

        // Show or hide markers based on the selected company
        markers.forEach(function(marker) {
            if (selectedCompany === 'all' || marker.options.data_company === selectedCompany) {
                marker.setOpacity(1);
            } else {
                marker.setOpacity(0);
            }
        });
    }

    dropdown.addEventListener('change', updateMarkers);

    // Add markers to the map and store in the markers array
    Object.values(companyGroups).forEach(function(company_group) {
        company_group.getLayers().forEach(function(layer) {
            markers.push(layer);
            layer.addTo(map_mines);
        });
    });

    // Initial marker visibility based on the selected company
    updateMarkers();

</script>
"""

map_mines.get_root().html.add_child(folium.Element(dropdown_html))
map_mines.get_root().html.add_child(folium.Element(dropdown_script))

# Save the map to an HTML file
map_mines.save("index.html")