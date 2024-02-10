from django.urls import path, include
from rest_framework import routers
from hotels.views import HotelViewSet

router = routers.DefaultRouter()
router.register('hotels', HotelViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]