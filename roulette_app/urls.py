from rest_framework.routers import DefaultRouter
from .views import RouletteViewSet

router = DefaultRouter()
router.register(r'roulettes', RouletteViewSet, basename='roulette')

urlpatterns = [
]

urlpatterns += router.urls