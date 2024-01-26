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

def test_seconds_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(seconds=10))) == "10 seconds ago"

def test_minutes_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(minutes=1))) == "a minute ago"

def test_many_minutes_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(minutes=10))) == "10 minutes ago"

def test_hours_ago():
    assert (pretty_date(datetime.utcnow() - timedelta(hours=1))) == "an hour ago"