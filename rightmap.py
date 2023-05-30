import folium
import json

# Read the mines data from a file
with open("mines.json") as file:
    mines = json.load(file)

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

# Create a dictionary to store the company-specific feature groups
company_groups = {}

# Iterate over the mines and add markers to the respective company groups
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

    if company not in company_groups:
        company_groups[company] = folium.FeatureGroup(name=company, show=False)  # Set show=False to deselect the company by default

    folium.Marker(coordinates, icon=icon, popup=popup).add_to(company_groups[company])

# Sort the company groups alphabetically
sorted_company_groups = sorted(company_groups.items(), key=lambda x: x[0])

# Add the sorted company-specific feature groups to the map
for company, group in sorted_company_groups:
    group.add_to(map_mines)

# Create a LayerControl and add it to the map
folium.LayerControl(collapsed=False, position='topright').add_to(map_mines)

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

map_mines.get_root().html.add_child(folium.Element(legend_html))

# Save the map as an HTML file
map_mines.save("right_map.html")















































