from bluetooth import *
import csv
import sys
import time
import datetime

print("Scanning Devices...")
devices = {}

BTDevicesFile = open("BTDevices"+str(round(time.time()))+".csv", 'wt')
BTTimeFile = open("BTTime"+str(round(time.time()))+".csv", "wt")
BTPacketsFile = open("BTPackets"+str(round(time.time()))+".csv", "wt")

writerDevice = csv.writer(BTDevicesFile)
writerDevice.writerow(['Scan #', 'Scan Duration', 'MAC', 'Name', '# Devices/Scan'])

writerTime = csv.writer(BTTimeFile)
writerTime.writerow(['Start Time','End Time','Total Devices Discovered'])

writerPackets = csv.writer(BTPacketsFile)
writerPackets.writerow(['MAC Address', 'Packets'])

scanNumber = 0
scanDuration = 0

try:
	while(True):
		if not (scanDuration == 14):
			scanDuration += 1

		startTime = time.time()
		nearby_devices = discover_devices(lookup_names = True, flush_cache = True, duration = scanDuration)
		endTime = time.time()
		
		scanNumber += 1
		print("(Scan #%d) Devices Discovered : %d\nScan Duration: %d" % (scanNumber, len(nearby_devices), scanDuration))
		
		for addr, name in nearby_devices:
			writerDevice.writerow((scanNumber, scanDuration, addr, name, len(nearby_devices)))
			if addr in devices:
				devices[addr].append(name+":"+str(scanNumber))
			else:
				devices[addr] = [name+":"+str(scanNumber)]

		writerTime.writerow([startTime, endTime, len(devices)])
		print("Total devices discovered: %d" % len(devices))

except KeyboardInterrupt:
	BTDevicesFile.close()
	BTTimeFile.close()
	for MAC, Packets in devices.items():
		writerPackets.writerow([MAC, str(Packets)])
	BTPacketsFile.close()
	print('Goodbye!')
