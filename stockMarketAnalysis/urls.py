from django import views
from django.urls import path,include
from .views import *
from .views import stockMarketViewSet
from rest_framework import routers

# for api perpose
router=routers.DefaultRouter()
router.register(r'exchange',stockMarketViewSet)

urlpatterns = [
    path('',home),
    path('insert/',insert),
    path('save/',save_data),
    path('update/<int:entity_id>/',update),
    path('do_update/<int:entity_id>/',do_update),
    path('delete/<int:entity_id>/',delete_entity),
    path('deleteAll/',deleteAll),
    path('jsonForm/', jsonform),
    path('loadJSON/',loadJSON),
    path('options/',options),
    # api perpose
    path('',include(router.urls)),
    

]
