A simple python program to scan discoverable BT devices
Performs progressive scanning (increasing scanning interval by a second) 
Generates a csv file which displays Scan number, Scan Interval, BT Name, MAC Address, Number of devices scanned this interval
Generates another csv file whihc records the start time and end time of the scanning along with the total number of devices scanned since the beginning of the application 

Dependencies:
sudo apt-get install bluetooth bluez python-bluez

References:
http://pages.iu.edu/~rwisman/c490/html/pythonandbluetooth.htm
