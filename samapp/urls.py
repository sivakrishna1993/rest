from django.urls import path, include
from rest_framework import routers
from samapp import views

router = routers.DefaultRouter()
router.register('Student',views.StudentView)
router.register('Language',views.LanguageView)

urlpatterns =[
    path('',include(router.urls))
]
