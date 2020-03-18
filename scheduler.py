
from process import Process
import time

## todo the process only start on the start time
def load_processes(input_file):

    def create_process(line):
        line_split = line.split()
        if len(line_split) < 3:
            print ("invalid input|line={0}".format(line))
            raise ValueError("invalid input")

        pid = int(line_split[0])
        arrival_time = int(line_split[1])
        burst_time = int(line_split[2])
        if len(line_split) >3:
            share = int(line_split[3])
        else:
            share = None

        return Process(pid, arrival_time, burst_time, share)
    processes = []

    try:
        with open(input_file) as fd:
            lines = fd.readlines()
            for line in lines:
                process = create_process(line)
                processes.append(process)
        return processes
    except:
        print "unexpected error"

def write_processes(processes, out_file):
    with open(out_file, "wb") as fd:
        for process in processes:
            line = " ".join(map(str, [process.pid, process.finish_time, process.wait_time, process.turn_around_time]))
            line += "\n"
            fd.write(line)

        wait_time = average_wait_time(processes)
        turnaround_time = average_turnaround_time(processes)
        line = " ".join(map(str, [wait_time, turnaround_time ]))

        fd.write(line)

def run_process(process, run_time, current_time):
    # using sleep to simulate running the thread
    time.sleep(run_time /(1000 + 0.0))
    process.update(run_time, current_time)



class SchedulerEngine():
    def __init__(self, scheduler):
        self.scheduler = scheduler

    def run(self):
        pass

def is_process_done(process):
    return process.execution_time >= process.burst_time

def average_wait_time(processes):
    total = sum([process.wait_time for process in processes])
    return int(round(total/(len(processes) + 0.0)))

def average_turnaround_time(processes):
    total = sum([process.turn_around_time for process in processes])
    return int(round((total/(len(processes) + 0.0))))

class FCFSScheduler():
    def __init__(self, input_file, output_file):
        self.processes = load_processes(input_file)
        self.__sort_by_arrival_time()
        self.output_file = output_file
        self.scheduled_process = []
        self.current_time = 0

    def schedule(self):
        for process in self.processes:
            run_time = process.burst_time
            run_process(process, run_time, self.current_time)
            self.scheduled_process.append(process)
            self.current_time += run_time
            process.close(self.current_time)

        write_processes(self.processes, self.output_file)

    def __sort_by_arrival_time(self):
        self.processes.sort(key = lambda p : p.arrival_time)



class SRTFScheduler():
    def __init__(self, input_file, output_file):
        self.processes = load_processes(input_file)
        self.output_file = output_file
        self.cpu_slot = None ## assume cpu has a fixed slot!!!
        self.scheduled_process = []
    #todo important thing to consider, how to simulate the clock, and then how to execute the program by arrival time?
    def schedule(self,):
        while True:
            if self.__has_next() == False:
                break
            process = self.__next()

            run_process(process, self.cpu_slot)

            if is_process_done(process):
                self.__remove_process(process)
                self.scheduled_process.append(process)
        write_processes(self.scheduled_process, self.output_file)

    def __has_next(self):
        return len(self.processes) >= 0

    def __next(self):
        self.processes.sort(lambda p : p.remain)
        return self.processes[0]

    def __remove_process(self, process ):
        self.processes.remove(process)

class PSScheduler():
    def __init__(self):
        pass

    def schedule(self, input):
        pass