from django.db import models

# Create your models here.
class Pizza(models.Model):
    """The pizza names"""
    name = models.CharField(max_length=250, unique=True)
    date_added = models.DateTimeField(auto_now_add=True)
    

    class Meta:
        # verbose_name = _("")
        verbose_name_plural = 'pizzaz'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("_detail", kwargs={"pk": self.pk})


class Topping(models.Model):
    """Toppings go here"""
    pizza = models.ForeignKey(Pizza, on_delete=models.CASCADE)
    name = models.CharField(max_length=150)
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta:
        # verbose_name = _("topping")
        verbose_name_plural = 'toppings'
        constraints = [models.UniqueConstraint(fields=['pizza', 'name'], name='unique_topping')]

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("topping_detail", kwargs={"pk": self.pk})
