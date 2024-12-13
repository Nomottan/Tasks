import unittest
import module_12_1
import module_12_2

runs = unittest.TestSuite()
runs.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_1.RunnerTest))
runs.addTest(unittest.TestLoader().loadTestsFromTestCase(module_12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runs)