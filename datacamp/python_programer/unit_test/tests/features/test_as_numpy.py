import numpy as np
import pytest
from src.features.as_numpy import get_data_as_numpy_array


class TestGetDataAsNumpyArray(object):
    def test_on_clean_file(self):
        expected = np.array([[2081.0, 314942.0],
                             [1059.0, 186606.0],
                             [1148.0, 206186.0]
                             ]
                            )
        actual = get_data_as_numpy_array(
            "example_clean_data.txt", num_columns=2)
        message = "Expected return value: {0}, Actual return value: {1}".format(
            expected, actual)
        assert actual == pytest.approx(expected), message
