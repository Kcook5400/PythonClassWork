


def test_average_exception(self):
    with self.assertRaises(ValueError):
        average(-90, 89, 78)