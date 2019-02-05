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
    path('lawoffice/', views.lawOfficeListView.as_view(), name='lawOffice_lawoffice_list'),
    path('lawoffice/create/', views.lawOfficeCreateView.as_view(), name='lawOffice_lawoffice_create'),
    path('lawoffice/detail/<slug:slug>/', views.lawOfficeDetailView.as_view(), name='lawOffice_lawoffice_detail'),
    path('lawoffice/update/<slug:slug>/', views.lawOfficeUpdateView.as_view(), name='lawOffice_lawoffice_update'),
)

urlpatterns += (
    # urls for Lawyer
    path('lawyer/', views.LawyerListView.as_view(), name='lawOffice_lawyer_list'),
    path('lawyer/create/', views.LawyerCreateView.as_view(), name='lawOffice_lawyer_create'),
    path('lawyer/detail/<slug:slug>/', views.LawyerDetailView.as_view(), name='lawOffice_lawyer_detail'),
    path('lawyer/update/<slug:slug>/', views.LawyerUpdateView.as_view(), name='lawOffice_lawyer_update'),
)

urlpatterns += (
    # urls for Administrator
    path('administrator/', views.AdministratorListView.as_view(), name='lawOffice_administrator_list'),
    path('administrator/create/', views.AdministratorCreateView.as_view(), name='lawOffice_administrator_create'),
    path('administrator/detail/<slug:slug>/', views.AdministratorDetailView.as_view(), name='lawOffice_administrator_detail'),
    path('administrator/update/<slug:slug>/', views.AdministratorUpdateView.as_view(), name='lawOffice_administrator_update'),
)
