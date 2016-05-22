from django.db import models
from datetime import datetime
from django.template.defaultfilters import slugify
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\+?1?\d{9,15}$',
    message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")

PAYMENT_STATUS = (
    ('ONT','on time'),
    ('CMP','completed'),
    ('LAT','late'),
)

CURRENCIES = (
    ('MXN','MXN'),
    ('USD','USD'),
)

class Client(models.Model):
    name = models.CharField(max_length=140)
    compayName = models.CharField(blank=True, default="", max_length=140)
    slug = models.SlugField(editable=False)
    dateCreated = models.DateField(auto_now_add=True)
    dateUpdated = models.DateField(auto_now=True)
    dateAdquired = models.DateField(null=True)
    notes = models.TextField(blank=True)
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Client, self).save(*args, **kwargs)
    def email(self):
        email = Email.objects.filter(client=self).first()
        if email:
            return email
        else:
            return 'No email'
    def phone(self):
        phone = Phone.objects.filter(client=self).first()
        if phone:
            return phone
        else:
            return 'No phone'

class Payment(models.Model):
    client = models.ForeignKey('Client')
    name = models.CharField(max_length=140, default="Payment")
    money  = models.FloatField(default=0)
    currency = models.CharField(choices=CURRENCIES, max_length=3, default='MXN')
    dateCreated = models.DateField(auto_now_add=True)
    dateUpdated = models.DateField(auto_now=True)
    dateExpiration = models.DateField(null=True)
    dateSet = models.DateField(null=True)
    status = models.CharField(choices=PAYMENT_STATUS, max_length=3, default='ONT')
    # def save(self, *args, **kwargs):
        # if(self.dateExpiration < datetime.date(datetime.now())):
        #     self.status = 'LAT'
        # super(Payment, self).save(*args, **kwargs)

    class Meta:
        ordering = ['dateCreated']

    def __str__(self):
        return str(self.money)

class Email(models.Model):
    client = models.ForeignKey('Client')
    name = models.CharField(default="", blank=True, max_length=140)
    email = models.EmailField()
    class Meta:
        ordering = ['email']

    def __str__(self):
        return self.email

class Phone(models.Model):
    client = models.ForeignKey('Client')
    name = models.CharField(default="", blank=True, max_length=140)
    phone = models.CharField(validators=[phone_regex], max_length=140)
    class Meta:
        ordering = ['phone']

    def __str__(self):
        return self.phone
