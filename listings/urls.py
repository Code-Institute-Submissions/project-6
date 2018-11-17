from django.urls import path

from listings import views as listings

urlpatterns = [
	path('', listings.houses, name="houses"),
	path('house/<int:house_id>', listings.house, name="house"),
	path('house/<int:house_id>', listings.edit_house, name="edit_house"),
	path('search', listings.search, name="search")
]
