
#Imports the monkeyrunner modules used by this program
import os;
from subprocess import Popen
from com.android.monkeyrunner import MonkeyRunner, MonkeyDevice, MonkeyImage
from com.android.monkeyrunner.MonkeyDevice import takeSnapshot
from com.android.monkeyrunner.easy import EasyMonkeyDevice
from com.android.monkeyrunner.easy import By
from com.android.chimpchat.hierarchyviewer import HierarchyViewer
from com.android.monkeyrunner import MonkeyView
import random

# Connects to the current device, returning a MonkeyDevice object
device = MonkeyRunner.waitForConnection()
easy_device=EasyMonkeyDevice(device)
# Installs the Android package. Notice that this method returns a boolean, so you can test
# to see if the installation worked.
easy_device.installPackage('CircleAreaV1D0/bin/CircleAreaV1D0.apk')

package = 'com.example.circlearea'

# Sets the monkey adb command

command = "adb shell monkey -p " + package + " -v " + str(numberOfRandomEvents)
platformToolsPath = "C:\Kala\Android-Essential-Software-Packages\adt-bundle-windows-x86\adt-bundle-windows-x86\sdk\platform-tools"


process= Popen([platformToolsPath + command], shell=True)


# Set the initial count

count = 1


# While the Monkey process is running, take a screenshot periodically and write it to the screenshot storage location

while process.poll() is None:print "Taking screenshot " + str(count) + "..."
  
filename = "shot" + str(count) + ".png"
  
screenshot = device.takeSnapshot()
  
screenshot.writeToFile(filename,"png")
  
count += 1
  
MonkeyRunner.sleep(1)


