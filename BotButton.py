#coder :- Salman Faris
#Connect button on pin number GPIO12

import sys
import time
import random
import datetime
import telepot
import RPi.GPIO as GPIO

#Button
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# to use Raspberry Pi board pin numbers
GPIO.setmode(GPIO.BOARD)


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print 'Got command: %s' % command

    button_state = GPIO.input(12)
         if button_state == False:
             GPIO.output(12, True)
             bot.sendMessage(chat_id,text="Button Pressed")
             time.sleep(0.2)
    

bot = telepot.Bot('Bot Token')
bot.message_loop(handle)
print 'I am listening...'

while 1:
     time.sleep(10)
