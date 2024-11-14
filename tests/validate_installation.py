"""
Very simple CLI util to verify that installation is okay.
Most challenges related to pc_ble_driver so now we just ensure that it works.
"""
import sys
try:
    from pc_ble_driver_py import config
    config.__conn_ic_id__ = 'NRF52'
    from pc_ble_driver_py.ble_driver import BLEDriver  # noqa: F401,pylint: disable=unused-import
    print('INSTALLATION OK')
except Exception as error:  # pylint: disable=broad-except
    print('INSTALLATION IS NOT OK!')
    print(error)
    sys.exit(1)
