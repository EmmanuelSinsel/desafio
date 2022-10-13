from rest_framework import routers

from apps.management.views import UserViewSet

router = routers.SimpleRouter()
router.register(r'managements', UserViewSet, 'managements')

urlpatterns = router.urls