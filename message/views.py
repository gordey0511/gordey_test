from django.shortcuts import render
from .forms import MessageForm
from products.models import *


def message(request):
    current_day = "03.01.2017"
    form = MessageForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print (request.POST)
        print (form.cleaned_data)
        data  = form.cleaned_data
        print (data["name"])

        new_form = form.save()

    return render(request, 'message/message.html', locals())