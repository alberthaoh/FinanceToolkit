"""Overlap Model Tests"""
import pandas as pd

from financetoolkit.technical import overlap_model

# pylint: disable=missing-function-docstring


def test_get_moving_average(recorder):
    recorder.capture(
        overlap_model.get_moving_average(pd.Series([100, 110, 120, 130, 80]), 10)
    )


def test_get_exponential_moving_average(recorder):
    recorder.capture(
        overlap_model.get_exponential_moving_average(
            pd.Series([0.01, -0.03, 0.05, 0.01, -0.02]), 10
        )
    )


def test_get_double_exponential_moving_average(recorder):
    recorder.capture(
        overlap_model.get_double_exponential_moving_average(
            pd.Series([0.01, -0.03, 0.05, 0.01, -0.02]), 10
        )
    )


def test_get_trix(recorder):
    recorder.capture(
        overlap_model.get_trix(pd.Series([0.01, -0.03, 0.05, 0.01, -0.02]), 10)
    )


def test_get_triangular_moving_average(recorder):
    recorder.capture(
        overlap_model.get_triangular_moving_average(
            pd.Series([0.01, -0.03, 0.05, 0.01, -0.02]), 20
        )
    )
