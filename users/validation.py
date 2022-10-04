from wtforms.validators import ValidationError
from flask import request
import re


def character_check(form, field):
    excluded_chars = "<&%"

    for char in field.data:
        if char in excluded_chars:
            raise ValidationError(f"Character {char} is not allowed.")


def validate_number(form, field):
    pattern = re.compile(r"\d")
    if not pattern.search(field.data):
        raise ValidationError(f"Password Must Include at least 1 Number")


def validate_lowercase(form, field):
    pattern = re.compile(r"[a-z]")
    if not pattern.search(field.data):
        raise ValidationError(f"Password Must Include at least 1 Lowercase character")


def validate_password(form, field):
    if field.data != request.form.get('password'):
        raise ValidationError(f"Passwords Must Match")

