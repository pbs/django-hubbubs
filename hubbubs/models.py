from .abstract import AbstractSubscription
from django.core.urlresolvers import reverse


class Subscription(AbstractSubscription):

    class Meta:
        app_label = 'hubbubs'

    @property
    def callback_url(self):
        return reverse('hubbubs_callback', args=[self.id, ])

