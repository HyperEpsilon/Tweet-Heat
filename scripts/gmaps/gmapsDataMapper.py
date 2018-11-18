from ipywidgets.embed import embed_minimal_html
import gmaps

gmaps.configure(api_key="AIzaSyC3qCECSLE-f970GGyOpxsPBCj9n_SALIk")

fig = gmaps.figure()
embed_minimal_html('export.html', views=[fig])
