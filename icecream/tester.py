from icecream.models import Flavour
from icecream.serializers import FlavourSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

f = Flavour(name="chocolate", price=1.99)
f.save()

f = Flavour(name="vanilla", price=0.99)
f.save()