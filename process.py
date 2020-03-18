

class Process():
    def __init__(self, pid, arrival_time, burst_time, share):
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.share = share
        self.finish_time = 0
        self.wait_time = 0
        self.execution_time = 0
        self.remain = 0
        self.last_executed_time = None
        self.turn_around_time = 0

    def update(self, run_time, current_time):

        self.execution_time += run_time
        self.remain = self.burst_time - self.execution_time
        self.__cal_wait_time(current_time)
        self.last_executed_time = current_time

    def __cal_wait_time(self, current_time):
        if self.last_executed_time == None:
            # first time to execute
            self.wait_time += 0 if (current_time - self.arrival_time) <= 0 else (current_time - self.arrival_time)
        else:
            self.wait_time += (current_time - self.last_executed_time)

    def close(self, current_time):
        self.finish_time = current_time
        self.turn_around_time = self.execution_time + self.wait_time

