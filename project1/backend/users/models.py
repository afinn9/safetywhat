from django.db import models

class NavbarContent(models.Model):
    name=models.CharField(max_length=100,unique=True)

    def __str__(self) -> str:
        return self.name