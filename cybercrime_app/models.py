from pyexpat import model
from django.contrib.gis.db import models

# Create your models here.


REGIONS_OPTS = [

    ('Coast','Coast'),
    ('Central','Central'),
    ('Lower Eastern','Lower Eastern'),
    ('North Eastern','North Eastern'),
    ('North Rift','North Rift'),
    ('South Rift','South Rift'),
    ('Upper Eastern','Upper Eastern'),
    ('West Kenya','West Kenya'),
    ('Nairobi','Nairobi')
]

COUNTY_CHOICES = [
        
        ("Baringo", "Baringo"),
        ("Bomet", "Bomet"),
        ("Bungoma","Bungoma"),
        ("Busia", "Busia"),
        ("Elgeyo Marakwet", "Elgeyo Marakwet"),
        ("Embu",	"Embu"),
        ("Garissa", "Garissa"),
        ("Homa Bay", "Homa Bay"),
        ("Isiolo", "Isiolo"),
        ("Kajiado", "Kajiado"),
        ("Kakamega", "Kakamega"),
        ("Kericho", "Kericho"),
        ("Kiambu", "Kiambu"),
        ("Kilifi", "Kilifi"),
        ("Kirinyaga", "Kirinyaga"),
        ("Kisii", "Kisii"),
        ("Kisumu", "Kisumu"),
        ("Kitui", "Kitui"),
        ("Kwale", "Kwale"),
        ("Laikipia", "Laikipia"),
        ("Lamu", "Lamu"),
        ("Machakos", "Machakos"),
        ("Makueni", "Makueni"),
        ("Mandera", "Mandera"),
        ("Marsabit", "Marsabit"),
        ("Meru", "Meru"),
        ("Migori", "Migori"),
        ("Mombasa", "Mombasa"),
        ("Murang'a", "Murang'a"),
        ("Nairobi", "Nairobi"),
        ("Nakuru", "Nakuru"),
        ("Nandi", "Nandi"),
        ("Narok", "Narok"),
        ("Nyamira", "Nyamira"),
        ("Nyandarua", "Nyandarua"),
        ("Nyeri", "Nyeri"),
        ("Samburu", "Samburu"),
        ("Siaya", "Siaya"),
        ("Taita Taveta", "Taita Taveta"),
        ("Tana River", "Tana River"),
        ("Tharaka Nithi", "Tharaka Nithi"),
        ("Trans Nzoia", "Trans Nzoia"),
        ("Turkana", "Turkana"),
        ("Uasin Gishu", "Uasin Gishu"),
        ("Vihiga", "Vihiga"),
        ("Wajir", "Wajir"),
        ("West Pokot", "West Pokot"),
    ]

ATTACK_OPTS =[

    ('botnet','Botnet'),
    ('Financial fraud','Financial Fraud'),
    ('malware','Malware'),
    ('Phishing','Phishing'),
    ('spam','Spam'),
]

GENDER_OPTS = [

    ('Male','Male'),
    ('Female','Female'),
    ('Other','Other'),
]

class CyberVictims (models.Model):


    report_date_time = models.DateField(null=True)

    

    county= models.CharField(null=True,  blank= True, max_length=45, choices= COUNTY_CHOICES)

    region = models.CharField(null=True, blank= True, max_length=45, choices= REGIONS_OPTS)
    
    address= models.CharField(null=True, max_length=50, help_text="Type in the location / place where the \
        incident occurred in this field. Try to find out the exact location")

    type_of_attack = models.CharField(null=True, blank= True, max_length=15, choices= ATTACK_OPTS)

    gender = models.CharField(null=True, blank= True, max_length=10, choices= GENDER_OPTS)

    geom = models.PointField(srid=4326, null=True)

 

    def __str__(self):

        return self.type_of_attack

    class Meta:

        verbose_name = "Cyber Victim"
        verbose_name_plural = "Cyber Victims"




class CyberAttacks (models.Model):

    ip_address = models.CharField(max_length=55, null= True)

    country = models.CharField(max_length=70, null=True,  blank=False)

    city = models.CharField(max_length=70, null=True,blank=False)

    region_name = models.CharField(max_length=70, null=True)

    time_zone = models.CharField(max_length=70, null=True, blank=False)

    geom = models.PointField(srid=4326)

    type_of_attack = models.CharField(null=True, blank= True, max_length=35, choices= ATTACK_OPTS)

    class Meta:

        verbose_name = "Cyber Attack"
        verbose_name_plural = "Cyber Attacks"


