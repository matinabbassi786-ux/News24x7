from home.models import News
from rest_framework import serializers


class Newsserializers(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'
