import time
from datetime import datetime
from PIL import Image
from os import listdir, getcwd
from os.path import isfile, join
from rgbmatrix import RGBMatrix, graphics
from utils import args, led_matrix_options


# Get supplied command line arguments
args = args()

# Check for led configuration arguments
matrixOptions = led_matrix_options(args)

# Initialize the matrix
matrix = RGBMatrix(options=matrixOptions)
canvas = matrix.CreateFrameCanvas()

font = graphics.Font()
font.LoadFont("../../../fonts/7x13.bdf")
textColor = graphics.Color(255, 255, 0)
pos = canvas.width

#get list of images
baseDirName = getcwd()
stopsDir = baseDirName + '/subway_stops/'
onlyfiles = [f for f in listdir(stopsDir) if isfile(join(stopsDir, f))]

totNumStops = len(onlyfiles)-1
curTrainStopInt = 0

while True:

    # get time
    my_text = datetime.now().strftime("%I:%M:%S %p")

    # if time falls on the hour show subway stop image
    if my_text[3:5] == '00:00' or my_text[3:5] == '30:00':

        image = Image.open(stopsDir + onlyfiles[curTrainStopInt]).convert('RGB')
        image.resize((matrix.width, matrix.height), Image.ANTIALIAS)
        img_width, img_height = image.size

        # scroll through image twice
        for x in range(2):
            xpos = 0
            # let's scroll
            while (xpos+1) < img_width:
                xpos += 1
                canvas.SetImage(image, -xpos)
                canvas.SetImage(image, -xpos + img_width)
                canvas = matrix.SwapOnVSync(canvas)
                time.sleep(0.21)

        if curTrainStopInt == totNumStops:
            curTrainStopInt = 0
            # might add code to change direction
        else:
            curTrainStopInt = curTrainStopInt + 1

    else:  # if we don't fall on the hour then show time
        canvas.Clear()
        my_text = my_text[0:5] # trim seconds
        lenTime = graphics.DrawText(canvas, font, pos, 14, textColor, my_text)
        pos -= 1
        if pos + lenTime < 0:
            pos = canvas.width

        time.sleep(0.10)
        canvas = matrix.SwapOnVSync(canvas)
