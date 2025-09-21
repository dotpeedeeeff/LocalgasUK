import unittest
import postcode as pc


class TestStripperFunction(unittest.TestCase):
    def test_standard_postcodes(self):
        self.assertEqual(pc.space_stripper("PL12 1BN"), "PL121BN")
        self.assertEqual(pc.space_stripper("S4 6KX"), "S46KX")
        self.assertEqual(pc.space_stripper("W1F 3WX"), "W1F3WX")
        self.assertEqual(pc.space_stripper("HZ1R 9VN"), "HZ1R9VN")

    def test_mixed_capitals(self):
        self.assertEqual(pc.space_stripper("b1 9LC"), "B19LC")
        self.assertEqual(pc.space_stripper("Rt1 6cC"), "RT16CC")
        self.assertEqual(pc.space_stripper("tr23 0tz"), "TR230TZ")


class TestOutgoingFunction(unittest.TestCase):
    def test_outgoing_extraction(self):
        self.assertEqual(pc.extract_outer("PL12 1BN"), "PL12")
        self.assertEqual(pc.extract_outer("S4 6KX"), "S4")
        self.assertEqual(pc.extract_outer("W1F 3WX"), "W1F")
        self.assertEqual(pc.extract_outer("HZ1R 9VN"), "HZ1R")


class TestIncomingFunction(unittest.TestCase):
    def test_incoming_extraction(self):
        self.assertEqual(pc.extract_inner("PL12 1BN"), "1BN")
        self.assertEqual(pc.extract_inner("S4 6KX"), "6KX")
        self.assertEqual(pc.extract_inner("W1F 3WX"), "3WX")
        self.assertEqual(pc.extract_inner("HZ1R 9VN"), "9VN")


if __name__ == "__main__":
    unittest.main()
