from .views import RestaurantViewSet,ReviewViewSet
from django.urls import path
from . import views
from django.conf.urls import include
from rest_framework import routers


router = routers.DefaultRouter()
#router.register('users', UserViewSet)
router.register('Restaurants', RestaurantViewSet)
router.register('Reviews', ReviewViewSet)

urlpatterns = [
    path('api',include (router.urls)),
    path('', views.restaurant_list, name='restaurant_list'),
     
   

]
