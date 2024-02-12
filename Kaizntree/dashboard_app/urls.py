# dashboard_app/urls.py
from django.urls import path
from .views import ItemListView, build_dashboard, item_dashboard

urlpatterns = [
    path('item-dashboard/', item_dashboard, name='item-dashboard'),
    path('build-dashboard/', build_dashboard, name='build-dashboard'),
    path('api/items/', ItemListView.as_view(), name='api-items'),  # This assumes your API endpoint for items is in ItemListView
]
