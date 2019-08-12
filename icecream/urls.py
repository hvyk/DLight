from django.urls import include, path
from rest_framework import routers
from icecream import views


# router = routers.DefaultRouter()
# router.register(r'flavours', views.FlavourViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('flavours', views.FlavourList.as_view()),
    path('flavours/<int:pk>/', views.FlavourDetail.as_view()),
    path('containers', views.ContainerList.as_view()),
    path('containers/<int:pk>/', views.ContainerDetail.as_view()),
    path('orders', views.OrderList.as_view()),
    # path('orders/<int:pk>/', views.OrderDetail.as_view()),

    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]