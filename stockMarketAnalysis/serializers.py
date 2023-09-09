from rest_framework import serializers
from .models import stock_market_data
class entity_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=stock_market_data
        fields="__all__"