from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="FinTrak API",
        default_version='v1',
        description="Finanacial Analytics API",
        contact=openapi.Contact(email="hrfunsojoba@gmail.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
    path('user/', include('user_app.urls')),
    path('income/', include('income_app.urls')),
    path('expense/', include('expense_app.urls')),
    path('swagger/', schema_view.with_ui('swagger',
        cache_timeout=0), name='schema-swagger-ui'),

]
