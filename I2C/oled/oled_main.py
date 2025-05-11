import time
import board
import busio
import adafruit_ssd1306
from PIL import Image, ImageDraw, ImageFont

# I2C 설정
i2c = busio.I2C(board.SCL, board.SDA)

# 디스플레이 초기화
oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

# 디스플레이 초기화
oled.fill(0)
oled.show()

# 이미지 및 그리기 객체 생성
width = oled.width
height = oled.height
image = Image.new("1", (width, height))
draw = ImageDraw.Draw(image)

# 폰트 설정 (시스템 폰트를 사용할 수 있습니다)
try:
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 16)
except IOError:
    font = ImageFont.load_default()

# 텍스트 출력
draw.text((0, 0), "Hello, World!", font=font, fill=255)

# 디스플레이에 이미지 표시
oled.image(image)
oled.show()

# 잠시 대기
time.sleep(5)

# 디스플레이 지우기
oled.fill(0)
oled.show()
