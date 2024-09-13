from typing import Any

import narwhals.stable.v1 as nw
from tests.utils import Constructor
from tests.utils import compare_dicts

data = {
    "a": [1.0, None, None, 3.0],
    "b": [1.0, None, 4, 5.0],
}


def test_n_unique(constructor: Constructor) -> None:
    df = nw.from_native(constructor(data))
    result = df.select(nw.all().n_unique())
    expected = {"a": [3], "b": [4]}
    compare_dicts(result, expected)


def test_n_unique_series(constructor_eager: Any) -> None:
    df = nw.from_native(constructor_eager(data), eager_only=True)
    expected = {"a": [3], "b": [4]}
    result_series = {"a": [df["a"].n_unique()], "b": [df["b"].n_unique()]}
    compare_dicts(result_series, expected)
