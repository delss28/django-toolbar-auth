from django.db import models
from django.contrib.auth.models import AbstractUser


from main.models import Service

# Create your models here.

class User(AbstractUser):
    patronymic = models.CharField(max_length=50, blank=True, null=True)
    dateOfBirth = models.DateField(blank=True, null=True)
    number = models.CharField(max_length=30,blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars_images', blank=True, null=True)

    class Meta:
        db_table = 'user'
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

    def __str__(self):
        return self.username
    

class Appointment(models.Model):
    id_service = models.ForeignKey(Service,
                                   related_name='id_services',
                                   on_delete=models.CASCADE, null=True)
    id_user = models.ForeignKey(User,
                                    related_name='id_users',
                                    on_delete=models.CASCADE, null=False)
    appointment_date = models.DateField(blank=True, null=True)
    appointment_time = models.TimeField(blank=True, null=True)

    process = "В обрaботке"
    confirmed = "Подтвержден"
    deleted = "Отменен"
    status_choices = [
        (process, "В обработке"),
        (confirmed, "Подтвержден"),
        (deleted, "Отменен"),
    ]
        

    status = models.CharField(
        max_length=12, 
        choices=status_choices, 
        default=process,)


    class Meta:
        verbose_name = 'Прием'
        verbose_name_plural = 'Приемы'

    def is_upperclass(self):
        return self.status in {self.confirmed, self.deleted}
    
    def __str__(self):
        return f"Прием {self.id_user} на {self.appointment_date} в {self.appointment_time} - {self.id_service} | Статус: {self.status}"