from . import views
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = routers.DefaultRouter()
router.register(r'', views.Jobdescview,
                basename='Jobdesc')

urlpatterns = router.urls
