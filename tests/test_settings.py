# -*- coding: utf-8 -*-
from __future__ import absolute_import
import pytest
from mais.settings import Settings


def test_settings_init():
    s = Settings('mode', 'competition', 'model', 'batch', 'season')
    # object types
    assert isinstance(s, Settings)
