import os
from django.shortcuts import redirect
from django.contrib import messages

from fake_data_gen.fake_gen import FakeData


def fake_data(request):
    if os.environ.get('DEBUG'):
        FakeData()
    else:
        messages.error(request, 
            "You need to run in 'DEBUG' mode to be able to do fake data!")
        return redirect('index')
