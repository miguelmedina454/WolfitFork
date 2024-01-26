import textwrap
from datetime import timedelta, datetime
from app.helpers import pretty_date
from app import db
from app.models import Category, Post, User

def test_yesterday():
    assert (pretty_date(datetime.utcnow() - timedelta(days=1))) == "Yesterday"

def test_today_just_now():
    assert (pretty_date(datetime.utcnow())) ==  "just now"

def test_days_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(days=5))) == "5 days ago"

def test_weeks_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(days=14))) == "2 weeks ago"

def test_months_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(days=60))) == "2 months ago"

def test_years_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(days=380))) == "1 years ago"