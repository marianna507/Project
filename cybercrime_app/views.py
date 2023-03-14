from django.core.serializers import serialize
from django.http import HttpResponse
from django.views.generic import TemplateView

from .models import CyberAttacks, CyberVictims

# Create your views here.

def cyberattack_dataset(request):

    cyber_attacks = serialize  ('geojson',CyberAttacks.objects.all() )
    return HttpResponse (cyber_attacks, content_type='json')

def cybervictims_dataset(request):

    cyber_victims = serialize  ('geojson',CyberVictims.objects.all() )
    return HttpResponse (cyber_victims, content_type='json')


class CyberAttackView (TemplateView):

    template_name = 'cybercrime_app/index_attacks.html'

class CyberVictimsView (TemplateView):

    template_name = 'cybercrime_app/index_victims.html'