from django.contrib import admin
from django.urls import path, include, url
from django.views.static import serve
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from DjangoMedicalApp import views

router = routers.DefaultRouter()
router.register('company', views.CompanyViewSet, basename="Company")
router.register('companybank', views.CompanyBankViewSet,
                basename="CompanyBank")
router.register('medicine', views.MedicineViewSet,
                basename="medicine")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/gettoken/', TokenObtainPairView.as_view(), name="getToken"),
    path('api/refresh_token/', TokenRefreshView.as_view(), name="getToken"),
    path('api/companybyname/<str:name>/',
         views.CompanyNameViewSet.as_view(), name="CompanyNameViewSet"),
    url(r'^media/(?P<path>.*)$', serve,
        {'document_root':       settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,
        {'document_root': settings.STATIC_ROOT}),
]
