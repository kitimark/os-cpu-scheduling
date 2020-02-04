import record

def _create_record(process_list):
  """Pid must staring at 0"""
  return [record.ProcessRecord(process) for process in process_list]

def FCFS(process_list):
  """First come first search"""

  history = [0]
  record = _create_record(process_list)

  for process in process_list:
    used_time = history[-1] + process.exe_time
    record[process.pid].waiting_time = history[-1]
    record[process.pid].turnaround_time = used_time
    history.append(used_time)

  return history, record

  
def SJF(process_list):

  record = _create_record(process_list)

  # priority of this algorithm is time of process
  sorted_processes = sorted(process_list, key=lambda x: x.exe_time)

  history = [0]
  for process in sorted_processes:
    used_time = history[-1] + process.exe_time
    record[process.pid].waiting_time = history[-1]
    record[process.pid].turnaround_time = used_time
    history.append(used_time)

  return history, record


def RR(process_list, quantum_time=10):
  record = _create_record(process_list)
  process_queue = process_list.copy()
  history = [0]

  for process in process_queue:
    if process.exe_time_left <= quantum_time:
      use_time = history[-1] + process.exe_time_left
      record[process.pid].waiting_time = history[-1] - process.exe_time + process.exe_time_left
      record[process.pid].turnaround_time = use_time
      history.append(use_time)
    else:
      time_process_left = process.exe_time_left - quantum_time
      process.exe_time_left = time_process_left
      # Push same process in queue
      process_queue.append(process)
      use_time = history[-1] + quantum_time
      history.append(use_time)

  return history, record
