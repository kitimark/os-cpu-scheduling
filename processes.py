import random

class Process(object):
  def __init__(self, pid, exe_time):
    self.pid = None
    self.exe_time = exe_time


class Condition(object):
  def __init__(self, time_range, percent):
    """ Condition of random process
      time_range: tuple range of random time
      percent: percent of set processes
    """
    if len(time_range) != 2:
      raise ValueError('time_range should have 2 numbers')
    if time_range[0] > time_range[1]:
      raise ValueError()
    self.time_range = time_range
    self.percent = percent


class RamdomCondition(object):
  def __init__(self):
    self.random_condition = []

  def add_condition(self, time_range, percent):
    condition = Condition(time_range, percent)
    self.random_condition.append(condition) 

  def __iter__(self):
    percents = map(lambda x: x.percent, self.random_condition)
    if sum(percents) != 100:
      raise ValueError('Condition not complete')
    return iter(self.random_condition)


def process_generate(rand_condition, num_processes):
  """Generate random process list"""

  process_list = []
  for cond in rand_condition:
    count_time = int(cond.percent * num_processes / 100)
    process_list += [random.randint(
        cond.time_range[0], 
        cond.time_range[1])
        for _ in range(count_time)]
  random.shuffle(process_list)

  process_list = [Process(idx, process_time) 
                  for idx, process_time in enumerate(process_list)]

  return process_list
