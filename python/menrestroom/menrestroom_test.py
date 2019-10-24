import unittest
from unittest.mock import patch

import random

import menrestroom


class MenpeeingTest(unittest.TestCase):
  '''  @mock.patch(random.radint)
    @mock.patch(menrestroom.take_stall)
    @mock.patch(menrestroom.take_stall)
    def test_constructor(self, mockrandom, take_stall_mocked, take_stall_mocked):
        mockrandom.return_value = 1
        take_stall_mocked.return_value=
        a = menrestroom.Menpeeing()
        assert(True)
        '''

  @patch('menrestroom.leave_stall', create= True)
  def test_meenpeing_zero_stall(self, leaving_mock):
      leaving_mock.return_value((0, 0, None))
      try:
         peeing = menrestroom.Menpeeing(0, 0)
         assert(True)
      except Exception as ZeroDivisionError:
          assert(False)

  @patch('menrestroom.leave_stall', create=True)
  def test_meenpeing_zero_timer(self, leaving_mock):
    leaving_mock.return_value((0, 0, None))
    try:
        peeing = menrestroom.Menpeeing(1, 0, 1, 1)
        assert (True)
    except Exception as ZeroDivisionError:
        assert(False)

    '''obtained_value= peeing.take_stall()
      assert(obtained_value == (1, 1, 1), obtained_value)
'''
if __name__ == "'__main__":
    unittest.main()
