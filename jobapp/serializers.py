from rest_framework import serializers
from.models import Jobdesc


class Jobdescserializer(serializers.ModelSerializer):
    class Meta:
        model = Jobdesc
        fields = '__all__'
