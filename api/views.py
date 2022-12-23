from django.shortcuts import render
from rest_framework import viewsets
from .models import Restaurant, Review
from .serializers import RestaurantSerializer,ReviewSerializer

# Create your views here.
class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer
    #authentication_classes = (TokenAuthentication,)

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

def restaurant_list(request):
    restaurant = Restaurant.objects.all()
    context = {
        'restaurant': restaurant
    }


    return render (request, 'api/restaurant_list.html', context) 
