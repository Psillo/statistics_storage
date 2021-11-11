from rest_framework import serializers

from api.models import Statistic


class StatisticSerializer(serializers.ModelSerializer):

    class Meta:
        model = Statistic
        fields = '__all__'
