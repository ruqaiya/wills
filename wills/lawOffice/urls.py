from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'lawoffice', api.lawOfficeViewSet)
router.register(r'lawyer', api.LawyerViewSet)
router.register(r'administrator', api.AdministratorViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for lawOffice
    path('lawOffice/lawoffice/', views.lawOfficeListView.as_view(), name='lawOffice_lawoffice_list'),
    path('lawOffice/lawoffice/create/', views.lawOfficeCreateView.as_view(), name='lawOffice_lawoffice_create'),
    path('lawOffice/lawoffice/detail/<slug:slug>/', views.lawOfficeDetailView.as_view(), name='lawOffice_lawoffice_detail'),
    path('lawOffice/lawoffice/update/<slug:slug>/', views.lawOfficeUpdateView.as_view(), name='lawOffice_lawoffice_update'),
)

urlpatterns += (
    # urls for Lawyer
    path('lawOffice/lawyer/', views.LawyerListView.as_view(), name='lawOffice_lawyer_list'),
    path('lawOffice/lawyer/create/', views.LawyerCreateView.as_view(), name='lawOffice_lawyer_create'),
    path('lawOffice/lawyer/detail/<slug:slug>/', views.LawyerDetailView.as_view(), name='lawOffice_lawyer_detail'),
    path('lawOffice/lawyer/update/<slug:slug>/', views.LawyerUpdateView.as_view(), name='lawOffice_lawyer_update'),
)

urlpatterns += (
    # urls for Administrator
    path('lawOffice/administrator/', views.AdministratorListView.as_view(), name='lawOffice_administrator_list'),
    path('lawOffice/administrator/create/', views.AdministratorCreateView.as_view(), name='lawOffice_administrator_create'),
    path('lawOffice/administrator/detail/<slug:slug>/', views.AdministratorDetailView.as_view(), name='lawOffice_administrator_detail'),
    path('lawOffice/administrator/update/<slug:slug>/', views.AdministratorUpdateView.as_view(), name='lawOffice_administrator_update'),
)

