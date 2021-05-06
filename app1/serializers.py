from rest_framework import fields, serializers
  
from .models import Advisor, Bookings, CustomUser


class AdvisorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Advisor
        fields=('id','advisor_name','advisor_photo_url')


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bookings
        fields=('id','advisor.id')