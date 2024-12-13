import unittest
from testRunnerext import Runner
import logging

logging.basicConfig(level=logging.INFO, filemode="w", filename="runner_tests.log",
                    encoding='UTF-8', format="%(levelname)s | %(message)s")

class RunnerTest(unittest.TestCase):

    def test_walk(self):
        try:
            testwalk = Runner("test", -5)
        except ValueError as verr:
            logging.warning('ValueError', exc_info=True)
            return
        for step in range(0, 10):
            testwalk.walk()
        self.assertEqual(testwalk.distance, 50)
        logging.info('"test_walk" выполнен успешно')


    try:
        def test_run(self):
            testrun = Runner("test")
            for step in range(0, 10):
                testrun.run()
            self.assertEqual(testrun.distance, 100)
            logging.info('"test_run" выполнен успешно')
    except TypeError as terr:
        logging.warning('TypeError', exc_info=True)



runtest = RunnerTest()
runtest.test_run()
