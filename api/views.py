from django.contrib.auth import authenticate

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.status import (
    HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK
)
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .serializers import Statistic, StatisticSerializer


class GetTokenView(APIView):
    def get(self, request, format=None):
        username = request.data.get("username")
        password = request.data.get("password")

        if username is None or password is None:
            return Response(
                {'Ошибка!': 'Введите имя пользователя и/или пароль.'},
                status=HTTP_400_BAD_REQUEST
            )

        user = authenticate(username=username, password=password)

        if not user:
            return Response(
                {'Ошибка!': 'Такого пользователя не существует!'},
                status=HTTP_404_NOT_FOUND
            )

        token, _ = Token.objects.get_or_create(user=user)
        return Response(
            {'token': token.key},
            status=HTTP_200_OK
        )


class StatisticViewSet(viewsets.ModelViewSet):
    queryset = Statistic.objects.all().order_by('-date')
    serializer_class = StatisticSerializer
    permission_classes = [IsAuthenticated, IsAdminUser]

    def list(self, request, *args, **kwargs):
        start = request.data.get('from')
        end = request.data.get('to')
        order_by = request.data.get('order_by') if \
            request.data.get('order_by') else '-date'

        if start and end:
            if len(start) == 10 and len(end) == 10:
                try:
                    start.split('-')
                    end.split('-')
                    queryset = self.filter_queryset(
                        Statistic.objects.filter(
                            date__range=(start, end)
                        ).order_by(order_by)
                    )

                    page = self.paginate_queryset(queryset)
                    if page is not None:
                        serializer = self.get_serializer(
                            page, many=True
                        )
                        return self.get_paginated_response(
                            serializer.data
                        )

                    serializer = self.get_serializer(
                        queryset, many=True
                    )
                    return Response(serializer.data)
                except:
                    return Response(
                        {'Ошибка!':
                         'Введите дату начала и окончания периода, ' +
                         'в формате YYYY-MM-DD. ' +
                         'И правильный метод сортировки.'},
                        status=HTTP_400_BAD_REQUEST
                    )
            else:
                return Response(
                    {'Ошибка!':
                     'Введите дату начала и окончания периода, ' +
                     'в формате YYYY-MM-DD. ' +
                     'И правильный метод сортировки.'},
                    status=HTTP_400_BAD_REQUEST
                )
        else:
            return super().list(request, *args, **kwargs)

    @action(detail=False, methods=['post'])
    def delete_all(self, request):
        result = Statistic.objects.all().delete()
        return Response('Удалено {} объектов.'.format(result[0]))
