import os
import glob
import time
import pymssql

conn = pymssql.connect(host='daanvanmeerthema10.database.windows.net', port=1433,
database='Thema10', user='daanvanmeer', password='DitIsEenWachtwoord123!a')


os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')
 
base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
 
def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines
 
def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c
    
while True:
    print(read_temp())
    temp = read_temp()
    query = 'UPDATE Oefening21 SET sensorValue = ' + str(temp) + ' WHERE sensorDevice = ' + "'TempMeter'" +';'
    insertquery = 'INSERT INTO Oefening21 VALUES (' + "'TempMeter', " + str(temp) + ');'
    print(insertquery)
    cursor = conn.cursor()
    cursor.execute(insertquery)
    conn.commit()
    print("Execute complete")
    time.sleep(30)
