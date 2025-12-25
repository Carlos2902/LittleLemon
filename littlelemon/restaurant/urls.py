from django.urls import path, include
from . import views
from rest_framework.authtoken.views import obtain_auth_token

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.MenuItemView.as_view(), name='menuitems'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    path('booking/', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]