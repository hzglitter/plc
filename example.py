import snap7
import logging
from Tkinter import *

logging.basicConfig(level=logging.WARNING)

class myPlc:
    def __init__(self,ip,rack,slot):
        self.ip = ip
        self.rack = rack
        self.slot = slot

    def connect(self):
        self.client = snap7.client.Client()
        self.client.connect(self.ip, self.rack, self.slot)

    def disc(self):
        self.client.disconnect()
        self.client.destroy()

    def blocks (self):
        self.blockList = self.client.list_blocks()
        print self.blockList

    def stop(self):
        self.client.plc_stop()

    def start(self):
        self.client.plc_hot_start()

    def writeToDB(self,dbN,size,start):
        data = bytearray(size)
        i = 0
        for cifra in data:
            data[i] = i*i
            i += 1
        self.client.db_write(dbN, start, data)

    def readingDB(self,dbN,size,start):
        print "Reading DB",dbN,size,"byte"
        res = self.client.db_read(dbN,start,size)
        for rec in res:
            print(rec)

    def test_download(self,dbN):
        data = bytearray(1024)
        self.client.download(dbN, data)




if __name__ == '__main__':
    plc = myPlc('192.168.0.65',0,2)

    ans=True
    while ans:
        print ("""
        1.Connect to PLC
        2.Read DB
        3.Start PLC
        4.Stop PLC
        5.Write to DB
        6.List of Blocks
        7.Disconnect from PLC
        8.Exit
        """)
        ans=raw_input("Choose... ")
        if ans=="1":
            plc.connect()
        elif ans=="2":
            plc.readingDB(1,10,0)
        elif ans=="3":
            plc.start()
        elif ans=="4":
            plc.stop()
        elif ans=="5":
            plc.writeToDB(1,10,0)
        elif ans=="6":
            plc.blocks()
        elif ans=="7":
            plc.disc()
        elif ans=="8":
            break
        elif ans !="":
            print("\n Not Valid Choice Try again")



