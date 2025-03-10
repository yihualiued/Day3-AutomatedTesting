from utils.spike_math import compute_isi

def test_compute_isi_4():
    observed = compute_isi([3, 4, 5, 6])
    expected = [1, 1, 1]
    assert observed == expected

def test_compute_isi_order():
    observed = compute_isi([3, 1, 5])

