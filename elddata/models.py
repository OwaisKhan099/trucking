from django.db import models

class EldData(models.Model):
    driverId = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
    def __str__(self):
     str_ = f'{self.driverId}  -  {self.location}  -  {self.status}  -  {str(self.timestamp)}'
     return str_
