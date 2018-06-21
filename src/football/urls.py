from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from football import views

router = DefaultRouter()
router.register(r'games', views.GameViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'seasons', views.SeasonViewSet)
router.register(r'weeks', views.WeekViewSet, 'week')
router.register(r'historic-bankrolls', views.HistoricBankrollViewSet)
router.register(r'profiles', views.ProfileViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'badges', views.BadgeViewSet)

urlpatterns = [
  url(r'^', include(router.urls)),
]