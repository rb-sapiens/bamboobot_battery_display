import time

import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

import smbus
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

current_battery = 0

def show_battery(rate):
	disp.clear()
	disp.display()
	draw.rectangle((0,0,width,height), outline=0, fill=0)

	padding = 5
	shape_width = 20
	top = padding
	bottom = height-padding
	x = padding
	fill = 255 if rate > 10 else 0
	draw.rectangle((x, top, x+shape_width, bottom), outline=255, fill=fill)

	fill = 255 if rate > 30 else 0
	draw.rectangle((x + shape_width + padding, top, x+shape_width*2 + padding, bottom), outline=255, fill=fill)

	fill = 255 if rate > 50 else 0
	draw.rectangle((x + shape_width*2 + padding * 2, top, x+shape_width*3 + padding * 2, bottom), outline=255, fill=fill)

	fill = 255 if rate > 70 else 0
	draw.rectangle((x + shape_width*3 + padding * 3, top, x+shape_width*4 + padding * 3, bottom), outline=255, fill=fill)

	fill = 255 if rate > 90 else 0
	draw.rectangle((x + shape_width*4 + padding * 4, top, x+shape_width*5 + padding * 4, bottom), outline=255, fill=fill)

	disp.image(image)
	disp.display()

# Raspberry Pi pin configuration:
RST = 24
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0

disp = Adafruit_SSD1306.SSD1306_128_32(rst=None, i2c_bus=1, gpio=1)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

font = ImageFont.truetype("/usr/share/fonts/truetype/noto/NotoSansMono-Bold.ttf", 23)
draw.text((10, 5), 'BambooBot',  font=font, fill=255)
disp.image(image)
disp.display()

bus = smbus.SMBus(1)
device_address = 0x0b

while True:
    data = bus.read_byte_data(device_address, 0x0d)
    time.sleep(10)
    if current_battery is not int(data):
        show_battery(int(data))
        current_battery = int(data)