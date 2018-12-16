class Sleep:
    def __init__(self, persistance):
        self.__persistance = persistance
        self.__hour = self.__persistance.load()
        self.__minute = 0

    def increment_hour(self):
        self.__hour += 1
        if self.__hour == 24:
            self.__hour = 0
        self.__persistance.persist(self.__hour)
        return self.__hour

    def decrement_hour(self):
        self.__hour -= 1
        if self.__hour == -1:
            self.__hour = 23
        self.__persistance.persist(self.__hour)
        return self.__hour

    def get_hour(self):
        return self.__hour

    def increment_minute(self):
        self.__minute += 1
        if self.__minute == 60:
            self.__minute = 0
        return self.__minute

    def decrement_minute(self):
        self.__minute -= 1
        if self.__minute == -1:
            self.__minute = 59
        return self.__minute

    def get_minute(self):
        return self.__minute
