from rest_framework import status

from rest_framework import viewsets
from rest_framework.response import Response

from clicks.serializers import (
    UserClickSerializer,
    UserClickCreateSerializer,
    UserClickRetrieveSerializer
)
from clicks.models import UserClick, CountryStatistic


class UserClickViewSet(viewsets.ModelViewSet):
    queryset = UserClick.objects.all()
    serializer_class = UserClickSerializer
    retrieve_serializer = UserClickRetrieveSerializer

    def get_queryset(self):
        if self.action == 'list':
            return UserClick.objects.none()
        return UserClick.objects.all()

    def get_permissions(self):
        if self.action == 'retrieve' or self.action == 'create':
            return [permission() for permission in self.permission_classes]
        return []

    def create(self, request, *args, **kwargs):
        username = request.data.get('username', None)
        click_count = request.data.get('click_count', 0)

        if username:
            existing_record = UserClick.objects.filter(username=username).first()

            if existing_record:
                existing_record.click_count += click_count
                existing_record.save()

                country_statistic = CountryStatistic.objects.get(country=existing_record.country)
                country_statistic.click_count += click_count
                country_statistic.save()

                serializer = UserClickCreateSerializer(existing_record)
                return Response(serializer.data)

        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        username = self.kwargs.get('pk', None)

        if username:
            user_click = UserClick.objects.filter(username=username).first()

            if user_click:
                serializer = UserClickRetrieveSerializer(user_click)
                return Response(serializer.data)
            else:
                return Response({"error": f"No found username: {username}"},
                                status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "username parameter is required"}, status=status.HTTP_400_BAD_REQUEST)
