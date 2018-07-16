from qnet3 import Connection

c = Connection('10.0.1.6', 7777)

print(c.converse('who'))
print(c.converse('motd'))

while True:
    print(c.converse('killerkido ' + input('> ')))
