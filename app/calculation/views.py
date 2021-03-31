from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Calculation
from .serializers import CalculationSerializer


class Calculations(APIView):
    def get(self, request):
        calculation_list = Calculation.objects.all()
        serializer = CalculationSerializer(calculation_list, many=True)
        return Response(serializer.data)
