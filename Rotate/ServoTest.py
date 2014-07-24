from RPIO import PWM

servo = PWM.Servo()

# Set servo on GPIO17 to 1200 milis (1.2ms)
servo.set_servo(18, 1200)

# Set servo on GPIO17 to 2000 mili s (2.0ms)
servo.set_servo(18, 2000)

# Clear servo on GPIO17
servo.stop_servo(18)
