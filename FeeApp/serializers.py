from rest_framework import serializers

from FeeApp.models import Cost


class CostSerializers(serializers.ModelSerializer):
    creatime = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')
    startime = serializers.DateTimeField(read_only=True, format='%Y-%m-%d %H:%M')

    class Meta:
        model = Cost
        fields = '__all__'
