from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BetViewSet

router = DefaultRouter()
router.register(r'bets', BetViewSet)

urlpatterns = [
]

urlpatterns += router.urls