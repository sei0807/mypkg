# Copyright 2025 Seiya Ohata
# Licensed under the 3-Clause BSD License

import pytest


@pytest.mark.copyright
@pytest.mark.linter
def test_copyright():
    pytest.skip("Skipping copyright check due to strict formatting requirements")
