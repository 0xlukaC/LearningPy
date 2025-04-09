#!/usr/bin/python

import cpu
import gpu
import harddisk
import ram

from random import *


class Computer:

    gprice = None
    
    def __init__(self, CPU, GPU, hardDisk, RAM):
        self.CPU = CPU
        self.GPU = GPU
        self.hardDisk = hardDisk
        self.RAM = RAM

    def start(self):
        self.CPU.compute()
        self.hardDisk.load_os()

    def __calcPrice(self):
        gprice = self.CPU.price + self.GPU.price + self.hardDisk.price + self.RAM.price
        return gprice

    def printPrice(self):
        return self.gprice if self.gprice != None else self.__calcPrice()

brands = ["xtreambean", "gognetoworks", "lukasupplies"]
price = [12999, 2, 12, 33333333, 110, 67]
speeds = [120, 300, 35, 2]


comp = Computer(cpu.CPU(12, brands[randint(0, 2)], 133), gpu.GPU(122, "xtreambean", "idk", 5), harddisk.HardDisk(1, "gognetworks", "idk", 1), ram.RAM(33, "lukasupplies", "DDR4"))


comp.start()
print(comp.printPrice())
