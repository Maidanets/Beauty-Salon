from django.db import models
# Create your models here.


class Services(models.Model):
    name_service = models.CharField(max_length=100)
    time_service = models.IntegerField()
    price_service = models.IntegerField()

    def __str__(self):
        return f'{self.name_service} {self.time_service} {self.price_service}'


class Master(models.Model):
    name_master = models.CharField(max_length=100)
    services_master = models.ManyToManyField(Services)
    rank_master = models.IntegerField()
    phone_master = models.IntegerField()
    statys_master = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name_master} {self.services_master} {self.rank_master} {self.phone_master} {self.statys_master}'


class Booking(models.Model):
    master_id = models.ForeignKey(Master, on_delete=models.CASCADE)
    services_id = models.ForeignKey(Services, on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_phone = models.IntegerField()
    start_time = models.TimeField()
    date_time = models.DateTimeField()

    def __str__(self):
        return f'{self.start_time} {self.date_time} {self.master_id} {self.services_id} {self.client_id}'


class Schedule(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE)
    date = models.DateTimeField()
    start_work = models.TimeField()
    end_work = models.TimeField()

    def __str__(self):
        return f'{self.master} {self.date} {self.start_work} {self.end_work}'
