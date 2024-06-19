from django.db.models.signals import post_save, post_delete
from django.db.models import Sum
from django.dispatch import receiver
from cars.models import Car, CarInventory


def car_inventory_update():
    qtd_cars = Car.objects.all().count()
    value_inventory = Car.objects.aggregate(
        total_value=Sum('value')
    )['total_value']

    CarInventory.objects.create(
        cars_count=qtd_cars,
        cars_value=value_inventory
    )


@receiver(post_save, sender=Car)
def car_post_save(sender, instance, **kwargs):
    car_inventory_update()


@receiver(post_delete, sender=Car)
def car_post_delete(sender, instance, **kwargs):
    car_inventory_update()
