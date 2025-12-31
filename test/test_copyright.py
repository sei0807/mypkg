# SPDX-FileCopyrightText: 2025 Seiya Ohata
# SPDX-License-Identifier: BSD-3-Clause

from ament_copyright.main import main
import pytest


@pytest.mark.copyright
@pytest.mark.linter
def test_copyright():
    rc = main(argv=[
        '.',
        'test',
        '--copyright-holder',
        'Seiya Ohata',
        '--license',
        'BSD-3-Clause',
    ])
    assert rc == 0, 'Found %d errors' % rc
