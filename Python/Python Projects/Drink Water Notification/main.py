import win10toast
from plyer import notification
import time

# toast = win10toast.ToastNotifier()
# while True:
#     toast.show_toast("Reminder to drink Water",
#                      "Drink water to stay hydrated and healthy",
#                     icon_path="Python Projects\Drink Water Notification\water.ico",
#                     duration=5)
#     time.sleep(60*60)

while True:
    try:
        notification.notify(
                    title = "  Reminder to Drink Water!!!",
                    message="  Hii, Drink water to stay Hydrated and Healthy" ,
                    app_icon="D:\Tasks\Python\Python Projects\Drink Water Notification\water.ico",
                    timeout=10
                )
    except Exception as e:
        print(e)
        
    time.sleep(60*60)
