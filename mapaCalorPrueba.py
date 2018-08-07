from gmplot import gmplot

# Place map
gmap = gmplot.GoogleMapPlotter(37.766956, -122.438481, 13)


# Scatter points
top_attraction_lats, top_attraction_lons = zip(*[
    (37.769901, -122.498331),
    (37.768645, -122.475328),
    (37.771478, -122.468677),
    (37.769867, -122.466102),
    (37.767187, -122.467496),
    (37.770104, -122.470436)
    ])
gmap.heatmap(top_attraction_lats,top_attraction_lons)

# Draw
gmap.draw("my_map.html")
