from django.db import models
from django.forms.models import model_to_dict


class Owners(models.Model):
    name = models.CharField("owner name", max_length=45)
    email = models.CharField("owner email", max_length=300)
    age = models.IntegerField("owner age")

    def __repr__(self):
        return {"id": self.id, "name": self.name, "email": self.email, "age": self.age}

    def __str__(self):
        return f"ID: {self.id} name: {self.name} email: {self.email} age: {self.age}"

    def to_dict(self):
        return model_to_dict(self)


class Dogs(models.Model):
    owner = models.ForeignKey(
        "Owners", verbose_name="owner id", on_delete=models.CASCADE
    )
    name = models.CharField("dog name", max_length=45)
    age = models.IntegerField("dot age")

    def __str__(self):
        return f"{self.id}: name: {self.name} age: {self.age} ownedBy: {self.owner_id}"

    def to_dict(self):
        dog_info = model_to_dict(self)
        dog_info.update(owner=self.owner.to_dict())
        return dog_info