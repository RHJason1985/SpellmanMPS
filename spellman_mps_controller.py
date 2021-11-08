#!/usr/bin/env python
#-*- coding: utf-8 -*-
# Filename: spellman_mps_controller.py

""" 
    This module defines the functions and methods to open communication ports between a 
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
        bytesize = EIGHTBITS)

        if not ser.isOpen():
            print ('Unsuccessful')
        else:
            print ('The port is open')
            #Print the port was opened successfully. 
            #or head back to the drawing board.
#       
#       def checksum(value, address):
#            
#       PERFORM CHECKSUM HERE FOR SENDLINE
#

        def uart_sendline(ser, address, value):
            ser.serial.flushInput()                         #This is the only place that seems logical to me to flush.
            time.sleep(.01)
            ser.serial.flushOutput()                        #This is the only place that seems logical to me to flush.
            time.sleep(.01)
            finalstring = ser.checksum(value)               # This will be the string sent to Spellman after checksum is inserted into user input. 
            ser.serial.write(finalstring.encode('ascii'))   # I will probably need to encode into ascii during checksum method, so this encode
                                                            # may not be necessary for final version. May just be ser.serial.write(finalstring)

        def uart_receiveline(ser, value):
            data = ser.serial.readline(value)
            return data.decode('utf-8')

class SpellmanClass(SetPort):
    def __init__(self, address):                # 1 is the default address that will need to be modified for further instances. 
        address = self.address                  # So, it needs to be hooked up, have address 1 altered through SpellmanClass methods, then 
                                                # create another instance with the new address after being altered. Any ideas on a way to set the address
                                                # earlier on?

        def setvoltage(address, command):       # Command <V1=xxxx.x> where xxxx.x is a voltage from 0.0 to the maximum unit voltage. 
            setvoltage.uart_sendline(command)   # Typical response ACK.         
            response = setvoltage.uart_receiveline()
            print (response)
    
        def currentvoltage(address, command):   # Command <V1?> Request present value of output voltage. See MPS datasheet note 1.     
            currentvoltage.uart_sendline(command)
            response = currentvoltage.uart_receiveline()
            print (response)
    
        def readvoltage(address, command):      # Command <M0?> 0V to the maximum voltage of the unit. See MPS datasheet note 2.   
            readvoltage.uart_sendline(command)
            response = readvoltage.uart_receiveline()
            print (response)
    
        def readcurrent(address, command):      # Command <M1?> 0uA to the maximum current of the unit. See MPS datasheet note 2.   
            readcurrent.uart_sendline(command)
            response = readcurrent.uart_receiveline()
            print (response)
     
        def readvoltageraw(address, command):   # Command <R0?>      
            readvoltageraw.uart_sendline(command)
            response = readvoltageraw.uart_receiveline()
            print (response)
    
        def readcurrentraw(address, command): # Command <R1?>  
            readcurrentraw.uart_sendline(command)
            response = readcurrentraw.uart_receiveline()
            print (response)
    
        def disable(address, command):        # Command <EN0> Disable all outputs. See MPS datasheet note 4. No response. 
            disable.uart_sendline(command)
            response = disable.uart_receiveline()
            print (response)
 
        def enable(address, command):         # Command <EN1> Enable all outputs. See MPS datasheet note 4. No response. 
            enable.uart_sendline(command)
            response = enable.uart_receiveline()
            print (response)

        def getaddress(address, command):     # Command <ID?> Read the unit's address. See MPS datasheet note 4 and 5.  
            getaddress.uart_sendline(command)
            response = getaddress.uart_receiveline()
            print (response)

        def setaddress(address, command):     # Command <ID=x> Set the unit's address. Typical response ACK. See MPS datasheet note 6.
            setaddress.uart_sendline(command)
            response = setaddress.uart_receiveline()
            print (response)

        def getsoftware(address, command):     # Command <SW?> Request software version number.
            getsoftware.uart_sendline(command)
            response = getsoftware.uart_receiveline()
            print (response)

        def getbaud(address, command):         # Command <BD?> Read the baud rate, where 0 is 9600, 1 is 19200.
            getbaud.uart_sendline(command)
            response = getbaud.uart_receiveline()
            print (response)     
       
        def setbaud(address, command):         # Command <BD=x> Set the baud rate, where 0 is 9600, 1 is 19200.
            setbaud.uart_sendline(command)
            response = setbaud.uart_receiveline()
            print (response)     
       
        def getdevicetype(address, command):   # Command <DT?> 
            getdevicetype.uart_sendline(command)
            response = getdevicetype.uart_receiveline()
            print (response)                 
    
