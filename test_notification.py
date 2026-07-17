from win10toast import ToastNotifier
import time

toast = ToastNotifier()

toast.show_toast(
    "AstraQuant Test",
    "Windows notification is working!",
    duration=10,
    threaded=False,
)

time.sleep(12)