from rest_framework import viewsets

from .models import Thing
from .serializers import ThingSerializer


class ThingViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Thing instances
    to be viewed or edited.
    """
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
