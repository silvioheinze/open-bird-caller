# SPDX-FileCopyrightText: 2021 Silvio Heinze
# SPDX-License-Identifier: GPL3
#
# Bird attraction caller with DS3231 RTC
# and DFPlayer mini to use MP3 files

import board
import busio
import adafruit_ds3231
from DFPlayer import DFPlayer


# setup dfplayer
uart = busio.UART(board.GP16, board.GP17)
dfplayer = DFPlayer(uart=uart, volume=100)

# time
i2c = busio.I2C(board.GP13, board.GP12)
rtc = adafruit_ds3231.DS3231(i2c)
current = rtc.datetime

# set time the first time running
# t = time.struct_time((2021, 06, 23, 17, 27, 0, 0, -1, -1))
# rtc.datetime = t

# set the full play hours as a comma separated list
times = [7, 8, 9, 12, 19, 20]

# main loop
while True:
    if current.tm_hour in times:
        dfplayer.play()
