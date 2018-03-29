
# Subway Clock Project
## Making a NYC subway themed Clock with a led pixel display and a raspberry pi

Our first Raspberry Pi project


Project Subway Sandwich Display

**Project goals: **

- ●To create a clock display, which tells (i) the time and (ii) the stops for Line 6 in New York city.
- ●Is a conversation piece in the living room to help Ismael get a girlfriend!
- **Stretch goals: **

- ●Combine Raspberry Pi + Display to use a single source of power
- ●Create frame for clock (e.g. subway sandwich on wheels)
- **Phase I: **
- Clock to display time + names of subway stops for Line 6 at fixed intervals
- **Phase II: **
- Clock to display time + live updates from of subway e.g. 10:10, arriving at Longwood Av.
- **Materials we need: **

- ●Adafruit 16 x 32 RGB LED Matrix Panel Display
- ●Raspberry Pi Zero (with WiFi)
- ●See more Materials: [https://learn.adafruit.com/connecting-a-16x32-rgb-led-matrix-panel-to-a-raspberry-pi/you-will-need](https://learn.adafruit.com/connecting-a-16x32-rgb-led-matrix-panel-to-a-raspberry-pi/you-will-need)
- **RGB Code Repository:**

- ●[https://github.com/hzeller/rpi-rgb-led-matrix](https://github.com/hzeller/rpi-rgb-led-matrix)
- **Raspberry Pi Setup **

- ●https://gist.github.com/gbaman/975e2db164b3ca2b51ae11e45e8fd40a

1. 1.Install OS to memory that allows the Raspberry to function as computer
2. 2.Use Mac with WiFi and make local network (aka hotspot)
3. 3.Go back to raspberry and connect to Mac network. Tell Raspberry to always have same network address
4. 4.Go to Mac and SSH via network address into Raspberry Pi
1. a.ssh  pi@raspberrypi in terminal password: raspberry

5. 5.Use login credentials available on Pi to log in
6. 6.Use command line on Mac to control Pi
7. 7.Setup wifi following: https://medium.com/a-swift-misadventure/setup-your-raspberry-pi-2-3-with-raspbian-headless-without-cables-c78309fd7045
8. *Code in gist link allows us to skip 1-3
9. How to transfer files from Mac to Raspberry Pi:

- ●[http://thomasloughlin.com/how-to-transfer-files-from-a-mac-or-pc-onto-a-raspberry-pi/](http://thomasloughlin.com/how-to-transfer-files-from-a-mac-or-pc-onto-a-raspberry-pi/)
- ●Open up a Terminal window.  Type in the following command: **scp **/_destination_/_filename_ pi@raspberrypi.local:_destination/path_

- ●Password: raspberry
- ●Example: scp test.jpg  pi@raspberrypi.local:~ (test.jpg is in home directory e.g. Ismael)
- **Codes**
- E.g. runs a program - sudo ./led-image-viewer some-image.jpg. You can tell via the ./ (equivalent to opening a program like google chrome on laptop)
- But only allows you to run one program at a time. So need to use Bash to bundle all these programs to run simultaneously.
- **Code for clock (not using anymore as they are in C++):**
- [https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/examples-api-use/clock.cc](https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/examples-api-use/clock.cc)
- **Code for images (not using anymore as they are in C++):**
- [https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/utils](https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/utils)
- https://github.com/adafruit/RGB-matrix-Panel
- **Next steps: **

1. 1.Set the clock on the Raspberry Pi
2. 2.Download the clock.cc code onto Raspberry Pi
3. 3.Create photoshop images (in pmp format) of all train stop names with circle (6) - [https://learn.adafruit.com/connecting-a-16x32-rgb-led-matrix-panel-to-a-raspberry-pi/a-scrolling-message](https://learn.adafruit.com/connecting-a-16x32-rgb-led-matrix-panel-to-a-raspberry-pi/a-scrolling-message)
4. [https://forums.adafruit.com/viewtopic.php?f=47&t=79916&p=404763&hilit=create+led+image#p404763](https://forums.adafruit.com/viewtopic.php?f=47&t=79916&p=404763&hilit=create+led+image#p404763)
5. My forum request: [https://forums.adafruit.com/viewtopic.php?f=47&t=127528](https://forums.adafruit.com/viewtopic.php?f=47&t=127528)
6. 4.Figure out a way to cycle through clock.cc code and images of train stops
8. **General code:**
9. [https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/bindings/python](https://github.com/hzeller/rpi-rgb-led-matrix/tree/master/bindings/python)
11. **Next steps for coding: **
12. 5.Use Python to figure out styling and font size for text appearing on screen
13. 6.Then use Python again to figure out how to create 6 in a circle. So we need to know how to create a circle using code, and have a ‘6’ in the middle of it.
14. 7.Use Python to figure out how to make text scroll
15. 8.Write code to get current time on Pi and sync it to the screen
16. 9.Write code to time alternation between clock and station name


- **Reference Material:**

- ●[https://www.raspberrypi.org/blog/nyc-train-sign/](https://www.raspberrypi.org/blog/nyc-train-sign/)
- ●[https://www.youtube.com/watch?v=Yeq8_xPArGM](https://www.youtube.com/watch?v=Yeq8_xPArGM)
- ●[https://www.youtube.com/watch?v=PbggS2rV9W4](https://www.youtube.com/watch?v=PbggS2rV9W4) (6) train
- ●[http://web.mta.info/nyct/service/sixline.htm](http://web.mta.info/nyct/service/sixline.htm)
- ●
- **Screen:**

- ●Will show time, and at intervals, scroll through station names



Write code to satisfy our project goals

Homework:
- ●Michelle to talk with friend about removing grey pixels (to black pixels) from image
- ● Make all the images
- ●[http://web.mta.info/nyct/service/sixline.htm](http://web.mta.info/nyct/service/sixline.htm)
- ●Write code that switches between clock and image



1. 8.Installing an OS to memory that allows the Raspberry to function as computer
2. 9.Use Mac with WiFi and make local network (aka hotspot)
3. 10.Go back to raspberry and connect to Mac network. Tell Raspberry to always have same network address
4. 11.Go to Mac and SSH via network address into Raspberry Pi
5. 12.Use login credentials available on Pi to log in
6. 13.Use command line on Mac to control Pi
7. *Code allows us to skip 1-3
9. [https://gist.github.com/gbaman/975e2db164b3ca2b51ae11e45e8fd40a](https://gist.github.com/gbaman/975e2db164b3ca2b51ae11e45e8fd40a)
11. Ideas:
12. Pacman eating time
13. Mini Yayoi Kusama installation
