from rest_framework import routers
from fetchimg.viewsets import ImgViewSet

router=routers.DefaultRouter()
router.register('',ImgViewSet)