#!/bin/env python3

# motors_control.py
def turn_on_motors():
    # Включить моторы
    print("Моторы ВКЛ.")

def set_smooth_speed(speed):
    # Плавно меняет скорость робота
    print(f"Скорость плавно изменена до {speed}%")

def turn_off_motors():
    # Выключить моторы
    print("Моторы ВЫКЛ.")

# Главный цикл
turn_on_motors()
set_smooth_speed(50) # Добавлено улучшение
turn_off_motors()
