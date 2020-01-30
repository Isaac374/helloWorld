# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 09:44:38 2020

@author: Idrab
"""
import math
def circleArea(r):
    return math.pi*r**2
def squareArea(a):
    return a*a
def rectangleArea(a,b):
    return a*b
def triangleArea(b,h):
    return 0.5*b*h
goAgain = 'y'

while (goAgain == 'y'):
    print("Which shape's area do you want to calculate?")
    print("\n1, Circle")
    print("2, Square")
    print("3, Rectangle")
    print("4, Triangle")
    choice = input("Enter the number of your choice: ")
    if (choice =='1'):
        r = float(input("Enter the radius of the circle: "))
        A = circleArea(r)
        print("Area of the circle is: ", A)
        
    if (choice == '2'):
        a=float(input("Enter the side length of the square: "))
        A=squareArea(a)
        print ("area of the square is: ", A)
        
    if (choice == '3'):
        a = float(input("Enter the first side length: "))
        b = float(input("Enter the second side length: "))
        A = rectangleArea(a,b)
        print("Area of the rectangle is: ", A)
    
    if (choice == '4'):
        b = float(input("Enter the base of the triangle: "))
        h = float(input("Enter the height of the triangle "))
        A = triangleArea(b,h)
        print("Area of the triangle is: ", A)
        
    goAgain = input("Would you like to run again (y/n): ")

print("Thank you for using our program!")
