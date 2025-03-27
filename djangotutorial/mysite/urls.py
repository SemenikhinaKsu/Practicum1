from django.contrib import admin
from django.urls import include, path
from polls.nocodb_utils import get_nocodb_data
from rest_framework.routers import DefaultRouter
from polls.views import QuestionViewSet, ChoiceViewSet, BankViewSet, TransactionViewSet, ClientViewSet, DepositViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
router = DefaultRouter()
router.register(r'questions', QuestionViewSet)
router.register(r'choices', ChoiceViewSet)
router.register(r'banks', BankViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'clients', ClientViewSet)
router.register(r'deposits', DepositViewSet)

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="API documentation for My Django Project",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('', include(router.urls)),
    path('nocodb-data/', get_nocodb_data, name='nocodb_data'),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('polls.urls')),
]

