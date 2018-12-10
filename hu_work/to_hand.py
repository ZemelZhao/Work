import serial

if __name__ == '__main__':
    ser = serial.Serial('/dev/rfcomm0', 115200)
    judge = True
    while True:
        if input() == '1':
            break
        else:
            if judge:
                print('fist')
                ser.write(b'A')
            else:
                print('rest')
                ser.write(b'B')


