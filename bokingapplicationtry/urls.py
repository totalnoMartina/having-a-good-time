from django.urls import path
from .views import RoomReservation


urlpatterns = [
        path(r"^reservationroom/create/(?<pk>\d+)$", RoomReservation.as_view()),
]