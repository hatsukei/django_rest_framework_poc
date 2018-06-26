from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from serverInvent import views
from rest_framework.schemas import get_schema_view

# For schema view
schema_view = get_schema_view(title='serverInvent')

# API endpoints by url
urlpatterns = format_suffix_patterns([
    url(r'^schema/$', schema_view),

    url(r'^serverinvent/$',
        views.ServerInventList.as_view(),
        name='serverinvent-list'),

    url(r'^serverinvent/(?P<pk>[0-9]+)/$',
        views.ServerInventDetail.as_view(),
        name='serverinvent-detail'),

    url(r'^users/$',
        views.UserList.as_view(),
        name='user-list'),

    url(r'^users/(?P<pk>[0-9]+)/$',
        views.UserDetail.as_view(),
        name='user-detail'),

    url(r'^api-auth/', include('rest_framework.urls')),
])