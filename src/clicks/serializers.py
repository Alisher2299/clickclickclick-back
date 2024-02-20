from rest_framework import serializers
from .models import UserClick, CountryStatistic


class UserClickSerializer(serializers.ModelSerializer):
    country = serializers.CharField(read_only=True)
    latitude = serializers.FloatField(write_only=True)
    longitude = serializers.FloatField(write_only=True)

    class Meta:
        model = UserClick
        fields = (
            "created_dt",
            "username",
            "latitude",
            "longitude",
            "country",
            "click_count",
        )


class UserClickCreateSerializer(serializers.ModelSerializer):
    latitude = serializers.FloatField(write_only=True)
    longitude = serializers.FloatField(write_only=True)
    country = serializers.CharField(read_only=True)

    class Meta:
        model = UserClick
        fields = (
            "username",
            "country",
            "click_count",
            "latitude",
            "longitude",
            "created_dt",
        )


class UserClickRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserClick
        fields = (
            "created_dt",
            "username",
            "country",
            "city",
            "click_count",
        )


class CountryStatisticSerializer(serializers.ModelSerializer):
    class Meta:
        model = CountryStatistic
        fields = (
            "country", "click_count"
        )
