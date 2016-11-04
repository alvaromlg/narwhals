from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings

#Override Django user
from django.db import models

from authemail.models import EmailUserManager, EmailAbstractUser

# Future translation
from django.utils.translation import ugettext_lazy as _

UP = 'up';
DOWN = 'down'
TREND_CHOICES = (
	(UP, 'UP'),
        (DOWN, 'DOWN'),
)

# Trigger to create a token for every user
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)

class User(EmailAbstractUser):

    date_of_birth = models.DateField(null=True)
    
    # Custom fields
    position = models.IntegerField(verbose_name=(_('Ranking position.')),
                                   help_text=_('Ranking position.'),
                                   blank=True, null=True)
    meters = models.IntegerField(verbose_name=(_('Total meters.')),
                                   help_text=_('Total meters.'),
                                   blank=True, default=0)
    minutes = models.IntegerField(verbose_name=(_('Total minutes.')),
                                   help_text=_('Total minutes.'),
                                   blank=True, default=0)
    strokes = models.IntegerField(verbose_name=(_('Total strokes.')),
                                   help_text=_('Total strokes'),
                                   blank=True, default=0)
    metersAverage = models.IntegerField(verbose_name=(_('Meters average.')),
                                   help_text=_('Meters average.'),
                                   blank=True, default=0)
    minutesAverage = models.IntegerField(verbose_name=(_('Minutes average.')),
                                   help_text=_('Minutes average'),
                                   blank=True, default=0)
    city_id = models.IntegerField(verbose_name=(_('??')),
                                   help_text=_('??'),
                                   blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    surname = models.CharField(max_length=100, blank=True, null=True)
    trend = models.CharField(max_length=10, choices=TREND_CHOICES, default=DOWN)
    bio = models.CharField(max_length=500, blank=True, null=True)
    avatar = models.CharField(max_length=100, blank=True, null=True)

    objects = EmailUserManager()

    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['date_of_birth']
