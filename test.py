import unittest
import processes

class ProcessesTest(unittest.TestCase):

  def test_rand_condition(self):
    
    cond = processes.RamdomCondition()
    cond.add_condition((1, 2), 50)

    with self.assertRaises(ValueError):
      cond.__iter__()

    with self.assertRaises(ValueError):
      cond.add_condition((4, 3), 50)

    cond.add_condition((4, 4), 50)


if __name__ == "__main__":
  unittest.main()