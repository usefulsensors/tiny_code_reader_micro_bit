# Tiny Code Reader Micro Bit
Example of accessing the Tiny Code Reader from MicroPython on a BBC Micro:bit.

The [Tiny Code Reader](https://usfl.ink/tcr) from [Useful Sensors](https://usefulsensors.com)
is a small hardware module that's intended to make it easy
to scan QR codes. It has an image sensor and a microcontroller with pretrained
software and outputs information from any identified codes over I2C.

It is designed to be used as an input to a larger system, and this example
shows how to read it from a [BBC micro:bit board](https://microbit.org/)
using MicroPython. It can also be used as the starting point for other
MicroPython-based boards, but since the exact syntax used to access the I2C bus
varies across platforms, you'll probably need to modify the lines that mention
`i2c` in the main Python script. For a full developer's guide, see [usfl.ink/tcr_dev](https://usfl.ink/tcr_dev).

## BoM

To build this project you'll need:

 - [Micro:bit board](https://microbit.org/buy/).
 - [Tiny Code Reader from Useful Sensors](https://usfl.ink/tcr).
 - [Qwiic connector cable](https://www.sparkfun.com/products/14427).
 - [SparkFun Qwiic micro:bit breakout](https://www.sparkfun.com/products/16445).

 I suggest the SparkFun breakout because it converts the micro:bit's small I2C
 pins into a standard Qwiic socket, but if you're skilled at soldering you could
 attach the wires directly to the edge pins on the board instead.

## Assembling

Slot the micro:bit into the breakout slot, with the two I2C sockets on the
breakout facing in the same direction as the front of the board (the side with
the buttons and LED display on it). Plug one end of the Qwiic cable into either
of the breakout's I2C sockets, and the other into the socket at the top of the
tiny code reader. If you power the micro:bit board, you should see the blue LED
on the tiny code reader start flashing multiple times a second.

## Running

Create a new project in the [Python micro:bit editor](https://python.microbit.org/v/3).
Click on the `Open` button, and choose the `main.py` file in this folder. Make
sure you have your Micro:bit plugged in and click `Send to micro:bit` to upload
the program to the board. If you point a QR code at the reader module, you
should see the text content of that code start scrolling on the display of the
Micro:bit.

For example if you open [this QR code](https://en.wikipedia.org/wiki/QR_code#/media/File:QR_code_for_mobile_English_Wikipedia.svg)
on your phone and hold it about fifteen centimeters or six inches from the 
module, facing the camera, you should see `http://en.m.wikipedia.org` scrolling
on the front LEDs of the board.