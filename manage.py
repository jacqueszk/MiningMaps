import folium

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
        "name": "San Julian Mine",
        "location": "Chihuahua",
        "coordinates": [26.653, -105.652],
        "company": "Fresnillo plc",
        "mining_method": "Open-pit"
    },
    {
        "name": "La Platosa Mine",
        "location": "Durango",
        "coordinates": [25.085, -103.791],
        "company": "Plata Latina Minerals",
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
        "company": "Endeavour Silver",
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
        "name": "La Platosa Mine",
        "location": "Durango",
        "coordinates": [24.011, -103.945],
        "company": "Excellon Resources",
        "mining_method": "Underground"
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
        "name": "Cerro Moro Mine",
        "location": "Santa Cruz",
        "coordinates": [-47.706, -69.573],
        "company": "Yamana Gold",
        "mining_method": "Underground"
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
    }
]



# Create a map centered on Mexico
map_mines = folium.Map(location=[23.6345, -102.5528], zoom_start=5)

# Define colors for the markers
open_pit_color = 'blue'
underground_color = 'brown'

# Add markers for each mine
for mine in mines:
    name = mine["name"]
    location = mine["location"]
    coordinates = mine["coordinates"]
    company = mine["company"]
    mining_method = mine["mining_method"]
    
    tooltip = f"{name}\nLocation: {location}\nCompany: {company}\nMining Method: {mining_method}"
    
    # Set marker color based on mining method
    if mining_method == "Open-pit":
        marker_color = open_pit_color
    else:
        marker_color = underground_color
    
    folium.Marker(
        location=coordinates,
        popup=tooltip,
        icon=folium.Icon(color=marker_color, icon="industry", prefix="fa")
    ).add_to(map_mines)

# Save the map to an HTML file
map_mines.save("index.html")


