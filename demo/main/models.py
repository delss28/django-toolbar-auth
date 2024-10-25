from django.db import models


class Doctor(models.Model):
    full_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    job_title = models.CharField(max_length=50)
    work_experience = models.IntegerField()
    phone = models.CharField(max_length=30)
    mail = models.CharField(max_length=50)
    room_number = models.IntegerField()
    salary = models.DecimalField(max_digits=10,
                                 decimal_places=2)

    class Meta:
        verbose_name = 'Доктор'
        verbose_name_plural = 'Доктора'

    def __str__(self):
        return self.full_name


class Service(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    id_doctor = models.ForeignKey(Doctor,
                                  related_name='id_doctors',
                                  on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=10, decimal_places=2)
    slug = models.SlugField(max_length=200,unique=True, blank=True, null=True)
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ("id",)

    def __str__(self):
        return self.title
