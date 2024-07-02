from django.urls import path, include
from . import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register(r"", views.EldDataViewSet)


urlpatterns = [
    path("",include(router.urls)),
    path('detect-hos-violations/<str:driver_id>/', views.DetectHOSViolationsView.as_view(), name='detect-hos-violations'),
]