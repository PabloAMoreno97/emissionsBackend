from rest_framework.routers import DefaultRouter
from core.views import EmissionViewSet, CountryViewSet, ActivityViewSet, EmissionTypeViewSet

router = DefaultRouter()
router.register("emissions", EmissionViewSet)
router.register("activities", ActivityViewSet)
router.register("countries", CountryViewSet)
router.register("emission_types", EmissionTypeViewSet)

urlpatterns = router.urls
