from django.shortcuts import render
import requests
from weatherapp.forms import SearchForm

# Create your views here.
def index(request):
    form = SearchForm()
    data = None
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            lat = form.cleaned_data['latitude']
            lon = form.cleaned_data['longitude']
            purl = 'https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=' + str(lat) + '&lon=' + str(lon)
            print(purl)
            headers = headers=requests.utils.default_headers()
            headers.update(
    {
        'User-Agent': 'My User Agent 1.0',
    }
)

            r = requests.get(purl, headers=headers)
            data = r
            print(r.status_code)
    return render(request, 'index.html', context={'form': form, "data": data})