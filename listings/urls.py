from django.urls import path

from listings import views as listings

urlpatterns = [
	path('', listings.houses, name="houses"),
	path('<int:house_id>', listings.house, name="house"),
	path('search', listings.search, name="search")
]