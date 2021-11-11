from django.urls import include, path

from rest_framework.routers import DefaultRouter

from api.views import StatisticViewSet, GetTokenView


app_name = 'api'
router = DefaultRouter()
router.register('statistic', StatisticViewSet, 'statistic')


urlpatterns = [
    path('api/login/', GetTokenView.as_view(), name='login'),
    path('api/', include(router.urls))
]
