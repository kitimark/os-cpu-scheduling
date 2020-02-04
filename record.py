class ProcessRecord(object):
  def __init__(self, process, waiting_time=0, turnaround_time=0):
    self.pid = process.pid
    self.exe_time = process.exe_time
    self.waiting_time = waiting_time
    self.turnaround_time = turnaround_time
