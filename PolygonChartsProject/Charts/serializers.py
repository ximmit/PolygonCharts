from rest_framework import serializers
from .models import HistoricalData

class HistoricalDataSerializer(serializers.ModelSerializer):
    ticker = serializers.CharField()
    o = serializers.CharField()
    h = serializers.CharField()
    l = serializers.CharField()
    c = serializers.CharField()
    v_name = serializers.CharField()
    vw = serializers.CharField()
    t = serializers.CharField()
    n = serializers.CharField()
    class Meta:
        model = HistoricalData
        fields = ('ticker', 'o', 'h', 'l', 'c', 'v_name', 'vw', 't', 'n')





