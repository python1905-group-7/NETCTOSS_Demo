from rest_framework import serializers

from FeeApp.models import Cost


class CostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cost
        fields = [
            'id',
            'name',
            'base_duration',
            'base_cost',
            'unit_cost',
            'status',
            'descr',
            'creatime',
            'startime',
            'cost_type'
        ]
