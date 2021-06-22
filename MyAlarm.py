import datetime
import winsound   # pip install PlaySound

def alarm(Timing):
    altime = str(datetime.datetime.now().strptime(Timing, "%H:%M %p"))

    altime = altime[11:-3]
    print(altime)
    Horeal = altime[:2]
    Horeal = int(Horeal)
    Mireal = altime[3:5]
    Mireal = int(Mireal)
    print(f"Done sir, alarm is set for {Timing}")

    while True:
        if Horeal==datetime.datetime.now().hour:
            if Mireal==datetime.datetime.now().minute:
                print("alarm is running")
                winsound.PlaySound('abc',winsound.SND_LOOP)

            elif Mireal<datetime.datetime.now().minute:
                break

if __name__ == '__main__':
    alarm("13:10 PM")   # enter whatever time you need