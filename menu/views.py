from django.http import HttpResponse
from django.template import loader

def menu(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())


from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


def home(request):
    return render(request, 'home.html')


@api_view(['GET'])
def menu_api(request):
    menu_items = [
        {
            'id': 1,
            'name': 'Chicken Burger',
            'price': 5.00
        },
        {
            'id': 2,
            'name': 'Pizza',
            'price': 8.00
        },
        {
            'id': 3,
            'name': 'Fried Rice',
            'price': 6.00
        }
    ]

    return Response(menu_items)
