import json


class SleepPersistance:
    def persist(self, hour):
        pass

    def load(self):
        return 0


class SleepPersistanceImpl(SleepPersistance):
    def persist(self, hour):
        with open('data.json', 'w') as outfile:
            json.dump({"hour": hour}, outfile)

    def load(self):
        with open('data.json', 'r') as outfile:
            return json.load(outfile)["hour"]



