from django.urls import path, include
from rest_framework import routers

from . import api
from . import views

router = routers.DefaultRouter()
router.register(r'clientsession', api.ClientSessionViewSet)
router.register(r'client', api.ClientViewSet)
router.register(r'spouse', api.SpouseViewSet)
router.register(r'child', api.ChildViewSet)


urlpatterns = (
    # urls for Django Rest Framework API
    path('api/v1/', include(router.urls)),
)

urlpatterns += (
    # urls for ClientSession
    path('clientsession/', views.ClientSessionListView.as_view(), name='client_clientsession_list'),
    path('clientsession/create/', views.ClientSessionCreateView.as_view(), name='client_clientsession_create'),
    path('clientsession/detail/<int:pk>/', views.ClientSessionDetailView.as_view(), name='client_clientsession_detail'),
    path('clientsession/update/<int:pk>/', views.ClientSessionUpdateView.as_view(), name='client_clientsession_update'),
)

urlpatterns += (
    # urls for Client
    path('client/', views.ClientListView.as_view(), name='client_client_list'),
    path('create/', views.ClientCreateView.as_view(), name='client_client_create'),
    path('detail/<slug:slug>/', views.ClientDetailView.as_view(), name='client_client_detail'),
    path('update/<slug:slug>/', views.ClientUpdateView.as_view(), name='client_client_update'),
)

urlpatterns += (
    # urls for Spouse
    path('spouse/', views.SpouseListView.as_view(), name='client_spouse_list'),
    path('spouse/create/', views.SpouseCreateView.as_view(), name='client_spouse_create'),
    path('spouse/detail/<slug:slug>/', views.SpouseDetailView.as_view(), name='client_spouse_detail'),
    path('spouse/update/<slug:slug>/', views.SpouseUpdateView.as_view(), name='client_spouse_update'),
)

urlpatterns += (
    # urls for Child
    path('child/', views.ChildListView.as_view(), name='client_child_list'),
    path('child/create/', views.ChildCreateView.as_view(), name='client_child_create'),
    path('child/detail/<slug:slug>/', views.ChildDetailView.as_view(), name='client_child_detail'),
    path('child/update/<slug:slug>/', views.ChildUpdateView.as_view(), name='client_child_update'),
)

urlpatterns += (
    # urls for docGeneration
    path('generate/', views.generateDoc2, name='generateDoc'),
)
