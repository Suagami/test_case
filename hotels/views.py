
from .filters import QueryParamOrderFilterBackend
from .models import Hotel
from .pagination import LimitPagination
from .serializers import HotelSerializer
from rest_framework import viewsets, permissions


# Create your views here.
class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.select_related('city')
    serializer_class = HotelSerializer
    # permission_classes = (permissions.IsAuthenticated,)
    pagination_class = LimitPagination
    filter_backends = (QueryParamOrderFilterBackend,)
    ordering_fields = ['city_id']



