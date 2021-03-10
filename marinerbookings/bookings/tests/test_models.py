import pytest
pytestmark = pytest.mark.django_db

from ..models import Guest
from .factories import GuestFactory

def test___str__():
    guest = GuestFactory()
    assert guest.__str__() == "guest.guest_first_name"
    assert str(guest) == "guest.guest_first_name"
