"""fcfserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.views.generic import TemplateView
from django.urls import path, re_path, include
from rest_framework import routers, serializers, viewsets
from rest_framework.urlpatterns import format_suffix_patterns
from football.views import (
    restaurant_listview,
    RestaurantListView,
)

#### DRF Testing
from django.contrib.auth.models import User
# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
### /End Testing

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include(router.urls)),
    # re_path(r'^$', TemplateView.as_view(template_name='home.html')), 
    re_path(r'^restaurants/$', RestaurantListView.as_view()),
    re_path(r'^restaurants/(?P<slug>\w+)/$', RestaurantListView.as_view()),
    #re_path(r'^restaurants/asian/$', AsianFusionRestaurantListView.as_view()),
    re_path(r'^about/$', TemplateView.as_view(template_name='about.html')),
    re_path(r'^contact/$', TemplateView.as_view(template_name='contact.html')),
    re_path(r'^api-auth/', include('rest_framework.urls'))
    
]

urlpatterns = format_suffix_patterns(urlpatterns)