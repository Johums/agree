# -*- coding: utf-8 -*-

from django.conf.urls import url

import views

urlpatterns = [
    url(r"^$", views.storeHouse, name="storeHouse" ),
    url(r"^dataStore$", views.dataStore, name="dataStore" ),
]
