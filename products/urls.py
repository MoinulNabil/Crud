from django.urls import path

from .views import (
    ListCreateItems,
    RetrieveUpdateDeleteItems
)


urlpatterns = [
    path("", ListCreateItems.as_view(), name='list-create-items'),
    path("<int:pk>/", RetrieveUpdateDeleteItems.as_view(), name='retrieve-update-delete-items'),

]