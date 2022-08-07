from django.contrib import admin
from django.urls import path,include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('applications',views.ApplicationView)
router.register('users',views.UserView)
router.register('farms',views.Farmview)
router.register('profile',views.Profileview)

urlpatterns = [
 
    path('',include(router.urls),name='test')
]

