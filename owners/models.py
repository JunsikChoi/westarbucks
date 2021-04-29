from django.db import models


class Owners(models.Model):
    name = models.CharField("owner name", max_length=45)
    email = models.CharField("owner email", max_length=300)
    age = models.IntegerField("owner age")

    def __str__(self):
        return f"{self.id}: name: {self.name} email: {self.email} age: {self.age}"


class Dogs(models.Model):
    owner_id = models.ForeignKey(
        "Owners", verbose_name="owner id", on_delete=models.CASCADE
    )
    name = models.CharField("dog name", max_length=45)
    age = models.IntegerField("dot age")

    def __str__(self):
        return f"{self.id}: name: {self.name} age: {self.age} ownedBy: {self.owner_id}"
