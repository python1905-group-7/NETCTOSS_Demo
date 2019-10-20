from rest_framework import serializers

from LoginApp.models import AdminInfo


class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = AdminInfo
        fields = ['id', 'admin_code', 'password', 'name', 'telephone', 'email', 'enrolldate']
