from gpiozero import AngularServo
import time
import explorerhat

s = AngularServo(18, min_angle=-0, max_angle=180, min_pulse_width=0.5/1000, max_pulse_width=2.4/1000)

#servo = AngularServo(18, min_angle=45, max_angle=-45, min_pulse_width=0.5/1000, max_pulse_width=2.4/1000)

s.angle = 170.0
time.sleep(0.1)
s.detach()
speed = 100
wipes = 2
interval = 2
def wipe():
        s.angle = 20.0
	time.sleep(0.1)
	s.detach()
        time.sleep(2)
	explorerhat.motor.one.backwards(100)
	time.sleep(interval)
        s.angle = 170.0
	time.sleep(0.1)
	s.detach()
	explorerhat.motor.one.stop()
        time.sleep(2)


def bubbles():
        for x in range(1, wipes):
		wipe()
	#s.angle = 170.0
	time.sleep(0.1)
	s.detach()

def open(channel, event):
	s.angle = 40.0
        time.sleep(0.1)
        s.detach()

def close(channel, event): 
	s.angle = 170.0
        time.sleep(0.1)
        s.detach()

explorerhat.touch.four.released(open)
explorerhat.touch.one.released(close)

#def handle_input(pin):
#    print(pin.name)


def changed(input):
  state = input.read()
  name  = input.name
  if state == 1:
	bubbles()
	print("Input {} changed to {}".format(name,state))

explorerhat.input.one.changed(changed)


#explorerhat.input.changed(handle_input)

explorerhat.pause()
