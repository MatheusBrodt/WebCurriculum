from django.urls import path
from .views import ModelView, ProjectView, QualiView, CurView

urlpatterns = [
    # path('address/', My_View.as_view(), name='url_name')
    path('inicio/', ModelView.as_view(), name='index'),
    path('projects/', ProjectView.as_view(), name='projects'),
    path('quali/', QualiView.as_view(), name='qualifications'),
]
