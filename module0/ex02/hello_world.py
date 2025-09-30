#!/usr/bin/env python3

print("Hello World")
array = []

while True:
	user = input("digita arrombado: ")
	if user == "stop":
		break
	array.append(user)

print(array)