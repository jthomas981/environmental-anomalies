from django.shortcuts import render
from backend import env_filter
from .forms import WeatherForm
import folium
from geopy.distance import geodesic

def map_request(request):
    """Take parameters from user and display environment anomalies."""
    if request.method == "POST":
        form = WeatherForm(request.POST)
        if form.is_valid():
            # Gather environment anomalies.
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            env_data = env_filter.get_data(start_date, end_date)

            # Create map centered on user's starting location.
            center_lat = form.cleaned_data['lat']
            center_lon = form.cleaned_data['lon']
            center = (center_lat, center_lon)
            map = folium.Map(location=center, zoom_start=3)

            # Add weather anomalies to map if it's within search radius.
            radius = form.cleaned_data['radius']
            for environment_event in env_data:
                coords = (environment_event['Latitude'], environment_event['Longitude'])
                # Check that environment event is in search area.
                if geodesic(center, coords).kilometers <= radius:
                    # All icons/popups have to be initialize each iteration.
                    custom_icon = folium.CustomIcon(
                        icon_image=f'static/icons/{environment_event["Event"]}.png',
                        icon_size=[50, 50]
                    )
                    custom_popup = folium.Popup(
                        html=environment_event["Title"], 
                        max_width=500
                    )
                    try:
                        folium.Marker(
                            location=coords,
                            icon=custom_icon,
                            tooltip="Select for more details",
                            popup=custom_popup
                        ).add_to(map)
                    except ValueError:
                        continue

            return render(request, 'map_result.html', 
                          {'map': map._repr_html_()})
    else:
        form = WeatherForm()

    map = folium.Map()
    return render(request, 'map_request.html', {"form": form,
                                                     "map": map._repr_html_()})