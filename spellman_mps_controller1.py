#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Filename: spellman_mps_controller.py

""" 
    This module defines the functions and instance methods to open communication ports between a 
    master device and Spellman MPS series high voltage power supply. 
    It defines how to pass queries to, communicate with, and command networked MPS devices
    attached to a UART-RS485 converted series of devices. Full manufacturer datasheet functionality 
    is included. 
"""

import serial
import time

from serial.serialutil import EIGHTBITS, PARITY_NONE

class SetPort:
    def __init__(ser, dev, baudrate, timeout):
        ser.dev = '/dev/ttyS0'
        ser.baudrate = 9600
        ser.timeout = 1
        ser.serial = serial.Serial(ser.dev, baudrate, parity=PARITY_NONE, stopbits = serial.STOPBITS_ONE, 
        bytesize = EIGHTBITS,)
        
        if not ser.isOpen():
            print ('Unsuccessful')
        else:
            print ('The port is open')
            #Print the port was opened successfully. 
            #or head back to the drawing board.
    
    
###########################################################3 
#   def Uart_SendByte(ser, value):
#       ser.serial.write(value.encode('ascii'))
#
#   def Uart_SendString(ser, value):
#       ser.serial.write(value.encode('ascii'))
#
#   def Uart_ReceiveByte(ser):
#       ser.serial.read(1).decode("utf-8")
#
#   def Uart_ReceiveString(ser, value):
#       data = ser.serial.read(value)
#       return data.decode("utf-8")

# REPLACE WITH READUNTIL or READLINE IF POSSIBLE, WRITEUNTIL OR WRITELINE - SPELLMAN LINE-FEED CHAR ON ALL STX RTX
# OTHERWISE IMPLEMENT BUFFER UNTIL \n
# TIMEOUT NEEDED?           ???SERIAL.READ_UNTIL(EXPECTED=LF, SIZE=NONE)???             SERIAL.READ(SIZE)???
# FLUSH BUFFER BEFORE AND AFTER READLINE.
# 10 MS SLEEP AFTER EACH.


#############################################################

# CHECKSUM - FUNCTION/LOOP.
# AFTER RESPONSE OR QUERY HAVE BEEN DECODED, INTERPRETS TO ENGLISH THE RESPONSE AND PRINTS.

#  Transmit from host
#  The general message format is shown below 
#  <STX><ADDR><DEVTYPE>< DATA><CSUM><<LF>
#  Response from host
#  <STX><ADDR><DEVTYPE><DATA><CSUM><LF>
#  The host ADDR is always 9
#  Where:
#  <STX> = 1 ASCII 0x02 Start of Text character.
#  <ADDR> = 1 ASCII character representing the address of the unit to
#  which the message is being sent.
#  <DEVTYPE> = 1 ASCII characters representing the type of power module.
#  < DATA> = Command Argument, up to 7 ASCII characters.
#  <CSUM> = Checksum (see section 7 for details)
#  <LF> = 1 ASCII 0x0A Line Feed character 
########################################################

######################################
# 
# 
# DEFINE SpellmanClass(SetPort)
#
#
# PARAMETER FOR ADDRESS OF EACH SPELLMAN
# DEFINE METHODS FOR ALL COMMANDS AND QUERIES ON SPELLMAN DATASHEET
# RETURNS BOOL (OR STRING, INTEGER, ETC CASE DEPENDENT) TO MASTER DEVICE TO CONFIRM SUCCESS
# CLOSES PORT ON USER INPUT OR POSSIBLE TIMEOUT.    
#
#######################################