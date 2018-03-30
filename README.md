# Subway Clock Project
For our first Raspberry Pi project we decided to making a NYC subway themed clock with a led pixel display and a raspberry pi

### Project goals

Main goal:
- To create a clock display, which tells (i) the time and (ii) the stops for Line 6 in New York city.

Phase I Goal:
- Clock to display time + names of subway stops for Line 6 at fixed intervals
Phase II Goal:
- Clock to display time + live updates from of subway, e.g. 10:10, arriving at Longwood Av., using MTA api

Stretch goals:
- Combine Raspberry Pi + Display to use a single source of power
- Create frame for clock


### Materials
- Adafruit 16 x 32 RGB LED Matrix Panel Display
- Raspberry Pi Zero (with WiFi)
- See more materials: [https://learn.adafruit.com/connecting-a-16x32-rgb-led-matrix-panel-to-a-raspberry-pi/you-will-need](https://learn.adafruit.com/connecting-a-16x32-rgb-led-matrix-panel-to-a-raspberry-pi/you-will-need)

### RGB LED Matrix Code Repository

- [https://github.com/hzeller/rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix)

### Headless Raspberry Pi Zero Setup

1. Download and Install [raspbian](https://www.raspberrypi.org/downloads/raspbian/) to SD card
2. Plug in SD Card to Raspberry Pi
3. We wanted to setup our raspberry pi without ever having to plug it into a physical screen
so we followed this [gist](https://gist.github.com/gbaman/975e2db164b3ca2b51ae11e45e8fd40a) that allowed us to do so as long as we had a micro USB cable and an additional computer
4. Use micro USB cable to connect a computer to the Pi
5. Go to Mac/PC and SSH via network address into Raspberry Pi
    Use login credentials available on Pi to log in
    ssh  pi@raspberrypi in terminal password: raspberry
6. Use command line on Mac/PC to control Pi
7. Setup wifi on Pi by following: https://medium.com/a-swift-misadventure/setup-your-raspberry-pi-2-3-with-raspbian-headless-without-cables-c78309fd7045
8. Transfer files from Mac/PC to Raspberry Pi:
    - [http://thomasloughlin.com/how-to-transfer-files-from-a-mac-or-pc-onto-a-raspberry-pi/](http://thomasloughlin.com/how-to-transfer-files-from-a-mac-or-pc-onto-a-raspberry-pi/)
    - Example: scp test.jpg  pi@raspberrypi.local:~ (test.jpg is in home directory e.g. Ismael)
9. Set the clock on the Raspberry Pi

### Wire Up Raspberry Pi and Adafruit 16 x 32 RGB LED Matrix Panel Display
We would recommend following hzeller [guide](https://github.com/hzeller/rpi-rgb-led-matrix/)

###  Additional steps:
1. Create photoshop images (in pmp format) of all train stop names

### Code Requirements
We are use the python bindings of hzeller [rpi-rgb-led-matrix project](https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/bindings/python) so be sure to install clone his repo and install all necessary libraries for getting images displayed

### Reference and Inspiration Material:

- [https://www.raspberrypi.org/blog/nyc-train-sign/](https://www.raspberrypi.org/blog/nyc-train-sign/)
- [https://www.youtube.com/watch?v=Yeq8_xPArGM](https://www.youtube.com/watch?v=Yeq8_xPArGM)
- [https://www.youtube.com/watch?v=PbggS2rV9W4](https://www.youtube.com/watch?v=PbggS2rV9W4) (6) train
- [http://web.mta.info/nyct/service/sixline.htm](http://web.mta.info/nyct/service/sixline.htm)
- [https://github.com/MLB-LED-Scoreboard/mlb-led-scoreboard](https://github.com/MLB-LED-Scoreboard/mlb-led-scoreboard)
### Clock Images
