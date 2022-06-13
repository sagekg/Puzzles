#! /usr/bin/env python3


import matplotlib.pyplot as plt
import geopandas as gpd
import pandas as pd
import numpy as np

data = gpd.read_file('country_shapes/World_Countries__Generalized_.shp')

regions = pd.read_csv('country_shapes/regions.csv')

r = []
for c in data["COUNTRY"]:
    cr = regions[regions["name"] == c]["region"].values
    if len(cr) == 1:
        r.append(cr[0])
    else:
        r.append("None")

data["REGION"] = r

secret_idx = np.random.randint(len(data))
secret = data.loc[secret_idx]
map = data.drop(secret_idx).explore(tiles=None, tooltip=False)

out = r"output.html"

map.save(out)

print(secret)
