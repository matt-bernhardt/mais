# -*- coding: utf-8 -*-
from __future__ import absolute_import
import pytest
from mais.settings import Settings


def test_settings_init():
    with pytest.raises(TypeError) as excinfo:
        s = Settings()
    assert 'missing 5 required' in str(excinfo.value)
    s = Settings('mode', 'competition', 'model', 'batch', 'season')
    # object types
    assert isinstance(s, Settings)


# Need a test for the output method
def test_settings_output():
	s = Settings('mode', 'competition', 'model', 'batch', 'season')
	assert len(s.output()) > 0
