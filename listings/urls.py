from django.urls import path

from listings import views as listings

urlpatterns = [
    path('', listings.houses, name="houses"),
    path('house/add_house/<int:user_id>', listings.add_house, name="add_house"),
    path('house/preview_house/<int:user_id>/<int:house_id>',
         listings.preview_house, name="preview_house"),
    path('house/pay_fee/<int:user_id>/<int:house_id>',
         listings.pay_fee, name="pay_fee"),
    path('house/<int:house_id>', listings.house, name="house"),
    path('house/edit_house/<int:user_id>/<int:house_id>',
         listings.edit_house, name="edit_house"),
    path('house/delete_house/<int:user_id>/<int:house_id>',
         listings.delete_house, name="delete_house"),
    path('search', listings.search, name="search")
]
