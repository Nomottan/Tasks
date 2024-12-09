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
        for result in self.all_results:
            print(result)

    def TourTest(self):
        tour = testRunner.Tournament(90, (self.runner1, self.runner3))
        tour_result = tour.start()
        new_keys = {len(self.__class__.all_result) + k: v for k, v in tour_result.items()}
        self.__class__.all_results.update(new_keys)
        self.assertTrue(tour_result[max(tour_result.keys())] == self.runner3)
        # tour2 = testRunner.Tournament(90, (self.runner2, self.runner3))
        # tour2_result = tour2.start()
        # new_keys = {len(self.all_result) + k: v for k, v in tour2_result.items()}
        # self.all_results.update(new_keys)
        # self.assertTrue(tour2_result[max(tour2_result.keys())])
        # tour3 = testRunner.Tournament(90, (self.runner1, self.runner2, self.runner3))
        # tour3_result = tour3.start()
        # new_keys = {len(self.all_result) + k: v for k, v in tour3_result.items()}
        # self.all_results.update(new_keys)
        # self.assertTrue(tour_result[max(tour3_result.keys())])


if __name__ == "__main__":
    unittest.main()


