from testRunner import Runner, Tournament
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


class TournamentTest(unittest.TestCase):
    is_frozen = True
    def setUp(self):
        self.runner1 = Runner("Усейн", 10)
        self.runner2 = Runner("Андрей", 9)
        self.runner3 = Runner("Ник", 3)

    @classmethod
    def setUpClass(self):
        self.all_results = {}

    @classmethod
    def tearDownClass(self):
        for k, v in self.all_results.items():
            print(f"{k}: {str(v)}")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tour(self):
        tour = Tournament(90, self.runner1, self.runner3)
        tour_result = tour.start()
        new_keys = {len(self.__class__.all_results) + k: v for k, v in tour_result.items()}
        self.__class__.all_results.update(new_keys)
        self.assertTrue(tour_result[max(tour_result.keys())] == self.runner3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tour2(self):
        tour = Tournament(90, self.runner2, self.runner3)
        tour_result = tour.start()
        new_keys = {len(self.__class__.all_results) + k: v for k, v in tour_result.items()}
        self.__class__.all_results.update(new_keys)
        self.assertTrue(tour_result[max(tour_result.keys())] == self.runner3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_Tour3(self):
        tour = Tournament(90, self.runner1, self.runner2, self.runner3)
        tour_result = tour.start()
        new_keys = {len(self.__class__.all_results) + k: v for k, v in tour_result.items()}
        self.__class__.all_results.update(new_keys)
        self.assertTrue(tour_result[max(tour_result.keys())] == self.runner3)

if __name__ == "__main__":
    unittest.main()
