from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Person
from .api import client
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=Person)
def update_person(sender, instance, created, **kwargs):
    if hasattr(instance, '_updating'):
        return
    if instance.public:
        instance._updating = True
        instance.card_item_id = client.create_person(instance)
        instance.save()
        delattr(instance, '_updating')
    elif not instance.public and instance.card_item_id is not None:
        instance._updating = True
        client.delete_person(instance.card_item_id)
        instance.card_item_id = None
        instance.save()
        delattr(instance, '_updating')
