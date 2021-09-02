# create a reminder bot.
# get updates, grab user text, store a user text,constantly check time_1, send text.
import requests
from datetime import datetime, time
import time
import threading

bot_api = "Replace this with your api key"
base_url = f"https://api.telegram.org/bot{bot_api}/"


def updates(offset=None):
    r = f"{(base_url)}getupdates?offset={offset}&timeout=100"
    update = requests.get(r)
    update = update.json()["result"]
    return update

# https://api.telegram.org/bot/sendMessage?chat_id=325011602&text=Hey%20%20you%20hard%20on%20neck


def send_msg(chatid, text):
    full_url = f"{base_url}sendMessage?chat_id={chatid}&text={text}"
    msg_req = requests.get(full_url)


# thread handler function
def thread_handler(vka_msg, vid):

    msg, time_1 = (vka_msg).split(',')
    time_1 = time_1.replace(' ', '')
    flag = 0

    while True:
        try:
            time.sleep(2)
            date_1 = datetime.now()
            current_time = date_1.strftime('%H:%M:%d')
            print(
                f"current time_1={current_time} , user time_1 = {time_1}, user text = {vka_msg}\n")
            if current_time == time_1 and flag == 0:
                send_msg(vid, vka_msg)
                flag == 1
                break
        except:
            print('in exception state')
            break


# thread starter function


def thread_starter(vka_msg, vid):
    dummy_thread = threading.Thread(target=thread_handler, args=(vka_msg, vid))
    dummy_thread.start()


count = 0
uid = None
temp_uid = 0
while(True):
    text = updates(offset=uid)
    if text:
        vka_msg = text[-1]["message"]["text"]  # user text
        vid = text[-1]["message"]["chat"]["id"]  # chat_id
        uid = text[-1]["update_id"]  # update id
        if uid > temp_uid:
            thread_starter(vka_msg, vid)
        temp_uid = uid
        uid = uid+1
