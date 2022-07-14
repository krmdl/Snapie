import adb
import snapchat


delay = 1


while True:
    adb.clear_data()
    adb.execute_snapchat()

    username = snapchat.get_username()
    userCreds = str(snapchat.snapchat(username)).split("'")
    password = userCreds[13]


    adb.submit_creds(username, password, delay)
    adb.skip(1)
    adb.follow("john.doe")

