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
        tour = testRunner.Tournament(90, (self.runner1, self.runner3))   # создание объекта Tournament
        tourresult = tour.start()                                                           # вызов метода "stаrt" в объекте Tournament
        self.all_results.copy(tourresult)                                                   # сохранение результатов в список
        self.assertTrue(tourresult[2] == "Ник")                                     # проверка результата по ключу в словаре
        tour2 = testRunner.Tournament(90, (self.runner2, self.runner3))
        tourresult1 = tour2.start()
        self.all_results.copy(tourresult1)
        self.assertTrue(tourresult1[2] == "Ник")
        tour3 = testRunner.Tournament(90, (self.runner1, self.runner2, self.runner3))
        tourresult2 = tour3.start()
        self.all_results.copy(tourresult2)
        self.assertTrue(tourresult2[3] == "Ник")


if __name__ == "__main__":
    unittest.main()
