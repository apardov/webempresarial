from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from pages import views

urlpatterns = [
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('<int:page_id>', views.page, name='page'),
]
