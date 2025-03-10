from utils import count_spikes

def test_count_spikes_3():
    count = count_spikes([1,2,3])
    assert count == 3

def test_count_spikes_0():
    count = count_spikes([])
    assert count == 0

def test_count_spikes_tuple():
    count = count_spikes((3, 4, 5, 6))
    assert count == 4