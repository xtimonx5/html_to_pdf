from rest_framework import routers
from .views import GeneratePdfApiViewSet

router = routers.DefaultRouter()

router.register('gen_pdf', GeneratePdfApiViewSet, 'html-2-pdf')

urlpatterns = router.urls
