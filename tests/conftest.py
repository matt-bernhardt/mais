from __future__ import absolute_import
import pytest
import os


@pytest.fixture
def data_teams():
    return _fixture_path('tbl_teams.csv')


def _fixture_path(path):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(current_dir, 'fixtures', path)
