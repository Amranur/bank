from django.conf.urls import url 
from django.urls import path,include
from . import views
from .views import (
    BranchesAPIView,
    BranchDetailAPIView,
    BanksAPIView,
    BankDetailAPIView,
    CreateAccountAPIView,
    AccountListAPIView

)

urlpatterns = [
    url(r'^branches/', BranchesAPIView.as_view(),name='branches'),
    url(r'^branch/(?P<pk>[0-9]+)/', BranchDetailAPIView.as_view(),name='branch-detail'),
    url(r'^banks', BanksAPIView.as_view(), name='banks'),
    url(r'^bank/(?P<pk>[0-9]+)/', BankDetailAPIView.as_view(), name='bank-detail'),
    url(r'^create_account/', CreateAccountAPIView.as_view(), name='create-account'),
    url(r'^accounts/', AccountListAPIView.as_view(), name='accounts'),
    path('swagger/', views.SwaggerView.as_view(), name='swagger'),
    path('swagger/(?P<format>.json|yaml)$', views.SwaggerView.as_view(), name='swagger-json'),
    path('docs/', include('drf_yasg.urls', namespace='drf_yasg')),
    path('docs/', include('drf_yasg.urls', namespace='drf_yasg')),
    
    
]