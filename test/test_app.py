import unittest
from unittest import TestCase
from redissample import app


class AppTests(TestCase):

  def test_hello(self):
    res = app.hello_world()
    self.assertIn('World', res)
    self.assertIn('/data/redis-server', res)


if __name__ == '__main__':
  unittest.main()
