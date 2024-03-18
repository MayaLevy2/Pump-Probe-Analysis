import unittest
import numpy as np
from Fitting_Functions import lorentzian, fluorescence


# Test Lorentzian at center peak
def test_lorentzian_center_peak():
    x0, a, gam, y0 = 0, 1, 1, 0
    expected_result = a + y0
    assert lorentzian(x0, a, x0, gam, y0) == expected_result, "Lorentzian function failed at center peak test."

# Test Lorentzian symmetry
def test_lorentzian_symmetry():
    x0, a, gam, y0 = 0, 1, 1, 0
    x1, x2 = x0 - 2, x0 + 2
    result1, result2 = lorentzian(x1, a, x0, gam, y0), lorentzian(x2, a, x0, gam, y0)
    assert np.isclose(result1, result2), "Lorentzian function failed symmetry test."

# Test Lorentzian with y-offset
def test_lorentzian_offset():
    x, x0, a, gam, y0 = 10, 0, 1, 1, 5
    expected_result = lorentzian(x, a, x0, gam, 0) + y0
    assert lorentzian(x, a, x0, gam, y0) == expected_result, "Lorentzian function failed y-offset test."

# Test fluorescence initial intensity
def test_fluorescence_initial_intensity():
    I_null, a1, tau1, a2, tau2, y0 = 1, 0.5, 1, 0.5, 2, 10
    time_zero = 0
    expected_result = I_null * (a1 + a2) + y0
    assert fluorescence(time_zero, I_null, a1, tau1, a2, tau2, y0) == expected_result, "Fluorescence function failed at initial intensity test."