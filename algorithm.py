def FCFS(process_list):
  """First come first search"""

  history = [0]
  for process in process_list:
    used_time = history[-1] + process.exe_time
    history.append(used_time)

  return history

  
def SJF(process_list):
  # priority of this algorithm is time of process
  sorted_processes = sorted(process_list, key=lambda x: x.exe_time)

  history = [0]
  for process in sorted_processes:
    used_time = history[-1] + process.exe_time
    history.append(used_time)

  return history


def RR(process_list, quantum_time=10):
  process_queue = process_list.copy()
  history = [0]
  for process in process_queue:
    if process.exe_time <= quantum_time:
      use_time = history[-1] + process.exe_time
      history.append(use_time)
    else:
      time_process_left = process.exe_time - quantum_time
      process.exe_time = time_process_left
      # Push same process in queue
      process_queue.append(process)
      use_time = history[-1] + quantum_time
      history.append(use_time)

  return history
