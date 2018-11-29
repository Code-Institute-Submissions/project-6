from django.urls import path

from listings import views as listings

urlpatterns = [
    path('', listings.houses, name="houses"),
    path('house/add_house/<int:user_id>', listings.add_house, name="add_house"),
    path('house/<int:house_id>', listings.house, name="house"),
    path('house/edit_house/<int:house_id>',
         listings.edit_house, name="edit_house"),
    path('search', listings.search, name="search")
]
