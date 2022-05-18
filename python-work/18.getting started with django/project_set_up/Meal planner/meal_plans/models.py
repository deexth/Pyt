from django.db import models

# Create your models here.
class Meal(models.Model):
    """Whta are in the meals"""
    Foods = models.CharField(max_length=80)
    
    class Meta:
        verbose_name_plural = "Meals"
    
    def __str__(self):
        """Placeholder"""
        return self.Foods