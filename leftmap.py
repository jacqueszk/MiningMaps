import folium
import json

# Read the mines data from a file
with open("mines.json") as file:
    mines = json.load(file)

# Create a map centered on Mexico
left_map = folium.Map(location=[23.634, -102.552], zoom_start=5)

# Define a color scheme for the mining methods
color_scheme = {
    "Open-pit": "blue",
    "Underground": "red",
    "Exploration": "green",
    "Open-pit, Underground": "orange",
    "": "purple"
}

# Iterate over the mines and add markers with color coding
for mine in mines:
    name = mine["name"]
    location = mine["location"]
    coordinates = mine["coordinates"]
    company = mine["company"]
    mining_method = mine["mining_method"]

    color = color_scheme.get(mining_method, "black")
    icon = folium.Icon(color=color, icon='circle', icon_color='white')

    popup_html = f"<b>{name}</b><br>Location: {location}<br>Company: {company}<br>Mining Method: {mining_method}"
    popup = folium.Popup(popup_html, max_width=250)

    folium.Marker(coordinates, icon=icon, popup=popup).add_to(left_map)

# Add legend to the map
legend_html = '''
     <div style="position: fixed; bottom: 50px; left: 50px; z-index: 1000; background-color: white; padding: 10px; border: 1px solid grey; font-size: 14px;">
       <p><strong>Legend</strong></p>
       <p><i class="fa fa-circle" style="color: blue;"></i> Open-pit</p>
       <p><i class="fa fa-circle" style="color: red;"></i> Underground</p>
       <p><i class="fa fa-circle" style="color: green;"></i> Exploration</p>
       <p><i class="fa fa-circle" style="color: orange;"></i> Open-pit, Underground</p>
       <p><i class="fa fa-circle" style="color: purple;"></i> Project</p>
     </div>
'''

left_map.get_root().html.add_child(folium.Element(legend_html))

# Save the map as an HTML file
left_map.save("left_map.html")







































