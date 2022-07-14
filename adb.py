from ppadb.client import Client as AdbClient
from time import sleep
client = AdbClient(host="127.0.0.1", port=5037)
device = client.device("emulator-5554") 


def clear_data():
    device.shell("pm clear com.snapchat.android")

def execute_snapchat():
    device.shell("pm grant com.snapchat.android android.permission.CAMERA")
    device.shell("pm grant com.snapchat.android android.permission.READ_EXTERNAL_STORAGE")
    device.shell("pm grant com.snapchat.android android.permission.WRITE_EXTERNAL_STORAGE")
    device.shell("am start com.snapchat.android")


def close_snapchat():
    device.shell("input keyevent 3")

def submit_creds(username: str, password: str, delay: float):
    sleep(delay+5)
    device.shell("input keyevent 61")
    sleep(delay)
    device.shell("input keyevent 61")
    sleep(delay)
    device.shell("input keyevent 66")
    sleep(delay + 1)
    device.shell("input text '%s'" %username)
    sleep(delay)
    device.shell("input keyevent 61")
    sleep(delay)
    device.shell("input keyevent 61")
    sleep(delay)
    device.shell("input text '%s'" %password)
    sleep(delay + 1)
    device.shell("input keyevent 61")
    sleep(delay)
    device.shell("input keyevent 61")
    sleep(delay)
    device.shell("input keyevent 61")
    sleep(delay)
    device.shell("input keyevent 66")
    sleep(delay+10)


def skip(delay: float):
    sleep(delay)
    device.shell("input keyevent 61")
    sleep(delay)
    device.shell("input keyevent 66")
    sleep(delay)

def follow(username: str):
    device.shell("am start -a android.intent.action.VIEW -d https://www.snapchat.com/add/%s" %username)
    sleep(10)
    device.shell("input tap 521 1394")
    sleep(5)
