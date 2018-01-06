import abc

class Patient(object):
    def __init__(self):
        self._observers = []

    def signObserver(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def  detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        for observer in self._observers:
            observer.update(self)

class CancerPatient(Patient):
    def __init__(self):
        super(CancerPatient, self).__init__()
        self._message = None

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, msg):
        self._message = msg
        self.notify()

class Observer(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def update(self, patient):
        pass

class FamillyObserver(Observer):
    def update(self, patient):
        print("Familly observer: %s" % patient.message)

class NurseObserer(Observer):
    def update(self, patient):
        print("Nurse observer: %s" % patient.message)

familly = FamillyObserver()
nurse = NurseObserer()
cancerpatient = CancerPatient()
cancerpatient.signObserver(familly)
cancerpatient.message = "my familly comes to see patient."
cancerpatient.signObserver(nurse)
cancerpatient.message = "nurse comes to see patient."
cancerpatient.detach(nurse)
cancerpatient.message = "nurse is gone."
