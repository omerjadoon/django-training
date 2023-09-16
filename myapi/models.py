from django.db import models

class Books(models.Model):
    """Model definition for Books."""

    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    qty = models.CharField(max_length=200)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Books."""

        verbose_name = 'Books'
        verbose_name_plural = 'Bookss'

    def __str__(self):
        """Unicode representation of Books."""
        return self.name + " ,==== " +self.price

   

