from pathlib import Path

from django.contrib.gis.utils.layermapping import LayerMapping

from .models import CyberVictims, CyberAttacks

cyber_victim_mapping = {
    'region': 'REGION',
    'county': 'COUNTY',
    'address':'SCENE',
    'type_of_attack': 'Type of at',
    'gender':'Gender',
    'geom':'POINT',
}

cyber_victims_shp = Path(__file__).resolve().parent / 'datasets' / 'shapefiles' / 'cyber_vict.shp'

def run(verbose=True):
    lm = LayerMapping(CyberVictims, str(cyber_victims_shp), cyber_victim_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)



cyber_attacks_mapping = {

    'ip_address': 'IP',
    'country': 'Country',
    'city': 'City',
    'region_name': 'Region Nam',
    'time_zone': 'Time Zone',
    'type_of_attack': 'Type of at',
    'geom': 'POINT',


}

cyber_attacks_shp = Path(__file__).resolve().parent / 'datasets' / 'shapefiles' / 'cyber_att.shp'

def run_2(verbose=True):
    lm = LayerMapping(CyberAttacks, str(cyber_attacks_shp), cyber_attacks_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
