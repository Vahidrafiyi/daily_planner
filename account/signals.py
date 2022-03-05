import datetime

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from account.models import Profile, SalaryReceipt
from account.utils import create_5_digit_random
from eventlog.models import EnterExit


def save_profile_user(sender, **kwargs):
    print(kwargs)
    if kwargs['created']:
        profile_user = Profile.objects.create(user=kwargs['instance'], employee_code=create_5_digit_random(), date_joined=datetime.date.today())
        print(profile_user)
        # profile_user.save()

post_save.connect(save_profile_user, sender=User)

@receiver(post_save, sender= SalaryReceipt)
def paid_salary(sender, created, instance, **kwargs):
    if created:
        EnterExit.objects.filter(user=instance.user, is_paid=False, date__range=[instance.from_date, instance.to_date]).update(is_paid=True)