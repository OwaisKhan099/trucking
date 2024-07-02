from django.db import models

class EldData(models.Model):
    driverId = models.CharField(max_length=20)
    timestamp = models.DateTimeField(auto_now_add=False)
    location = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
    def __str__(self):
     str_ = f'{self.driverId}  -  {self.location}  -  {self.status}  -  {str(self.timestamp)}'
     return str_
class HOSViolation(models.Model):
    driverId = models.CharField(max_length=20)
    violation_time = models.DateTimeField()
    violation_type = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f"{self.driverId} - {self.violation_type} - {self.violation_time}"

