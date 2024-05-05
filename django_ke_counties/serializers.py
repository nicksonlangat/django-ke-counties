from rest_framework import serializers

from .models import County, SubCounty, Ward


class CountySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = County


class SubCountySerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = SubCounty

    def to_representation(self, instance):
        data = super(SubCountySerializer, self).to_representation(instance)
        data["county"] = CountySerializer(instance.county).data
        return data


class WardSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Ward

    def to_representation(self, instance):
        data = super(WardSerializer, self).to_representation(instance)
        data["sub_county"] = SubCountySerializer(instance.sub_county).data
        return data
