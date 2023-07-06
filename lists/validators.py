from datetime import datetime
from django.core.exceptions import ValidationError


def validate_event_date(date):
    if date < datetime.now().date():
        raise ValidationError("Date cannot be in the past")
