import time
from plyer import notification
if __name__ == '__main__':
    while True:
        notification.notify(
            title="**Start your coding Now!",
            message="You have to do coding without coding  you can not get a job in company and Improve your communication skill.",
            # app_icon = "C:\\Users\\acer\Desktop\\python_question\\download.jpg",
            timeout=12
        )

        time.sleep(60*60)
