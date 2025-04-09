#!/usr/bin/python

class HardDisk:

    def __init__(self, price, brand, hd_type, size):
        self.price = price
        self.brand = brand
        self.hd_type = hd_type
        self.size = size

    def load_os(self):
        return print("the os is loading")
    
