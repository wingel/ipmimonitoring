# Python ipmimonitoring

This module is a Python wrapper for libipmimonitoring from
https://www.gnu.org/software/freeipmi/ .

## Requirements

libipmimonitoring must be installed, on debian install it with:

```
sudo apt install -y libipmimonitoring6
```

Install ipmimonitoring either from source or via PyPi:

```
pip install impimonitoring
```

## Test application

ipmimonitoring/\_\_main\_\_.py contains a simple tool which reads
sensor data, similar to ipmi-sensors from the freeipmi-tools package
which can be run like this:

```
python -m ipmimonitoring [arguments]
```

The output will look like this:

```
+-----+-------+--------+----------------+------------------------+----------+---------+---------+---------+---------+------------------------+-----------------------------+
| Num | Event | Sensor | Sensor Name    | Sensor Type            | State    | Reading | Units   | Type    | Bitmask | Bitmask Type           | Bitmask Strings             |
+-----+-------+--------+----------------+------------------------+----------+---------+---------+---------+---------+------------------------+-----------------------------+
|   1 |  0x6f |    235 | Watchdog       | WATCHDOG2              | NOMINAL  |    None | NONE    | UNKNOWN |    0x00 | WATCHDOG2              | OK                          |
|  23 |  0x6f |    225 | SEL            | EVENT_LOGGING_DISABLED | CRITICAL |    None | NONE    | UNKNOWN |    0x10 | EVENT_LOGGING_DISABLED | SEL Full                    |
|  29 |  0x6f |    228 | CPU0_Status    | PROCESSOR              | NOMINAL  |    None | NONE    | UNKNOWN |    0x80 | PROCESSOR              | Processor Presence detected |
|  30 |  0x01 |      1 | CPU0_TEMP      | TEMPERATURE            | NOMINAL  |   44.00 | CELSIUS | DOUBLE  |    0xc0 | THRESHOLD              | OK                          |
|  31 |  0x01 |      4 | DIMMG0_TEMP    | TEMPERATURE            | NOMINAL  |   35.00 | CELSIUS | DOUBLE  |    0xc0 | THRESHOLD              | OK                          |
|  32 |  0x01 |      5 | DIMMG1_TEMP    | TEMPERATURE            | NOMINAL  |   35.00 | CELSIUS | DOUBLE  |    0xc0 | THRESHOLD              | OK                          |
|  33 |  0x01 |     12 | CPU0_DTS       | TEMPERATURE            | NOMINAL  |   56.00 | CELSIUS | DOUBLE  |    0xc0 | THRESHOLD              | OK                          |
|  34 |  0x01 |      2 | PCH_TEMP       | TEMPERATURE            | NOMINAL  |   44.00 | CELSIUS | DOUBLE  |    0xc0 | THRESHOLD              | OK                          |
|  41 |  0x01 |     25 | THERM_7        | TEMPERATURE            | NOMINAL  |   27.00 | CELSIUS | DOUBLE  |    0xc0 | THRESHOLD              | OK                          |
|  42 |  0x01 |     29 | M2_AMB_TEMP_1  | TEMPERATURE            | NOMINAL  |   40.00 | CELSIUS | DOUBLE  |    0xc0 | THRESHOLD              | OK                          |
|  43 |  0x01 |     30 | M2_AMB_TEMP_2  | TEMPERATURE            | NOMINAL  |   27.00 | CELSIUS | DOUBLE  |    0xc0 | THRESHOLD              | OK                          |
|  44 |  0x01 |      8 | HIC_TEMP_0     | TEMPERATURE            | NOMINAL  |   31.00 | CELSIUS | DOUBLE  |    0xc0 | THRESHOLD              | OK                          |
|  45 |  0x01 |      9 | HIC_TEMP_1     | TEMPERATURE            | NOMINAL  |   30.00 | CELSIUS | DOUBLE  |    0xc0 | THRESHOLD              | OK                          |
|  46 |  0x01 |     10 | HIC_TEMP_2     | TEMPERATURE            | NOMINAL  |   36.00 | CELSIUS | DOUBLE  |    0xc0 | THRESHOLD              | OK                          |
|  47 |  0x01 |     11 | HIC_TEMP_3     | TEMPERATURE            | NOMINAL  |   34.00 | CELSIUS | DOUBLE  |    0xc0 | THRESHOLD              | OK                          |
|  48 |  0x01 |     13 | HIC_TEMP_4     | TEMPERATURE            | NOMINAL  |   37.00 | CELSIUS | DOUBLE  |    0xc0 | THRESHOLD              | OK                          |
|  49 |  0x01 |    184 | CPU0_FAN       | FAN                    | NOMINAL  |  750.00 | RPM     | DOUBLE  |    0xc0 | THRESHOLD              | OK                          |
|  50 |  0x01 |    185 | FCH_FAN        | FAN                    | NOMINAL  | 2400.00 | RPM     | DOUBLE  |    0xc0 | THRESHOLD              | OK                          |
|  56 |  0x6f |    230 | PS1_Status     | POWER_SUPPLY           | NOMINAL  |    None | NONE    | UNKNOWN |    0x00 | POWER_SUPPLY           | OK                          |
|  57 |  0x6f |    231 | PS2_Status     | POWER_SUPPLY           | NOMINAL  |    None | NONE    | UNKNOWN |    0x00 | POWER_SUPPLY           | OK                          |
|  60 |  0x01 |     64 | P_12V          | VOLTAGE                | NOMINAL  |   12.09 | VOLTS   | DOUBLE  |    0xc0 | THRESHOLD              | OK                          |
|  61 |  0x01 |     66 | P_3V3          | VOLTAGE                | NOMINAL  |    3.33 | VOLTS   | DOUBLE  |    0xc0 | THRESHOLD              | OK                          |
|  62 |  0x01 |     65 | P_5V           | VOLTAGE                | NOMINAL  |    5.00 | VOLTS   | DOUBLE  |    0xc0 | THRESHOLD              | OK                          |
|  63 |  0x01 |     67 | P_5V_STBY      | VOLTAGE                | NOMINAL  |    5.03 | VOLTS   | DOUBLE  |    0xc0 | THRESHOLD              | OK                          |
|  64 |  0x01 |     79 | P_VBAT         | VOLTAGE                | NOMINAL  |    2.93 | VOLTS   | DOUBLE  |    0xc0 | THRESHOLD              | OK                          |
|  66 |  0x01 |     14 | VR_P0_TEMP     | TEMPERATURE            | NOMINAL  |   33.00 | CELSIUS | DOUBLE  |    0xc0 | THRESHOLD              | OK                          |
|  67 |  0x01 |     16 | VR_DIMMG0_TEMP | TEMPERATURE            | NOMINAL  |   38.00 | CELSIUS | DOUBLE  |    0xc0 | THRESHOLD              | OK                          |
|  68 |  0x01 |     17 | VR_DIMMG1_TEMP | TEMPERATURE            | NOMINAL  |   35.00 | CELSIUS | DOUBLE  |    0xc0 | THRESHOLD              | OK                          |
|  69 |  0x01 |     81 | VR_P0_VOUT     | VOLTAGE                | NOMINAL  |    0.93 | VOLTS   | DOUBLE  |    0xc0 | THRESHOLD              | OK                          |
+-----+-------+--------+----------------+------------------------+----------+---------+---------+---------+---------+------------------------+-----------------------------+
```

