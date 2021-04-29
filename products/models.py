from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        verbose_name_plural = "Menus"

    def __str__(self):
        return f"{self.id} {self.name}"


class Category(models.Model):
    menu = models.ForeignKey("Menu", on_delete=models.CASCADE)
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return f"{self.id} {self.name}"


class Allegy(models.Model):
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        verbose_name_plural = "Allegies"

    def __str__(self):
        return f"{self.id} {self.name}"


class Nutrition(models.Model):
    one_serving_kcal = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Calories per serving (kcal)",
        null=True,
    )
    sodium_mg = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Sodium contents per serving (mg)",
        null=True,
    )
    saturated_fat_g = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Saturated fat contents per serving(g)",
        null=True,
    )
    sugars_g = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Sugar contents per serving (g)",
        null=True,
    )
    protein_g = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Protein contents per serving (g)",
        null=True,
    )
    caffeine_mg = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Caffeine contents per sercing (mg)",
        null=True,
    )
    size_ml = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Size per serving (ml)",
        null=True,
    )
    size_ounce = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        verbose_name="Size per serving (oz)",
        null=True,
    )

    class Meta:
        verbose_name_plural = "Nutritions"

    def __str__(self):
        return f"{self.id} \n Calories per serving (kcal): {self.one_serving_kcal} \n Sodium contents per serving (mg): {self.sodium_mg} \n Saturated fat contents per serving(g): {self.saturated_fat_g} \n Sugar contents per serving (g): {self.sugars_g} \n Protein contents per serving (g): {self.protein_g} \n Caffeine contents per sercing (mg): {self.caffeine_mg} \n Size per serving (ml): {self.size_ml} \n Size per serving (oz): {self.size_ounce} \n"


class Product(models.Model):
    # TODO: Foreign Key
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    nutrition = models.ForeignKey("Nutrition", on_delete=models.CASCADE)
    allegies = models.ManyToManyField("Allegy", blank=True, through="ProductAllegy")
    korean_name = models.CharField(max_length=45)
    english_name = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name_plural = "Products"

    def __str__(self):
        return f"{self.id} {self.english_name}"


class ProductAllegy(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    allegy = models.ForeignKey("Allegy", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "ProductAllegies"

    def __str__(self):
        return f"{self.id} Product: {self.product} Allegy: {self.allegy}"


class Image(models.Model):
    image_url = models.CharField(max_length=2000)
    drink = models.ForeignKey("Product", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Images"

    def __str__(self):
        return f"{self.id} {self.image_url}"
