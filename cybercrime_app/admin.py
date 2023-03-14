from django.contrib.gis import admin
#from leaflet.admin import LeafletGeoAdmin

from .models import CyberAttacks, CyberVictims

# Register your models here.


class CyberVictimsAdmin (admin.OSMGeoAdmin):

    display_raw= True



class CyberAttacksAdmin (admin.OSMGeoAdmin):

    display_raw =True



admin.site.register (CyberVictims,CyberVictimsAdmin)
admin.site.register (CyberAttacks,CyberAttacksAdmin)