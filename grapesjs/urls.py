from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('page', views.page, name='page'),
    path('add', views.addpage, name='addpage'),
    path('edit/<slug>', views.editPage, name='editpage'),
    path('editPage/<slug>', views.editPageContent, name="editPageContent"),
    path('page/create', views.savePage, name='create_page'),
    path('preview/<slug>', views.previewPage, name='previewPage')
]