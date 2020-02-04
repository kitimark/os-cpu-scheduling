class ProcessRecord(object):
  def __init__(self, pid, waiting_time=0, turnaround_time=0):
    self.pid = pid
    self.waiting_time = waiting_time
    self.turnaround_time = turnaround_time
