# os_scheduler
operating system scheduler algorithm implementation

# Input File Format

Input file is a text file that has all the necessary details of the schedulable processes.
Each line will represent a unique process in the following format:
```
<process-id> <arrival-time> <burst-time> <share>
```

- <process-id>: Unique, unsigned long, 2^63-1 maximum, that represents a process.
- <arrival-time>: Time when a process arrives, an unsigned integer.
- <burst-time>: CPU execution time, an integer number (0, 100]. This is the total time the process would spend running on CPU.
- <share>: An integer number (0, 100]. This will only be present in input files for the PS scheduler.

# Output File Format


Output file will record the results of your simulation. Each line will represent all necessary scheduler information for a unique process in the following format:

```
<process-id> <finish-time> <wait-time> <turnaround-time>
```
* ```<process-id>```: Unique id read from input file. File should be sorted in increasing order of ```<process-id>```s.
* ```<finish-time>```: The time when the process finishes.
* ```<wait-time>```: The total amount of time the process spends waiting in the ready queue.
* ```<turnaround-time>```: The period from when the process enters the system to when the process completes execution.

Lines should be ordered from least to greatest process identifier.

Last line of the output file should contain:

```
<average-wait-time> <average-turnaround-time>
```

where you average the wait-time and turnaround-time of all processes. Note that this value should be rounded using `Math.round()` function in Java.

A single whitespace character should separate items in each line.

Each test must finish within **2.1 seconds**. After that time, timeout will occur and that test will be assumed to have failed.