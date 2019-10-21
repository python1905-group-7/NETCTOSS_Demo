from rest_framework import serializers

from LoginApp.models import AdminInfo


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = AdminInfo
        fields = '__all__'
