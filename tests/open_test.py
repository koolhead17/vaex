import tempfile
import shutil
import os
import pytest

import vaex

path = os.path.dirname(__file__)


def test_open():
    with pytest.raises(IOError):
        vaex.open('doesnotexist')


    csv1 = os.path.join(path, 'data', 'small2.csv')
    csv2 = os.path.join(path, 'data', 'small2.csv')
    h51 = os.path.join(path, 'data', 'small2.csv.hdf5')
    h52 = os.path.join(path, 'data', 'small3.csv.hdf5')
    target = os.path.join(path, 'data', 'small2.csv.hdf5')

    vaex.open(csv1, convert=True)
    assert os.path.exists(target)
    os.remove(target)

    target = os.path.join(path, 'data', 'small2.csv_and_1_more.hdf5')
    vaex.open(os.path.join(path, 'data', 'small*.csv'), convert=True)
    assert os.path.exists(target)
    assert os.path.exists(h51)
    assert os.path.exists(h52)
    vaex.open(os.path.join(path, 'data', 'small?.csv.hdf5'))
    os.remove(target)
    os.remove(h51)
    os.remove(h52)

    # convert can also be a path
    target = os.path.join(path, 'data', 'convert.hdf5')
    vaex.open(os.path.join(path, 'data', 'small*.csv'), convert=target)
    assert os.path.exists(target)
    assert os.path.exists(h51)
    assert os.path.exists(h52)
    vaex.open(os.path.join(path, 'data', 'small?.csv.hdf5'))
    os.remove(target)
    os.remove(h51)
    os.remove(h52)

    target = os.path.join('custom.hdf5')
    vaex.open(os.path.join(path, 'data', 'small*.csv'), convert=target)
    assert os.path.exists(h51)
    assert os.path.exists(h52)
    assert os.path.exists(target)
    os.remove(target)
    os.remove(h51)
    os.remove(h52)



