# MicroPython example of reading the Tiny Code Reader from Useful Sensors on a
# Micro:bit. See https://usfl.ink/ps_dev for full documentation on the module,
# and README.md in this project for details on wiring and assembly.

from microbit import *

import struct
import time

# The code reader has the I2C ID of hex 0c, or decimal 12.
TINY_CODE_READER_I2C_ADDRESS = 0x0C

# How long to pause between sensor polls.
TINY_CODE_READER_DELAY = 0.2

TINY_CODE_READER_LENGTH_OFFSET = 0
TINY_CODE_READER_LENGTH_FORMAT = "H"
TINY_CODE_READER_MESSAGE_OFFSET = TINY_CODE_READER_LENGTH_OFFSET + struct.calcsize(TINY_CODE_READER_LENGTH_FORMAT)
TINY_CODE_READER_MESSAGE_SIZE = 254
TINY_CODE_READER_MESSAGE_FORMAT = "B" * TINY_CODE_READER_MESSAGE_SIZE
TINY_CODE_READER_I2C_FORMAT = TINY_CODE_READER_LENGTH_FORMAT + TINY_CODE_READER_MESSAGE_FORMAT
TINY_CODE_READER_I2C_BYTE_COUNT = struct.calcsize(TINY_CODE_READER_I2C_FORMAT)

# Keep looping and reading the person sensor results.
while True:
    read_data = i2c.read(TINY_CODE_READER_I2C_ADDRESS,
                         TINY_CODE_READER_I2C_BYTE_COUNT)

    message_length,  = struct.unpack_from(TINY_CODE_READER_LENGTH_FORMAT, read_data, TINY_CODE_READER_LENGTH_OFFSET)
    message_bytes = struct.unpack_from(TINY_CODE_READER_MESSAGE_FORMAT, read_data, TINY_CODE_READER_MESSAGE_OFFSET)

    try:
        message_string = bytearray(message_bytes[0:message_length]).decode("utf-8")
        display.scroll(message_string)
    except:
        display.scroll("Couldn't decode as UTF 8")
        pass

    time.sleep(TINY_CODE_READER_DELAY)
