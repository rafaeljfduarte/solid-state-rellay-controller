import sys
import serial

if (len(sys.argv) < 3):
	print "Usage: relaywrite.py <PORT> <CMD>\nAvailable Commands:\n- read\n- on \n- off\nEg: relaywrite.py /dev/ttyACM0 on"
	sys.exit(0)
else:
	portName = sys.argv[1];
	relayCmd = sys.argv[2];

#Open port for communication
serPort = serial.Serial(portName, 19200, timeout=1)

#Send the command
serPort.write("relay "+ str(relayCmd) +" 0 \n\r")

print "Command sent..."

response = serPort.read(25)

if(response.find("on") > 0):
	print "Relay 0 is ON"

elif(response.find("off") > 0):
	print "Relay 0 is OFF"

#Close the port
serPort.close()
