# Copyright 2025 Seiya Ohata
# Licensed under the 3-Clause BSD License

from ament_copyright.main import main
import pytest

@pytest.mark.copyright
@pytest.mark.linter
def test_copyright():
    rc = main(argv=['.', 'test'])
    assert rc == 0, 'Found %d errors' % rc
