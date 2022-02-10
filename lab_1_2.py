"""HTML map module"""
import argparse
import folium
from folium.folium import Map
from haversine import haversine
from geopy.geocoders import Nominatim

parser = argparse.ArgumentParser(description="Program for showing 10 closest filming locations")
parser.add_argument('year', help='Year of release for films to look')
parser.add_argument('latitude', help='Location latitude')
parser.add_argument('longitude', help='Location longitude')
parser.add_argument('path_to_dataset', help='Path to a dataset')
args = parser.parse_args()

def read_file(path: str) -> dict:
    """
    Return a dict where keys are years and values are lists of films that where released that year
    """
    with open(path, 'r', encoding='utf-8', errors='ignore') as file:
        lines = file.readlines()
        lines = [list(filter(lambda x: x != '', i.strip().split('\t'))) for i in lines[14:-1]]
        films_by_years_dict = {}
        for line in lines:
            year = line[0].split()[-1][1:5]
            if year not in films_by_years_dict:
                films_by_years_dict[year] = []
            films_by_years_dict[year].append(line)
    return films_by_years_dict

def find_cords(films: list) -> list:
    """
    Find cordinates of filming places
    >>> find_cords([['"#LakeShow" (2012)', 'El Segundo, California, USA']])
    [['"#LakeShow" (2012)', 'El Segundo, California, USA', (33.917028, -118.4156337)]]
    """
    geolocator = Nominatim(user_agent="lab_1_2.py")
    lst = []
    for film in films:
        location = geolocator.geocode(film[1])
        if location is None:
            continue
        else:
            lst.append([film[0], film[1], (location.latitude, location.longitude)])
    return lst

def find_distance(cords: tuple, lst: list) -> list:
    """
    Find distance between user cordinates and filming places cordinates
    >>> find_distance((1,1), [['A', 'El Segundo, California, USA', (33.917028, -118.4156337)]])
    [['A', 'El Segundo, California, USA', (33.917028, -118.4156337), 12613.852757382992]]
    """
    for i in lst:
        i.append(haversine(cords, i[2]))
    return lst

def put_markers(markers: list, name: str, map: Map):
    """
    Put markers on the map
    """
    fg = folium.FeatureGroup(name=name)
    location_cords = []
    for item in markers:
        if item[2] in location_cords:
            item[2] = (item[2][0]+0.008, item[2][1]+0.008)
        else:
            location_cords.append(item[2])
    for item in markers:
        fg.add_child(folium.Marker(location=item[2], popup=folium.Popup(item[0])))
    map.add_child(fg)

def main():
    """
    Main function
    """
    films_by_years_dict = read_file(args.path_to_dataset)
    needed_films = films_by_years_dict[args.year]
    lst = find_cords(needed_films)
    cords = (int(args.latitude), int(args.longitude))
    lst = find_distance(cords, lst)
    lst.sort(key=lambda x: x[-1])
    ten_closest = lst[:10]
    ten_farest = lst[-10:]
    map = folium.Map(location=[args.latitude, args.longitude], zoom_start=5)
    put_markers(ten_closest, "10 closest filming locations", map)
    put_markers(ten_farest, "10 farest filming locations", map)
    map.add_child(folium.LayerControl())
    map.save('Map.html')

if __name__ == '__main__':
    main()
