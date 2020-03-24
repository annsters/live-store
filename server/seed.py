from server import db, Stores
import sqlite3
import pandas as pd
import json

VANCOUVER_MAP_DATA_FILENAME = "map_data/vancouver_stores.json"



if __name__=="__main__":
  with open(VANCOUVER_MAP_DATA_FILENAME, "r") as vancouver_map_file:
    map_data = json.load(vancouver_map_file)
    print(len(map_data["features"]))

    df = pd.DataFrame(map_data["features"])
    print(df.columns)
    print(df.head)
    print(df)

    

    print(df.columns)

    for i in range(179):
      df["type"][i] = df["properties"][i]["name"]
  

    for i in range(179):
      df["properties"][i] = df["properties"][i]["shop"]
     


   

    for i in range(179):
      if len(df["geometry"][i]["coordinates"])== 2:

        lat = df["geometry"][i]["coordinates"][0]
        long = df["geometry"][i]["coordinates"][1]
        df["geometry"][i] = lat
        df["id"][i] = long
      else: 
        latsm = 0
        longsm = 0

        
        for k in range(len(df["geometry"][i]["coordinates"][0])):

       
          latsm += df["geometry"][i]["coordinates"][0][k][0]
          longsm += df["geometry"][i]["coordinates"][0][k][1]

        df["geometry"][i] = latsm/(k+1)
        df["id"][i] = longsm/(k+1)
  
    # print(df.columns)
    # print(df.head)
    # print(df)

    # TODO: use db to write stuff to Stores table.
    # print(map_data)
    # conn = sqlite3.connect("Stores.db")
    # df.to_sql("Stores", conn)

    df.columns = ['name', 'category', 'latitude', 'longitude']
   
   

    # adding to database

    for k in range(179):
        
        print(df['name'][k])
        print(df['name'])
        newStore = Stores(storeName= df['name'][k], category = df['category'][k], latitude = df['latitude'][k], longitude = df['longitude'][k])
    
        db.session.add(newStore)
        db.session.flush()
        db.session.commit()