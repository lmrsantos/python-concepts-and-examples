import psutil

# Get the memory usage of the current process
memory_usage = psutil.virtual_memory().percent
print (f'memory usage: {memory_usage}')

# Get the CPU usage of the current process
cpu_usage = psutil.cpu_percent()
print (f'cpu usage: {cpu_usage}')

# Get the elapse time of the current process
elapse_time_user = psutil.Process().cpu_times().user
elapse_time_system = psutil.Process().cpu_times().system
proc_name = psutil.Process().name()
proc_pid = psutil.Process().pid
print (f'elapse time (USER): {elapse_time_user}')
print (f'elapse time (SYSTEM): {elapse_time_system}')
print (f'process pid/name: {proc_pid}/{proc_name}')

# Get a list of the tasks that are running in the system
# tasks = psutil.process_iter()
# tasklist=list(tasks)
# for task in tasklist:
#     print (task)

