import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Device, Part


class DeviceModelTests(TestCase):
    def test_true_is_true(self):
        """ Tests if True is equal to True. Should always pass. """
        self.assertEqual(True, True)

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for devices whose created date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_device = Device(created=time)
        self.assertIs(future_device.was_published_recently(), False)
    
    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for devices whose created date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_device = Device(created=time)
        self.assertIs(old_device.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for devices whose created date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_device = Device(created=time)
        self.assertIs(recent_device.was_published_recently(), True)    


############### PART Tests ###############
class PartModelTests(TestCase):

    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for parts whose created date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_part = Part(created=time)
        self.assertIs(future_part.was_published_recently(), False)

    def test_was_published_recently_with_old_question(self):
        """
        was_published_recently() returns False for parts whose created date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_part = Part(created=time)
        self.assertIs(old_part.was_published_recently(), False)

    def test_was_published_recently_with_recent_question(self):
        """
        was_published_recently() returns True for parts whose created date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_part = Part(created=time)
        self.assertIs(recent_part.was_published_recently(), True)