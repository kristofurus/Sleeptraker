from Hackathon.Sleep import Sleep
from Hackathon.SleepPersistance import SleepPersistanceImpl
from Hackathon.SleepPresenter import SleepPresenter
from Hackathon.SleepView import SleepView
from tkinter import *
import tkinter as tk
import datetime

class SleepGUI(SleepView):
    def __init__(self, presenter):
        self.presenter = presenter

    def show_hour(self, hour):
        super().showhour(hour)

    def show_minute(self, minute):
        super().showminute(minute)


class SleepApplication(tk.Frame, SleepView):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.presenter = SleepPresenter(Sleep(SleepPersistanceImpl()), self)
        self.hour_option()
        self.minute_option()
        self.count_button()
        self.fact()

    def hour_option(self):
        hourframe = Frame(width=50, height=40)
        hourframe.pack(side="left")
        self.increment = tk.Button(self)
        self.increment.pack(side="right")
        self.create_button("+", self.presenter.increment_hour, self.increment)
        self.hour_display = tk.Label(self)
        self.hour_display["text"] = "0"
        self.hour_display.pack(side="top")
        self.decrement = tk.Button(self)
        self.create_button("-", self.presenter.decrement_hour, self.decrement)
        self.presenter.load_data()

    def minute_option(self):
        minuteframe = Frame(width=50, height=100)
        minuteframe.pack(side="right")
        self.increment = tk.Button(self)
        self.increment.pack(side="right")
        self.create_button("+", self.presenter.increment_minute, self.increment)
        self.minute_display = tk.Label(self)
        self.minute_display["text"] = "0"
        self.minute_display.pack(side="top")
        self.decrement = tk.Button(self)
        self.create_button("-", self.presenter.decrement_minute, self.decrement)

    def show_hour(self, hour):
        self.hour_display["text"] = str(hour)

    def show_minute(self, minute):
        self.minute_display["text"] = str(minute)

    def count_button(self):
        labelframe = LabelFrame(root, text="", width=100, height=5)
        labelframe.pack(fill="both", expand="yes")
        left = Label(labelframe, text=(self.lenght()), width=60, height=3)
        left.pack()
        #self.count = tk.Button(self)
        #self.count.pack()
        #self.create_button("count", labelframe, self.count)

    def fact(self):
        labelframe = LabelFrame(root, text="Interesting fact", width=100, height=5)
        labelframe.pack(fill="both", expand="yes")
        left = Label(labelframe, text="It takes the average human about 15 minutes to fall asleep", width=60, height=3)
        left.pack()

    def create_button(self, label, action, button):
        button["text"] = label
        button["command"] = action
        button.pack(side="top")

    def lenght(self):
        time_hour = self.hour_display["text"]
        time_minute = self.minute_display["text"]
        a = datetime.datetime.now()
        print(datetime.datetime.now())
        wakeup = a.replace(day=a.day + 1, hour=int(time_hour), minute=int(time_minute))
        print(wakeup)
        sleeptime = wakeup - a
        return "You will sleep: " + str(int(sleeptime.seconds/3600)) + " " + str(int((sleeptime.seconds / 60) % 60))
        # if sleeptime.seconds < 25200:
        #     str("You`ll sleep too short")
        # elif (sleeptime.seconds >= 25200 and sleeptime.seconds <= 32400):
        #     return str("Length of your sleep will be right")
        # elif sleeptime.seconds >= 32400:
        #     return str("You`ll sleep too long")


root = tk.Tk()
app = SleepApplication(master=root)
app.mainloop()
