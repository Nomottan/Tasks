import testRunner
import unittest


class TournamentTest(unittest.TestCase):
    def setUp(self):
        self.runner1 = testRunner.Runner("Усейн", 10)
        self.runner2 = testRunner.Runner("Андрей", 9)
        self.runner3 = testRunner.Runner("Ник", 3)

    @classmethod
    def setUpClass(self):
        self.all_results = {}

    @classmethod
    def tearDownClass(self):
        for k, v in self.all_results.items():
            print(f"{k}: {str(v)}")

    def test_Tour(self):
        tour = testRunner.Tournament(90, self.runner1, self.runner3)
        tour_result = tour.start()
        new_keys = {len(self.__class__.all_results) + k: v for k, v in tour_result.items()}
        self.__class__.all_results.update(new_keys)
        print(self.__class__.all_results)
        self.assertTrue(tour_result[max(tour_result.keys())] == self.runner3)

    def test_Tour2(self):
        tour = testRunner.Tournament(90, self.runner2, self.runner3)
        tour_result = tour.start()
        new_keys = {len(self.__class__.all_results) + k: v for k, v in tour_result.items()}
        self.__class__.all_results.update(new_keys)
        print(self.__class__.all_results)
        self.assertTrue(tour_result[max(tour_result.keys())] == self.runner3)

    def test_Tour3(self):
        tour = testRunner.Tournament(90, self.runner1, self.runner2, self.runner3)
        tour_result = tour.start()
        new_keys = {len(self.__class__.all_results) + k: v for k, v in tour_result.items()}
        self.__class__.all_results.update(new_keys)
        print(self.__class__.all_results)
        self.assertTrue(tour_result[max(tour_result.keys())] == self.runner3)

if __name__ == "__main__":
    unittest.main()

