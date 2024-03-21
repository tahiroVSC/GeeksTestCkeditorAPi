from rest_framework import serializers

from apps.Offering.models import Offering    
   
class OfferingSerializers(serializers.ModelSerializer):
    class Meta:
        model = Offering
        exclude = ('title',)
