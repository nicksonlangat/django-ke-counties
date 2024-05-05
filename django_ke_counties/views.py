from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import County, SubCounty, Ward
from .serializers import CountySerializer, SubCountySerializer, WardSerializer


class CountyApi(APIView):
    serializer_class = CountySerializer

    def get(self, request, format=None):
        return Response(
            self.serializer_class(County.objects.all(), many=True).data,
            status=status.HTTP_200_OK,
        )


class SubCountyApi(APIView):
    serializer_class = SubCountySerializer

    def get(self, request, format=None):
        return Response(
            self.serializer_class(SubCounty.objects.all(), many=True).data,
            status=status.HTTP_200_OK,
        )


class WardApi(APIView):
    serializer_class = WardSerializer

    def get(self, request, format=None):
        return Response(
            self.serializer_class(Ward.objects.all(), many=True).data,
            status=status.HTTP_200_OK,
        )
