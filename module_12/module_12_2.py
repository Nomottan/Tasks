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
            print(f"{str(v)}")

    def test_Tour(self):
        tour = testRunner.Tournament(90, self.runner1, self.runner3)
        tour_result = tour.start()
        for k, v in tour_result.items():
            tour_result[k] = str(v)
        self.__class__.all_results[0]=(tour_result)
        self.assertTrue(tour_result[max(tour_result.keys())] == self.runner3)

    def test_Tour2(self):
        tour = testRunner.Tournament(90, self.runner2, self.runner3)
        tour_result = tour.start()
        for k, v in tour_result.items():
            tour_result[k] = str(v)
        self.__class__.all_results[1]=(tour_result)
        self.assertTrue(tour_result[max(tour_result.keys())] == self.runner3)

    def test_Tour3(self):
        tour = testRunner.Tournament(90, self.runner1, self.runner2, self.runner3)
        tour_result = tour.start()
        for k, v in tour_result.items():
            tour_result[k] = str(v)
        self.__class__.all_results[2]=(tour_result)
        self.assertTrue(tour_result[max(tour_result.keys())] == self.runner3)

if __name__ == "__main__":
    unittest.main()


