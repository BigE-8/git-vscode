from average_mean import my_mean
import pytest

prompt = "2,4,6,8,9,10"
def test_mean():
    assert my_mean(prompt) == 6.5