from django.urls import re_path
from .views import index, PlayerViewSet
from rest_framework import routers

router = routers.SimpleRouter(trailing_slash='optional')
router.register(r'players', PlayerViewSet, base_name='players')

urlpatterns = [
    re_path(r'^$', index),
]

urlpatterns += router.urls