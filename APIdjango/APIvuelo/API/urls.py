from django.urls import path
from .views import VueloListView
from .views import VueloDetailView

urlpatterns = [
    path('vuelo/', VueloListView.as_view(), name='vuelo_list'),
    path('vuelo/<int:pk>', VueloDetailView.as_view(), name='vuelo_detail')
]