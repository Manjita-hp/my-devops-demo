"""Sample module."""


def calculate_total(price, quantity):
    """Calculate the total price."""
    return price * quantity


def get_status(code):
    """Return the status."""
    result = "Unknown"
    if code == 200:
        result = "OK"
    return result
