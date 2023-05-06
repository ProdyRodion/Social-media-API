from rest_framework import routers

from .views import PostViewSet

app_name = "social"

router = routers.DefaultRouter()
router.register("", PostViewSet)

urlpatterns = router.urls
