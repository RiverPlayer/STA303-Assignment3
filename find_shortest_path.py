from typing import List
from plot_underground_path import plot_path
from build_data import Station, build_data

stations, underground_lines = build_data()


# Implement the following function
def get_path(start_station_name: str, end_station_name: str, map: dict[str, Station]) -> List[str]:
    """
    runs astar on the map, find the shortest path between a and b
    Args:
        start_station_name(str): The name of the starting station
        end_station_name(str): str The name of the ending station
        map(dict[str, Station]): Mapping between station names and station objects of the name
    Returns:
        List[Station]: A path composed of a series of station_name
    """
    pass


start_station_name = ...
end_station_name = ...
path = get_path(start_station_name, end_station_name, stations)
# visualization the path
# Open the visualization_underground/my_path_in_London_railway.html to view the path , and your path is marked in red
plot_path(path, 'visualization_underground/my_path_in_London_railway.html', stations, underground_lines)
