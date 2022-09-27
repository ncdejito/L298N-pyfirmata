from pyfirmata import Arduino
from example2 import VNH2SP30
from example2 import Motor

board = Arduino('/dev/ttyACM0')
# analog_0 = board.get_pin('a:0:o')
# analog_1 = board.get_pin('a:1:o')
# analog_0.write(1)
# analog_1.write(1)
# Initial pin
ena = 5
enb = 6
in1 = 8
in2 = 7
in3 = 9
in4 = 4
motor = VNH2SP30(board, ena, in1, in2, in3, in4, enb)
# Forward with speed 70%
motor.forward(0.6,0.2)
motor.forward(0,0.2) # stop
motor.turn_right(0.6,0.2)
motor.turn_left(0.6,0.2)