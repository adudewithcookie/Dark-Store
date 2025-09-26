from django.db import models

class Location(models.Model):

    name = models.CharField(max_length=200)
    address = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Shelf(models.Model):

    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='shelves')
    identifier = models.CharField(max_length=50)
    weight_capacity = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "shelves"
        
    def __str__(self):
        return f"Shelf {self.identifier} at {self.location.name}"
