from pyfirmata import Arduino

board = Arduino("/dev/ttyACM0")

speed = 0.6  # l298n=0.3, vnh2sp30=0.6

# l298n
_ena = 11
_enb = 3
_in1 = 6
_in2 = 10
_in3 = 9
_in4 = 5

# Dual VNH2SP30
_ena = 5
_enb = 6
_in1 = 8
_in2 = 7
_in3 = 9
_in4 = 4

in1 = board.get_pin("d:{}:o".format(_in1))
in2 = board.get_pin("d:{}:o".format(_in2))
ena = board.get_pin("d:{}:p".format(_ena))
in3 = board.get_pin("d:{}:o".format(_in3))
in4 = board.get_pin("d:{}:o".format(_in4))
enb = board.get_pin("d:{}:p".format(_enb))


def forward():
    in1.write(1)
    in2.write(0)
    in3.write(1)
    in4.write(0)
    ena.write(speed)
    enb.write(speed)


def left():
    in1.write(1)
    in2.write(0)
    in3.write(0)
    in4.write(1)
    ena.write(speed)
    enb.write(speed)


def right():
    in1.write(0)
    in2.write(1)
    in3.write(1)
    in4.write(0)
    ena.write(speed)
    enb.write(speed)


def stop():
    in1.write(0)
    in2.write(0)
    in3.write(0)
    in4.write(0)
    ena.write(0)
    enb.write(0)


forward()
left()
right()
stop()
