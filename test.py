import unittest
import fake_eeid
import weights

class MyTest(unittest.TestCase):

    # Test data
#    sex_century = 3
#    year        = 76
#    month       = 5
#    date        = 3
#    serial      = 29
    # control     = 9

    def test_control_calcuration_g1_number(self):
        self.assertEqual(fake_eeid.calc_control('3760503029',weights.g1_weight), 9)

    def test_control_calcuration_g2_number_g1_calculation(self):
        self.assertEqual(fake_eeid.calc_control('4940313656',weights.g1_weight), 10)

    def test_control_calcuration_g2_number_g2_calculation(self):
        self.assertEqual(fake_eeid.calc_control('4940313656',weights.g2_weight), 4)


    def test_grade1_01(self):
         self.assertEqual(fake_eeid.control('3760503029'),(9,1))
    
    def test_grade2_01(self):
         self.assertEqual(fake_eeid.control('4940313656'),(4,2))
    
    def test_grade1_02(self):
         self.assertEqual(fake_eeid.control('5711030188'),(0,1))

if __name__ == "__main__":
    unittest.main()
