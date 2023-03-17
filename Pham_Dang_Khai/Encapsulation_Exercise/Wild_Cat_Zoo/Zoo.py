from Tiger import *
from Lion import *
from Cheetah import *
from Keeper import *
from caretake import *

class Zoo:
    def __init__(self, name, budget, animlal_capacity, workers_capacity):
        self.name = name
        self.animals = list()
        self.workers = list()
        self.__budget = budget
        self.__animal_capacity = animlal_capacity
        self.__workers_capacity = workers_capacity

    def add_animal(self, animal, price):
        if len(self.animals) < self.__animal_capacity:
            if self.budget >= price:
                self.budget -= price
                self.animals.append(animal)
                return f"{animal.name} the {type(animal).__name__} added to the zoo"
            else:
                return "Not enough budget"
        else:
            return "Not enough space for animal"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return "{} the {} hired successfully".format(worker.name, worker.__class__.__name__)
        else:
            return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return "{} fired successfully".format(worker_name)
        return "There is no {} in the zoo".format(worker_name)

    def pay_workers(self):
        sum_pay = 0
        for worker in self.workers:
            sum_pay += worker.salary
        if self.__budget >= sum_pay:
            self.__budget -= sum_pay
            return "You payed your workers. They are happy. Budget left: {}".format(sum_pay)
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        sum_pay = 0
        for animal in self.animals:
            sum_pay += animal.get_needs()
        if self.__budget >= sum_pay:
            self.__budget -= sum_pay
            return "You tended all the animals. They are happy. Budget left: {}".format(sum_pay)
        else:
            return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        status = ""
        status += "You have {} animals\n".format(len(self.animals))
        list_Lions = list()
        list_Tiger = list()
        list_Cheetah = list()
        for animal in self.animals:
            if isinstance(animal, Lion):
                list_Lions.append(animal)
            elif isinstance(animal, Tiger):
                list_Tiger.append(animal)
            else:
                list_Cheetah.append(animal)
        status += "----- {} Lions:\n".format(len(list_Lions))
        for lion in list_Lions:
            status += repr(lion) + "\n"
        status += "----- {} Tigers:\n".format(len(list_Tiger))
        for tiger in list_Tiger:
            status += repr(tiger) + "\n"
        status += "----- {} Cheetah:\n".format(len(list_Cheetah))
        for cheetah in list_Cheetah:
            status += repr(cheetah) + "\n"
        return status[:len(status) - 1]

    def workers_status(self):
        status = ""
        status += "You have {} workers\n".format(len(self.workers))
        list_Keeper = list()
        list_Caretaker = list()
        list_Vet = list()
        for worker in self.workers:
            if isinstance(worker, Keeper):
                list_Keeper.append(worker)
            elif isinstance(worker, Caretaker):
                list_Caretaker.append(worker)
            else:
                list_Vet.append(worker)
        status += "----- {} Keepers:\n".format(len(list_Keeper))
        for keeper in list_Keeper:
            status += repr(keeper) + "\n"
        status += "----- {} Caretakers:\n".format(len(list_Caretaker))
        for caretaker in list_Caretaker:
            status += repr(caretaker) + "\n"
        status += "----- {} Vets:\n".format(len(list_Vet))
        for vet in list_Vet:
            status += repr(vet) + "\n"
        return status[:len(status) - 1]