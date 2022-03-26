from django.db import models
from djreservation.contrib.CRUD import ObjectView, UserObjectView


class Room(UserObjectView):
    """ A model for a room """
    model = TShirtmodel  # requiered
    template_name_base = "room/room.html"  # not required but recomendable
    namespace = "room"  # required
    fields = [ ... ]  # not required


room = Room()
