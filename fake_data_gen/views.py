import os
from django.shortcuts import redirect
from django.contrib import messages
from aph.settings import DEBUG

from fake_data_gen.fake_gen import FakeData


def fake_data(request):
    if DEBUG:
        FakeData()
        messages.success(request, "Fake Data created")
        return redirect('index')
    else:
        messages.error(request, 
            "You need to run in 'DEBUG' mode to be able to do fake data!")
        return redirect('index')