### Reading in-band sensors from the local BMC

Read sensors from the local machine using /dev/impiN.  Normally
opening that device requires root permissions:

```
sudo python -m ipmimonitoring
```

alternately, change the permissions so that your user can access the
device:

```
sudo chown $USER /dev/impi*
python -m ipmimonitoring
```

### Reading out-of-band sensors from a remote BMC

It's also possible to access a remote BMC over the network.  You need
to provide a hostname, username and password.

```
python -m ipmimonitoring --hostname=host --username=user --password=password
```

### Flags

Most parameters supported by libipmimonitoring should be possible to
set using the command line.  A few additional ones are listed below.

Keep reading IPMI data forever.  Optionally specify how many seconds
to wait between each read.  Default 1 second.

```
python -m ipmimonitoring --follow[=seconds]
```

The table output is produced using the prettytable module
(https://github.com/prettytable/prettytable).  Any format supported by
prettytable (currently text, html, json, csv, latex and mediawiki) can
be used with this tool.

```
python -m ipmimonitoring --table[=format]]
```

Output JSON format with the field names as the keys instead of the
table headings.  Optionally pass the number of spaces to indent the
JSON data for a prettier readout.

```
python -m ipmimonitoring --json[=indent]
```

## License

All the code written by me is licensed under the MIT license.

Note that libimpimonitoring itself is licensed under GPLv2 or later,
but since libipmonitoring is distributed as a Debian package it should
be ok to use it the way this Python module does without tainting it.
Or that is how I read this paragraph from the GPLv2 license:

    However, as a special exception, the source code distributed need
    not include anything that is normally distributed (in either
    source or binary form) with the major components (compiler,
    kernel, and so on) of the operating system on which the executable
    runs, unless that component itself accompanies the executable

Also, as far as I know APIs are not copyrightable, so the headers and
APIs in wrapper.py and all enums should be ok to distribute under a
MIT license.
