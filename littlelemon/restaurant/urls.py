from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
  path('', views.home, name="home"),
  path('links', views.links, name="links"),
  path('api/menu', views.MenuItemsView.as_view()),
  path('api/menu-items', views.MenuItemsView.as_view()),
  path('api/menu/<int:pk>', views.SingleMenuItemView.as_view()),
  path('api/menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
  path('api-token-auth/', obtain_auth_token),
]
