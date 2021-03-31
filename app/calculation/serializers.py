from rest_framework import serializers
from .models import Calculation


class CalculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calculation
        order = True
        fields = (
            "id",
            "num1",
            "num2",
            "symbol",
            "result",
            "update_date",
            "delete_date",
            "create_date",
        )
