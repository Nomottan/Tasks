from test import Runner
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        testwalk = Runner("test")
        for step in range(0, 10):
            testwalk.walk()
        self.assertEqual(testwalk.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        testrun = Runner("test")
        for step in range(0, 10):
            testrun.run()
        self.assertEqual(testrun.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        testrun = Runner("test")
        testwalk = Runner("test")
        for step in range(0, 10):
            testwalk.walk()
            testrun.run()
        self.assertNotEqual(testrun.distance, testwalk.distance)



runtest = RunnerTest()
runtest.test_run()
