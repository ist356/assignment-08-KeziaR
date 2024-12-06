'''
map_dashboard.py
'''
import streamlit as st
import streamlit_folium as sf
import folium
import pandas as pd
import geopandas as gpd
# these constants should help you get the map to look better
# you need to figure out where to use them
CUSE = (43.0481, -76.1474)  # center of map
ZOOM = 14                   # zoom level
VMIN = 1000                 # min value for color scale
VMAX = 5000                 # max value for color scale


df = pd.read_csv('./cache/top_locations_mappable.csv')

geodf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.lon, df.lat))
cuse_map = folium.Map(location=CUSE, Zoom_tart=ZOOM)
cues_map = geodf.explore(geodf['amount'], m= cuse_map,
                        marker_type = 'circle' ,
                        cmap='YlOrRd', vmin=VMIN, 
                        vmax=VMAX, legend=True, Legend_name = 'Amount', 
                        marker_kwd = {"radius": 10, "fill":True})

sf.folium_static(cuse_map)
