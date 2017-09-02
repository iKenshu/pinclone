from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from .views import PinList, PinCreate, PinDetail, PinDelete, PinEdit

app_name = 'Pin'
urlpatterns = [
    url(r'^$', PinList.as_view(), name='pin_list'),
    url(r'^pin/add/$', PinCreate.as_view(), name='pin_add'),
    url(r'^pin/(?P<pk>\d+)/$', PinDetail.as_view(), name='pin_detail'),
    url(r'^pin/delete/(?P<pk>\d+)/$', PinDelete.as_view(), name='pin_delete'),
    url(r'^pin/edit/(?P<pk>\d+)/$', PinEdit.as_view(), name='pin_edit'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)