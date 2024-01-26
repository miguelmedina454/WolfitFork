import textwrap
from datetime import timedelta, datetime
from app.helpers import pretty_date
from app import db
from app.models import Category, Post, User

def test_yesterday():
    assert (pretty_date(datetime.utcnow() - timedelta(days=1))) == "Yesterday"
