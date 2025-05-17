import time
import board
import busio
import adafruit_vl53l0x

# I2C 연결 설정
i2c = busio.I2C(board.SCL, board.SDA)

# VL53L0X 센서 객체 생성
sensor = adafruit_vl53l0x.VL53L0X(i2c)

# 거리 측정
try:
    while True:
        distance = sensor.range  # 센서에서 거리 측정
        print(f"Distance: {distance} mm")
        time.sleep(0.5)
except KeyboardInterrupt:
    print("Measurement stopped by user")
