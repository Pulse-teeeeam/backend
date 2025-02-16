from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Person
from .api import client



# @receiver(post_save, sender=Person)
# def update_person(sender, instance, **kwargs):
#     if instance.public:
#         person = Person.objects.get(id=instance.id)
#         person.card_item_id = client.create_person(instance)
#         person.save()
