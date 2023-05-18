from django.db import models

class WantedPerson(models.Model):
    name = models.CharField(max_length=100)
    photo = models.URLField()
    crimes_committed = models.TextField()
    crime_type = models.TextField(max_length=100, default="Cyber") 
    investigation_status = models.BooleanField(default=True) #status da investigação
    
    
    class Meta:
        verbose_name_plural = "Wanted Persons"
    
    def __str__(self):
        return self.name
    