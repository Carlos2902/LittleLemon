from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(), name='menuitems'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    path('booking/', include(router.urls)),
]