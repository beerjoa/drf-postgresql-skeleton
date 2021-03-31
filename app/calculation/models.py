from django.db.models import IntegerField, CharField
from main.models import Base


class Calculation(Base):
    SYMBOL = (
        ("+", "Addition"),
        ("-", "Subtraction"),
        ("*", "Multiplication"),
        ("/", "Division"),
        ("%", "Modulus"),
        ("**", "Exponentiation"),
        ("//", "Floor division"),
    )
    num1 = IntegerField()
    num2 = IntegerField()
    symbol = CharField(max_length=2, choices=SYMBOL)
    result = CharField(max_length=100000)
