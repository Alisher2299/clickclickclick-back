from rest_framework import viewsets, status
from rest_framework.response import Response
from clicks.serializers import CountryStatisticSerializer
from clicks.models import CountryStatistic


class CountryStatisticViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CountryStatistic.objects.filter(country__isnull=False).order_by("-click_count")
    serializer_class = CountryStatisticSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
