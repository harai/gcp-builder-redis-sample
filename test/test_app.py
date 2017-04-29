import unittest
from unittest import TestCase
from redissample import app


class AppTests(TestCase):

  def test_hello(self):
    self.assertIn('World', app.hello_world())


if __name__ == '__main__':
  unittest.main()
