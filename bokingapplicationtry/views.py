# from django.shortcuts import render
from djreservation.views import SimpleProductReservation
from .models import Room


class RoomReservation(SimpleProductReservation):
    """ A reservation setup """
    base_model = Room     # required
    amount_field = 'quantity'  # required
    max_amount_field = 'max_amount' # required
    extra_display_field = []  # not required.
