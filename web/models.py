from django.core import exceptions
from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models


def validate_year(value):
    if value < Car.MIN_VALID_YEAR or value > Car.MAX_VALID_YEAR:
        raise exceptions.ValidationError("Year must be between 1980 and 2049")


class Profile(models.Model):
    MAX_USERNAME_LEN = 10
    MIN_USERNAME_LEN = 2
    MIN_AGE = 18
    MAX_PASS_LEN = 30
    MAX_NAME_LEN = 30

    username = models.CharField(
        max_length=MAX_USERNAME_LEN,
        validators=(
            MinLengthValidator(
                MIN_USERNAME_LEN,
                message="The username must be a minimum of 2 chars"),
        ),
        null=False,
        blank=False,
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.IntegerField(
        validators=(
            MinValueValidator(MIN_AGE),
        ),
        null=False,
        blank=False,
    )

    password = models.CharField(
        max_length=MAX_PASS_LEN,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_NAME_LEN,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_NAME_LEN,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=True,
    )


class Car(models.Model):
    MAX_TYPE_LEN = 10
    MAX_MODEL_LEN = 20
    MIN_MODEL_LEN = 2
    MIN_VALID_YEAR = 1980
    MAX_VALID_YEAR = 2049
    MIN_PRICE = 1
    CAR_CHOICES = (
        ("Sports Car", "Sports Car"),
        ("Pickup", "Pickup"),
        ("Crossover", "Crossover"),
        ("Minibus", "Minibus"),
        ("Other", "Other")
    )

    type = models.CharField(
        max_length=MAX_TYPE_LEN,
        choices=CAR_CHOICES,
        null=False,
        blank=False,
    )

    model = models.CharField(
        max_length=MAX_MODEL_LEN,
        validators=(
            MinLengthValidator(MIN_MODEL_LEN),
        ),
        null=False,
        blank=False,
    )

    year = models.IntegerField(
        validators=(
            validate_year,
        ),
        null=False,
        blank=False,
    )

    image_url = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        validators=(
            MinValueValidator(MIN_PRICE),
        ),
        null=False,
        blank=False,
    )



