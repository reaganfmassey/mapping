import folium
import requests
import json

lat = ''
long = ''


ip_request = requests.get('https://get.geojs.io/v1/ip.json')
my_ip = ip_request.json()['ip']  # ip_request.json() => {ip: 'XXX.XXX.XX.X'}
print(my_ip)
         # Prints The IP string, ex: 198.975.33.4

# Step 2) Look up the GeoIP information from a database for the user's ip

geo_request_url = 'https://get.geojs.io/v1/ip/geo/' + my_ip + '.json'
geo_request = requests.get(geo_request_url)
geo_data = geo_request.json()
print(geo_data)
for word in geo_data:
    if word == 'latitude':
        lat = float(geo_data[word])
    if word == 'longitude':
        long = float(geo_data[word])


map = folium.Map(location=[lat, long], zoom_start=12)
map.save("local1.html")
