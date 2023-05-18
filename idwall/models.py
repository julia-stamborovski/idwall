from django.db import models

class WantedPerson(models.Model):
    name = models.CharField(max_length=100)
    photo = models.URLField()
    physical_description = models.TextField() # descrição física
    nationality = models.CharField(max_length=50)
    crimes_committed = models.TextField()
    crime_type = models.CharField(max_length=100) 
    investigation_status = models.CharField(max_length=100) #status da investigação
    arrest_warrants = models.IntegerField() #mandados de prisao
    
    
    class Meta:
        verbose_name_plural = "Wanted Persons"
    
    def __str__(self):
        return self.name
    