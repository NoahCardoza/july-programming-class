from qnet3 import Connection

with open('bot.py', 'r') as f:
    bot = f.read()

c = Connection('10.0.1.6', 7777)
c.converse('killerkido upload\n' + bot)
