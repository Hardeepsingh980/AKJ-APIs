from django.urls import path
from . import views

urlpatterns = [
    path('latest', views.GetLatestKirtan.as_view()),
    path('dropdowns', views.GetDropdowns.as_view()),
    path('search/<str:query>', views.GetSearchResults.as_view()),
    path('smaagam/<int:page_no>', views.GetSmaagam.as_view()),
    path('kirtansmaagam/<str:id>', views.GetKirtanFromSmaagam.as_view()),
]