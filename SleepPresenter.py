class SleepPresenter:
    def __init__(self, counter_model, view):
        self.counter_model = counter_model
        self.view = view

    def increment_hour(self):
        new_hour = self.counter_model.increment_hour()
        self.view.show_hour(new_hour)

    def decrement_hour(self):
        new_hour = self.counter_model.decrement_hour()
        self.view.show_hour(new_hour)

    def increment_minute(self):
        new_minute = self.counter_model.increment_minute()
        self.view.show_minute(new_minute)

    def decrement_minute(self):
        new_minute = self.counter_model.decrement_minute()
        self.view.show_minute(new_minute)

    def load_data(self):
        self.view.show_hour(self.counter_model.get_hour())
        #self.view.show_minute(self.counter_model.get_minute())
