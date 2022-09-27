from pyfirmata import Arduino

MOTOR_A = 0
MOTOR_B = 1
HIGH = 1
LOW = 0


class Motor():
    def __init__(self, board, in1, in2, pwn):
        self.in1 = board.get_pin('d:{}:o'.format(in1))
        self.in2 = board.get_pin('d:{}:o'.format(in2))
        self.pwn = board.get_pin('d:{}:p'.format(pwn))


class VNH2SP30():
    def __init__(self, board, ena, in1, in2, in3, in4, enb):
        self.board = board

        self.motor = {
            0: Motor(board, in1, in2, ena),
            1: Motor(board, in3, in4, enb)
        }

    def drive_motor(self, motor_index, speed):
        self.motor[motor_index].pwn.write(speed)

    def drive_motors(self, speed):
        self.drive_motor(MOTOR_A, speed)
        self.drive_motor(MOTOR_B, speed)

    def setup_motor(self, motor_index, state1, state2):
        self.motor[motor_index].in1.write(state1)
        self.motor[motor_index].in2.write(state2)

    def setup_motors(self, state1, state2, state3, state4):
        self.setup_motor(MOTOR_A, state1, state2)
        self.setup_motor(MOTOR_B, state3, state4)

    def forward(self, speed, delay_time):
        self.setup_motors(HIGH, LOW, HIGH, LOW)
        self.drive_motors(speed)
        self.board.pass_time(delay_time)

    def backward(self, speed, delay_time):
        self.setup_motors(LOW, HIGH, LOW, HIGH)
        self.drive_motors(speed)
        self.board.pass_time(delay_time)

    def full_stop(self, delay_time):
        self.setup_motors(LOW, LOW, LOW, LOW)
        self.drive_motors(0)
        self.board(delay_time)

    def turn_left(self, speed, delay_time):
        self.setup_motors(HIGH, LOW, LOW, LOW)
        self.drive_motors(speed)
        self.board.pass_time(delay_time)

    def turn_right(self, speed, delay_time):
        self.setup_motors(LOW, HIGH, HIGH, LOW)
        self.drive_motors(speed)
        self.board.pass_time(delay_time)



def main():
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
    # motor.forward(0.6,0.2)
    motor.forward(0,0.2) # stop
    # motor.turn_right(0.6,0.2)
    # motor.turn_left(0.6,0.2)


if __name__ == '__main__':
    main()
