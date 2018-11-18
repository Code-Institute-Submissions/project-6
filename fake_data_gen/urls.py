from django.urls import path

from fake_data_gen import views as fake_data_gen


urlpatterns = [
	path('', fake_data_gen.fake_data, name="fake_data"),
]

