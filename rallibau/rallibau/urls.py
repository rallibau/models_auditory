from django.urls import include, path
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from naturitas.infrastructure.views import AuditoryViewSet, HealthView, OneViewSet, TwoViewSet

router = routers.DefaultRouter()
router.register(r'one', OneViewSet)
router.register(r'two', TwoViewSet)
router.register(r'auditory', AuditoryViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("health/", HealthView.as_view()),
]

urlpatterns += router.urls
