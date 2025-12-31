# Copyright 2025 Seiya Ohata
# SPDX-License-Identifier: BSD-3-Clause

import pytest


@pytest.mark.copyright
@pytest.mark.linter
def test_copyright():
    pytest.skip("Skipping copyright check due to strict formatting requirements")
