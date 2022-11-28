import time
from board import *
import digitalio
import busio
import usb_midi

import adafruit_midi
from adafruit_midi.note_off import NoteOff
from adafruit_midi.note_on import NoteOn

bln = [[GP1, GP22, 60], [GP3, GP21, 62], [GP4, GP20, 64], [
    GP6, GP19, 65], [GP10, GP18, 67], [GP13, GP17, 69], [GP14, GP16, 71]]
# bln = []

button = []
led = []
note = []

flg = []
tflg = []
midi = []

for i, e in enumerate(bln):
    bb = digitalio.DigitalInOut(e[0])
    bb.switch_to_input(pull=digitalio.Pull.DOWN)
    button.append(bb)
    led.append(digitalio.DigitalInOut(e[1]))
    led[i].direction = digitalio.Direction.OUTPUT
    note.append(e[2])

    flg.append(False)
    tflg.append(True)
    midi.append(adafruit_midi.MIDI(midi_out=usb_midi.ports[1], out_channel=i))

print('start')
while True:
    for i, (b, l, n, m) in enumerate(zip(button, led, note, midi)):
        if b.value:
            if tflg[i]:
                flg[i] = True
                tflg[i] = False
        else:
            tflg[i] = True

        if flg[i]:
            m.send(NoteOn(n, 100))
            flg[i] = False
        else:
            m.send(NoteOff(0, 0))

        l.value = not tflg[i]
