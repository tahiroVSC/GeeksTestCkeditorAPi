from rest_framework.generics import ListAPIView, RetrieveAPIView

from apps.Offering.models import Offering
from apps.Offering.serializers import OfferingSerializers
    
    # Create your views here.
class OfferingAPIViews(ListAPIView):
    queryset = Offering.objects.all()[:10]
    serializer_class = OfferingSerializers

   
# class OfferingDetailViewAPI(RetrieveAPIView):
#     queryset = Offering.objects.all()
#     serializer_class = OfferingDetailSerializer
#     lookup_field = 'id'