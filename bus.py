"""
bus.py
Demonstrate a dictionary.
"""

import sys

bus = {
    "wheels": "round and round",
    "wipers": "swish, swish, swish",
    "horn": "beep,beep,beep",
    "doors": "open and shut",
    "driver": "move on back",
    "babies": "move on back",
    "mommies": "shush, shush, shush",
    "muggers": "bang, bang, bang"
}

for things in bus:
    print(f"The {things} on the bus go {bus[things]}")
    print(f"{bus[things]}")
    print(f"{bus[things]}")
    print(f"The {things} on the bus go {bus[things]}")
    print("All through the town")
