from django.urls import path
from inventories.views import DeviceListView, DeviceDetailView, DeviceResultsView # DeviceCreateView
# from . import views #noob way

# FUNCTION BASED VIEWS
# urlpatterns = [
#     path('', views.index, name='index'),
# ]

app_name = 'device_inventory'
urlpatterns = [
    #sample for int:id and function-based views
    # path('', views.index, name='index'), # ex: /polls/
    # path('<int:question_id>/', views.detail, name='detail'), # ex: /polls/5/
    # path('<int:question_id>/results/', views.results, name='results'), # ex: /polls/5/results/
    # path('<int:question_id>/vote/', views.vote, name='vote'), # ex: /polls/5/vote/
    
    #Generic Views
    path('', DeviceListView.as_view(), name='device-list'),
    path('<str:slug>/', DeviceDetailView.as_view(), name='device-detail'),
    path('<str:slug>/results/', DeviceResultsView.as_view(), name='device-results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),
    # path('wiki/create/', DeviceCreateView.as_view(), name='wiki-create-page'), #add soon
    path('thanks/', DeviceDetailView.as_view(), name='device-thanks'),
]