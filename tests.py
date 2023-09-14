import unittest

from main import get_order_amount


class TestDogFoodOrderCalculator(unittest.TestCase):
    # the example case provided with the requirements
    def test_all_sizes(self):
        dogs = {
            'small': 3,
            'medium': 1,
            'large': 4,
        }
        remaining_amount = 15
        estimate = get_order_amount(dogs, remaining_amount)
        self.assertEqual(estimate, 186)

    def test_only_small(self):
        dogs = {
            'small': 3,
            'medium': 0,
            'large': 0,
        }
        remaining_amount = 15
        estimate = get_order_amount(dogs, remaining_amount)
        self.assertEqual(estimate, 18)

    def test_only_medium_missing_keys(self):
        dogs = {
            'medium': 5,
        }
        remaining_amount = 15
        estimate = get_order_amount(dogs, remaining_amount)
        self.assertEqual(estimate, 102)

    def test_no_dogs(self):
        dogs = {}
        remaining_amount = 15
        estimate = get_order_amount(dogs, remaining_amount)
        self.assertEqual(estimate, 0)

    def test_unknown_dog_size(self):
        dogs = {
            'chihuahua': 12,
        }
        remaining_amount = 15
        with self.assertRaises(Exception) as context:
            get_order_amount(dogs, remaining_amount)
            self.assertTrue('Unknown dog type found' in str(context.exception))

    def test_known_and_unknown_dog_sizes(self):
        dogs = {
            'small': 3,
            'medium': 4,
            'large': 5,
            'chihuahua': 12,
        }
        remaining_amount = 15
        with self.assertRaises(Exception) as context:
            get_order_amount(dogs, remaining_amount)
            self.assertTrue('Unknown dog type found' in str(context.exception))

    def test_custom_dog_sizes(self):
        custom_dog_sizes = {
            'chihuahua': 1,
            'corgi': 20,
            'beligian mallanois': 100,
        }
        dogs = {
            'chihuahua': 4,
            'corgi': 2,
            'beligian mallanois': 3,
        }
        remaining_amount = 15
        estimate = get_order_amount(dogs, remaining_amount, custom_dog_sizes)
        self.assertEqual(estimate, 395)


if __name__ == '__main__':
    unittest.main()
