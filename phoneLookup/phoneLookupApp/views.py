from django.shortcuts import render
import json
from django.views.decorators.csrf import csrf_exempt
from .forms import PhoneNumberForm
from django.http import HttpResponse
from .utils import numberInfo

# Create your views here.
@csrf_exempt
def home(request):
    context = {}
    if request.method == 'POST':
        form = PhoneNumberForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data.get("phone_number")
            # print('form_data', form_data)
            number_info = numberInfo(form_data)
            context['number_info'] = number_info
            # print(number_info)
            # return render(request, "home.html", {"number_info": number_info})
        else:
            context['error'] = "Invalid data from client"
            print("Invalid data from client")
    return render(request, "home.html", context)
