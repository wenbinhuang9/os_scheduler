import unittest


from scheduler import FCFSScheduler
class MyTestCase(unittest.TestCase):
    def test_FCFS(self):
        input_file = "./tests/fcfs4.input"
        out_file = "./tests/fcfs4.output"

        scheduler = FCFSScheduler(input_file, out_file)
        scheduler.schedule()

if __name__ == '__main__':
    unittest.main()
