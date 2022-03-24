import random

from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'generator/home.html')


def password(request):

    characters = list('qwertyuiopasdfghjklzxcvbnm')
    characters_upper = list('QWERTYUIOPASDFGHJKLZXCVBNM')
    special_symbols = list("!#$%&'()*+,-./:;<=>?@[\]^_`{|}~")
    numbers = list('1234567890')

    if request.GET.get('uppercase'):
        characters.extend(characters_upper)

    if request.GET.get('special_symbols'):
        characters.extend(special_symbols)

    if request.GET.get('numbers'):
        characters.extend(numbers)

    user_password = ''

    for i in range(int(request.GET.get('lenght', 7))):
        user_password += random.choice(characters)

    return render(request, 'generator/password.html', {'password': user_password})