from django.db import models

from django.conf import settings

from conf.models import TimestampModel


class ProductModel(TimestampModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=120)
    handle = models.SlugField(unique=True)
    # In inventory management, a stock keeping unit is the unit of measure in which
    # the stocks of a material are managed.
    sku = models.IntegerField(default=0)  # Quantity
    price = models.DecimalField(
        default=0,
        decimal_places=2,
        max_length=10,
        max_digits=9,
    )  # may be can be customizable instead of 0, users can assign the default value as their wish
    description = models.TextField()

    # the investment price to calculate the revenue
    # buying_price = models.DeciamlField(default=0, max_length=10, max_digits=9)
    on_sale = models.BooleanField(default=False)
    sale_percentage = models.IntegerField(default=5)
    sale_price = models.DecimalField(default=0, max_length=10, max_digits=9, decimal_places=2)
    sale_created_at = models.DateTimeField(auto_now_add=True)
    sale_starts_at = models.DateTimeField(blank=True, null=True)
    sale_ends_at = models.DateTimeField(blank=True, null=True)

    # law violence, sexual harassment, forgery, man-in-the-middle, fake, name-it
    VIOLENCE_OPTIONS = [
        ('n', 'None'),
        ('l', 'Law'),
        ('s', 'Sexual'),
        ('f', 'Forgery'),
        ('m', 'Man-in-the-middle'),
        ('r', 'Replicate'),
        ('c', 'Custom')
    ]
    report = models.CharField(max_length=20, choices=VIOLENCE_OPTIONS, default=VIOLENCE_OPTIONS[0])

    def save(self, *args, **kwargs):
        # How could I calculate the new price tag when the product is on sale.
        if self.on_sale:
            self.price = self.price * self.sale_percentage / 100
        pass
