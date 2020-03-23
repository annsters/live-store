from server import db, Stores
import json

VANCOUVER_MAP_DATA_FILENAME = "map_data/vancouver_stores.json"

if __name__=="__main__":
  with open(VANCOUVER_MAP_DATA_FILENAME, "r") as vancouver_map_file:
    map_data = json.load(vancouver_map_file)
    print(len(map_data["features"]))
    # TODO: use db to write stuff to Stores table.
    # print(map_data)
