#! uv run python3
"""Simple example of how to use the ipmimonitoring module."""

import os

from ipmimonitoring import IpmiMonitoringContext

def main():
    if 1:
        # in-band communication with the local BMC
        hostname = None
        username = None
        password = None
    else:
        # out-of-band communication with a remote BMC
        hostname = 'hostname'
        username = 'username'
        password = 'password'

    sdr_cache_directory = None
    if os.geteuid() != 0:
        # The default SDR cache directory is not writeable by a normal
        # user.  Default to ~/.cache if we are not running as root
        sdr_cache_directory = os.path.join(os.environ['HOME'], '.cache')

    ctx = IpmiMonitoringContext(
        hostname = hostname,
        username = username,
        password = password,
        sdr_cache_directory = sdr_cache_directory)

    records = ctx.read_sensors()

    for record in records:
        if isinstance(record.sensor_reading, float):
            print(f"{record.sensor_name:<20}  {record.sensor_reading:>8.2f}  {record.sensor_units.name}")

if __name__ == '__main__':
    main()
