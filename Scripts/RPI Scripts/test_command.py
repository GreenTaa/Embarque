import serial
from time import sleep


def Command (key) :                                                             #this function establish a serial cmmunication between RPI and the PCB
    if __name__=='__main__':                                                    #then it commands the pcb to execute a certain script.
        ser=serial.Serial('/dev/ttyACM0',9600,timeout=1)
        ser.flush()
        Stop = 0
        while Stop <= 1:
            ser.write(key)
            line=ser.readline().decode('utf-8').rstrip()
            print(line)
            sleep(1)
            Stop+=1

Command(b'2\n')
