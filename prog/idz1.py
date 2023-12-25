#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Разработать программу, в которой есть два вида задач - генерация чисел и проверка на чётность. 
# Производитель генерирует числа, а потребитель проверяет их на чётность.

import threading
from queue import Queue

class Producer(threading.Thread):
    def __init__(self, min_number, max_number, number_queue):
        threading.Thread.__init__(self)
        self.min_number = min_number
        self.max_number = max_number
        self.number_queue = number_queue
        
    def run(self):
        for number in range(self.min_number, self.max_number + 1):
            self.number_queue.put(number)
        self.number_queue.put(None)
        

class Consumer(threading.Thread):
    def __init__(self, input_queue, output_queue):
        threading.Thread.__init__(self)
        self.input_queue = input_queue
        self.output_queue = output_queue
        
    def run(self):
        while True:
            number = self.input_queue.get()
            if number is None:
                break
            result = self.check_number(number)
            self.output_queue.put((number, result))
                
    def check_number(self, number):
        # Проверка 
        if number % 2 == 0:
            return True
        else:
            return False
        
if __name__ == '__main__': 
    # Максимальные и минимальные значения принимаемые числами (диапазон значний)  
    min_number = -10 
    max_number = 10

    # Создание очередей
    input_queue = Queue()
    output_queue = Queue()

    # Создание объектов потоков 
    producer = Producer(min_number, max_number, input_queue)
    consumer = Consumer(input_queue, output_queue)

    # Запуск потоков
    producer.start()
    consumer.start()

    # Ожидание завершения потока потребителя
    consumer.join()

    # Вывод результатов
    while not output_queue.empty():
        number, result = output_queue.get()
        status = "чётное" if result else "не чётное"
        print('Число: {number}, {status}; ')