#!/usr/bin/env python
from __future__ import print_function
import time
from osr import Rover
from arguments import Arguments
import json
from bluetooth import *
import xbox

'''
This code runs the JPL Open Source Rover. It accepts a few command line arguments for different functionality
   -s : Attempts to connect to a Unix socket for controlling the LED screen. The screen.py script must be running
                        previous to this in order to work. It lives at ../led/screen.py
   -x : Attemps to connect to a remote Xbox Controller to recieve drive commands
   -b : Attmpts to connect to a remote Bluetooth device to recieve drive commands

An example line running this script to run the LED screen and with an Xbox controller
        sudo python main.py -s -x
'''
def connect(config):
        server_sock = BluetoothSocket(RFCOMM)
        server_sock.bind(("",PORT_ANY))
        server_sock.listen(1)

        port = server_sock.getsockname()[1]
        uuid = config['BLUETOOTH_SOCKET_CONFIG']['UUID']
        name = config['BLUETOOTH_SOCKET_CONFIG']['name']
        advertise_service( server_sock, name,
                                           service_id = uuid,
                                           service_classes = [uuid, SERIAL_PORT_CLASS],
                                           profiles = [SERIAL_PORT_PROFILE],
                                           )
        print("waiting for connection on RFCOMM channel %d" % port)
        client_socket, client_info = server_sock.accept()
        client_socket.setblocking(0)
        print("Accepted connection from ", client_info)
        bt_sock = client_socket
        bt_sock.settimeout(1)
        while True:
                data = bt_sock.recv(1024)
                if data:
                        print(data)

def connect_x(config):
        joy = xbox.Joystick()
        print("Waiting on Xbox connect")
        while not joy.connected():
                time.sleep(1)
        print("Accepted connection from  Xbox controller", self.joy.connected())

def main():
        args = Arguments()
        with open('/home/pi/osr/rover/config.json') as f:
                config = json.load(f)

        with open('1.txt') as q:
                text = q.read()
                print(text)
        connect(config)
        #rover = Rover(config,args.bt_flag,args.xbox_flag,args.unix_flag)
        #connect_x(config)

        while True:
                try:
                        #rover.drive()
                        #time.sleep(0.1)
                        pass
                except Exception as e:
                        print(e)
                        rover.cleanup()
                        time.sleep(0.5)
                        rover.connectController()

if __name__ == '__main__':
        main()
