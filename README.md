# Subway Clock Project
For our first Raspberry Pi project we decided to making a NYC subway themed clock with a led pixel display and a raspberry pi

### Project goals

Main goal:
- To create a clock display, which tells (i) the time and (ii) the stops for Line 6 in New York city.

Phase I Goal:
- Clock to display time + names of subway stops for Line 6 at fixed intervals
- Phase II Goal:
- Clock to display time + live updates from of subway e.g. 10:10, arriving at Longwood Av.

Stretch goals:
- Combine Raspberry Pi + Display to use a single source of power
- Create frame for clock


### Materials
- Adafruit 16 x 32 RGB LED Matrix Panel Display
- Raspberry Pi Zero (with WiFi)
- See more Materials: [https://learn.adafruit.com/connecting-a-16x32-rgb-led-matrix-panel-to-a-raspberry-pi/you-will-need](https://learn.adafruit.com/connecting-a-16x32-rgb-led-matrix-panel-to-a-raspberry-pi/you-will-need)

### RGB Code Repository

- [https://github.com/hzeller/rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix)

### Raspberry Pi Setup

- https://gist.github.com/gbaman/975e2db164b3ca2b51ae11e45e8fd40a

1. Install OS to memory that allows the Raspberry to function as computer
2. Use Mac with WiFi and make local network (aka hotspot)
3. Go back to raspberry and connect to Mac network. Tell Raspberry to always have same network address
4. Go to Mac and SSH via network address into Raspberry Pi
    Use login credentials available on Pi to log in
    ssh  pi@raspberrypi in terminal password: raspberry
5. Use command line on Mac to control Pi
6. Setup wifi following: https://medium.com/a-swift-misadventure/setup-your-raspberry-pi-2-3-with-raspbian-headless-without-cables-c78309fd7045
7. Code in gist link allows us to skip 1-3
8. How to transfer files from Mac to Raspberry Pi:
    - [http://thomasloughlin.com/how-to-transfer-files-from-a-mac-or-pc-onto-a-raspberry-pi/](http://thomasloughlin.com/how-to-transfer-files-from-a-mac-or-pc-onto-a-raspberry-pi/)
    - Open up a Terminal window.  Type in the following command: **scp **/_destination_/_filename_ pi@raspberrypi.local:_destination/path_
    - Password: raspberry
    - Example: scp test.jpg  pi@raspberrypi.local:~ (test.jpg is in home directory e.g. Ismael)
9. Set the clock on the Raspberry Pi


### Wire Up Raspberry Pi and Adafruit 16 x 32 RGB LED Matrix Panel Display

I would recommend following hzeller [guide](https://github.com/hzeller/rpi-rgb-led-matrix/)


###  Additional steps:

1. Create photoshop images (in pmp format) of all train stop names


### Code Requirements
We are use the python bindings of hzeller [rpi-rgb-led-matrix project](https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/bindings/python) so be sure to install clone his repo and install all necessary libraries for getting images displayed

### Reference and Inspiration Material:

- [https://www.raspberrypi.org/blog/nyc-train-sign/](https://www.raspberrypi.org/blog/nyc-train-sign/)
- [https://www.youtube.com/watch?v=Yeq8_xPArGM](https://www.youtube.com/watch?v=Yeq8_xPArGM)
- [https://www.youtube.com/watch?v=PbggS2rV9W4](https://www.youtube.com/watch?v=PbggS2rV9W4) (6) train
- [http://web.mta.info/nyct/service/sixline.htm](http://web.mta.info/nyct/service/sixline.htm)
- [http://web.mta.info/nyct/service/sixline.htm](http://web.mta.info/nyct/service/sixline.htm)

### Clock Images
