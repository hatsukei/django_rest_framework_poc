from django.db import models

# Arrays for database models
OS_CHOICES = (
    ("WINDOWS", "Windows"),
    ("MACINTOSH", "MAC"),
    ("LINUS", "Linux"),
)
STATUS_CHOICES = (
    ("ONLINE", "Online"),
    ("OFFLINE", "Offline"),
)

# Models for database
# items names based on a quick search on server infos.(just some of them for POC purpose)
class ServerInvent(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    server_name = models.CharField(max_length=100, blank=True, default='')
    domain_name = models.CharField(max_length=100, blank=True, default='')
    ip_address = models.CharField(max_length=100, default='0.0.0.0')
    location = models.CharField(max_length=100, blank=False, default='Montreal')
    operating_system = models.CharField(choices=OS_CHOICES, default='WINDOWS', max_length=10)
    status = models.CharField(choices=STATUS_CHOICES, default='ONLINE', max_length=10)
    owner = models.ForeignKey('auth.User', related_name='serverinvent', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)