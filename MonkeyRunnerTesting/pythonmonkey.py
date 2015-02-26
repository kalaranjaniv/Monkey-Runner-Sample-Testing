
#Imports the monkeyrunner modules used by this program
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

# sets a variable with the package's internal name
package = 'com.example.circlearea'

# sets a variable with the name of an Activity in the package
activity = 'com.example.circlearea.AreaCircle'

# sets the name of the component to start
runComponent = package + '/' + activity

# Runs the component
easy_device.startActivity(component=runComponent)
MonkeyRunner.sleep(5)
# Press the calculate Button-without error
device.press('KEYCODE_MOVE_END', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
device.type('12.2')
device.press('KEYCODE_TAB', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_MOVE_END', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
device.type('1')
easy_device.touch(By.id("id/calculate"), MonkeyDevice.DOWN_AND_UP)
result = device.takeSnapshot()
result.writeToFile('./shot1.png', 'png')

# Press the calculate Button-with error(Pi length more than 16)
device.press('KEYCODE_MOVE_END', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
device.type('17')
easy_device.touch(By.id("id/calculate"), MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(5)
result = device.takeSnapshot()
result.writeToFile('./shot2.png', 'png')


# Press the calculate Button-with error(Pi length empty)
device.press('KEYCODE_MOVE_END', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
easy_device.touch(By.id("id/calculate"), MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(5)
result = device.takeSnapshot()
result.writeToFile('./shot3.png', 'png')

# Press the calculate Button-with error(Radius is empty)
device.press('KEYCODE_TAB', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_TAB', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_TAB', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_TAB', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_MOVE_END', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
easy_device.touch(By.id("id/calculate"), MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(5)
result = device.takeSnapshot()
result.writeToFile('./shot4.png', 'png')

# Press the clear Button-with error
easy_device.touch(By.id("id/clear"), MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(5)
result = device.takeSnapshot()
result.writeToFile('./shot5.png', 'png')

# Press the calculate Button(pi length as 16)
device.press('KEYCODE_MOVE_END', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
device.type('0')
device.press('KEYCODE_TAB', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_MOVE_END', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
device.press('KEYCODE_DEL', MonkeyDevice.DOWN_AND_UP)
device.type('16')
easy_device.touch(By.id("id/calculate"), MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(5)
result = device.takeSnapshot()
result.writeToFile('./shot6.png', 'png')


#Press the random coordinates
a=random.randint(1000,2000)
b=random.randint(1000,2000)
device.touch(a,b,MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(5)
result = device.takeSnapshot()
result.writeToFile('./shot7.png', 'png')

#Press the random coordinates
a=random.randint(100,200)
b=random.randint(100,200)
device.touch(a,b,MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(5)
result = device.takeSnapshot()
result.writeToFile('./shot8.png', 'png')

#Press the random coordinates
a=random.randint(110,220)
b=random.randint(120,230)
device.touch(a,b,MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(5)
result = device.takeSnapshot()
result.writeToFile('./shot9.png', 'png')

# Press the exit Button
easy_device.touch(By.id("id/exit"), MonkeyDevice.DOWN_AND_UP)
MonkeyRunner.sleep(5)
result = device.takeSnapshot()
result.writeToFile('./shot10.png', 'png')


