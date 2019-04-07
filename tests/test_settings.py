# -*- coding: utf-8 -*-
from __future__ import absolute_import
import pytest
from datetime import date
from mais.settings import Settings


def test_settings_blank():
    with pytest.raises(TypeError) as excinfo:
        s = Settings()
    assert 'missing 6 required' in str(excinfo.value)

def test_settings_init():
    start = date(
        year=1996,
        month=4,
        day=13
    )
    s = Settings('mode', 'competition', 'model', 'batch', 1996, start)
    # object types
    assert isinstance(s, Settings)

# Need a test for the output method
def test_settings_output():
	s = Settings('mode', 'competition', 'model', 'batch', 1996, date.today())
	assert len(s.output()) > 0
