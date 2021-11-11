import RPi.GPIO as io

class L298NHBridge(object):

    PWM_MAX = 100

    leftmotor_in1_pin = 27
    leftmotor_in2_pin = 22
    leftmotorpwm_pin = 4

    rightmotor_in1_pin = 24
    rightmotor_in2_pin = 25
    rightmotorpwm_pin = 17


    def __init__(self):
        io.setmode(io.BCM)
        io.setwarnings(False)

        # Here we configure the GPIO settings for the left and right motors spinning direction. 
        # It defines the four GPIO pins used as input on the L298 H-Bridge to set the motor mode (forward, reverse and stopp).

        io.setup(self.leftmotor_in1_pin, io.OUT)
        io.setup(self.leftmotor_in2_pin, io.OUT)

        io.setup(self.rightmotor_in1_pin, io.OUT)
        io.setup(self.rightmotor_in2_pin, io.OUT)

        io.output(self.leftmotor_in1_pin, False)
        io.output(self.leftmotor_in2_pin, False)
        io.output(self.rightmotor_in1_pin, False)
        io.output(self.rightmotor_in2_pin, False)

        # Here we configure the GPIO settings for the left and right motors spinning speed. 
        # It defines the two GPIO pins used as input on the L298 H-Bridge to set the motor speed with a PWM signal.

        io.setup(self.leftmotorpwm_pin, io.OUT)
        io.setup(self.rightmotorpwm_pin, io.OUT)

        self.leftmotorpwm = io.PWM(self.leftmotorpwm_pin, 50)
        self.rightmotorpwm = io.PWM(self.rightmotorpwm_pin, 50)

        self.leftmotorpwm.start(0)
        self.leftmotorpwm.ChangeDutyCycle(0)

        self.rightmotorpwm.start(0)
        self.rightmotorpwm.ChangeDutyCycle(0)


    def set_motor_mode(self, motor, mode):
        # setMotorMode()
        # Sets the mode for the L298 H-Bridge which motor is in which mode.
        # This is a short explanation for a better understanding:
        #
        # motor		-> which motor is selected left motor or right motor
        # mode		-> mode explains what action should be performed by the H-Bridge
        #
        # setMotorMode(leftmotor, reverse)	-> The left motor is called by a function and set into reverse mode
        # setMotorMode(rightmotor, stopp)	-> The right motor is called by a function and set into stopp mode

        if motor == "leftmotor":
            if mode == "reverse":
                io.output(self.leftmotor_in1_pin, True)
                io.output(self.leftmotor_in2_pin, False)
            elif mode == "forward":
                io.output(self.leftmotor_in1_pin, False)
                io.output(self.leftmotor_in2_pin, True)
            else:
                io.output(self.leftmotor_in1_pin, False)
                io.output(self.leftmotor_in2_pin, False)

        elif motor == "rightmotor":
            if mode == "reverse":
                io.output(self.rightmotor_in1_pin, False)
                io.output(self.rightmotor_in2_pin, True)
            elif mode == "forward":
                io.output(self.rightmotor_in1_pin, True)
                io.output(self.rightmotor_in2_pin, False)
            else:
                io.output(self.rightmotor_in1_pin, False)
                io.output(self.rightmotor_in2_pin, False)
        else:
            io.output(self.leftmotor_in1_pin, False)
            io.output(self.leftmotor_in2_pin, False)
            io.output(self.rightmotor_in1_pin, False)
            io.output(self.rightmotor_in2_pin, False)


    def setMotorLeft(self, power):
        # SetMotorLeft(power)

        # Sets the drive level for the left motor, from +1 (max) to -1 (min).

        # This is a short explanation for a better understanding:
        # SetMotorLeft(0)     -> left motor is stopped
        # SetMotorLeft(0.75)  -> left motor moving forward at 75% power
        # SetMotorLeft(-0.5)  -> left motor moving reverse at 50% power
        # SetMotorLeft(1)     -> left motor moving forward at 100% power

        if power < 0:
            # Reverse mode for the left motor
            self.set_motor_mode("leftmotor", "reverse")
            pwm = -int(self.PWM_MAX * power)
            if pwm > self.PWM_MAX:
                pwm = self.PWM_MAX
        elif power > 0:
            # Forward mode for the left motor
            self.set_motor_mode("leftmotor", "forward")
            pwm = int(self.PWM_MAX * power)
            if pwm > self.PWM_MAX:
                pwm = self.PWM_MAX
        else:
            # Stopp mode for the left motor
            self.set_motor_mode("leftmotor", "stopp")
            pwm = 0
        # print "SetMotorLeft", pwm
        self.leftmotorpwm.ChangeDutyCycle(pwm)


    def setMotorRight(self, power):
        # SetMotorRight(power)

        # Sets the drive level for the right motor, from +1 (max) to -1 (min).

        # This is a short explanation for a better understanding:
        # SetMotorRight(0)     -> right motor is stopped
        # SetMotorRight(0.75)  -> right motor moving forward at 75% power
        # SetMotorRight(-0.5)  -> right motor moving reverse at 50% power
        # SetMotorRight(1)     -> right motor moving forward at 100% power

        if power < 0:
            # Reverse mode for the right motor
            self.set_motor_mode("rightmotor", "reverse")
            pwm = -int(PWM_MAX * power)
            if pwm > PWM_MAX:
                pwm = PWM_MAX
        elif power > 0:
            # Forward mode for the right motor
            self.set_motor_mode("rightmotor", "forward")
            pwm = int(PWM_MAX * power)
            if pwm > PWM_MAX:
                pwm = PWM_MAX
        else:
            # Stopp mode for the right motor
            self.set_motor_mode("rightmotor", "stopp")
            pwm = 0
        # print "SetMotorRight", pwm
        self.rightmotorpwm.ChangeDutyCycle(pwm)

    def exit(self):
        # Program will clean up all GPIO settings and terminates
        io.output(self.leftmotor_in1_pin, False)
        io.output(self.leftmotor_in2_pin, False)
        io.output(self.rightmotor_in1_pin, False)
        io.output(self.rightmotor_in2_pin, False)
        io.cleanup()
