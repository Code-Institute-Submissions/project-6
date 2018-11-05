from django.urls import path

from listings import views as listings

urlpatterns = [
	path('', listings.plants, name="plants"),
	path('<int:plant_id>', listings.plant, name="plant"),
	path('search', listings.search, name="search")
]