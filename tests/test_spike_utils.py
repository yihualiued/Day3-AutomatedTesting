import utils
from utils import spike_math

def test_pytest_is_working():
    assert True

def test_count_spikes_3():
    spikes = [1,2,3]
    total = spike_math.count_spikes(spikes)
    assert total == 3

def test_count_spike_0():
    spikes = []
    total = spike_math.count_spikes(spikes)
    assert total == 0

def test_count_spike_tuple():
    spikes = (1,2)
    total = spike_math.count_spikes(spikes)
    assert total == 2

def test_compute_isi_4():
    spikes = [1,2,3,4]
    isis = spike_math.compute_isi(spikes)
    assert isis == [1,1,1]

def test_compute_isi_1():
    spikes = [2]
    isis = spike_math.compute_isi(spikes)
    assert isis == []

def test_compute_isi_0():
    spikes = []
    isis = spike_math.compute_isi(spikes)
    assert isis == []

def test_compute_isi_minus():
    spikes = [-2,-4]
    isis = spike_math.compute_isi(spikes)
    assert isis == [-2]