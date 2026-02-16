import unittest

from television_system.television import TelevisionSystem


class TestTelevisionSystem(unittest.TestCase):
    def setUp(self):
        self.tv = TelevisionSystem()

    def test_that_television_is_off_at_initial(self):
        self.assertFalse(self.tv.is_on())

    def test_that_television_can_power_on(self):
        self.assertFalse(self.tv.is_on())

        self.tv.power_on()
        self.assertTrue(self.tv.is_on())

    def test_that_television_power_control_works(self):
        self.assertFalse(self.tv.is_on())

        self.tv.power_on()
        self.assertTrue(self.tv.is_on())
        self.tv.power_off()
        self.assertFalse(self.tv.is_on())

    def test_that_increase_volume_button_works(self):
        self.assertFalse(self.tv.is_on())

        self.tv.power_on()
        self.assertTrue(self.tv.is_on())

        initial_volume = self.tv.get_volume()
        self.tv.volume_up()
        self.assertEqual(initial_volume + 1, self.tv.get_volume())

    def test_that_volume_does_not_exceed_maximum(self):
        self.assertFalse(self.tv.is_on())

        self.tv.power_on()
        self.assertTrue(self.tv.is_on())

        for count in range(100):
            self.tv.volume_up()

        self.assertEqual(30, self.tv.get_volume())

    def test_that_decrease_volume_button_works(self):
        self.assertFalse(self.tv.is_on())

        self.tv.power_on()
        self.assertTrue(self.tv.is_on())

        initial_volume = self.tv.get_volume()
        self.tv.volume_down()
        self.assertEqual(initial_volume - 1, self.tv.get_volume())

    def test_that_volume_does_not_go_below_minimum(self):
        self.assertFalse(self.tv.is_on())

        self.tv.power_on()
        self.assertTrue(self.tv.is_on())

        for count in range(100):
            self.tv.volume_down()

        self.assertEqual(0, self.tv.get_volume())

    def test_that_channel_change_buttons_works(self):
        self.assertFalse(self.tv.is_on())

        self.tv.power_on()
        self.assertTrue(self.tv.is_on())

        self.tv.set_channel(10)
        self.assertEqual(10, self.tv.get_channel())