from pwn import *
import operator

from pwnlib.util.iters import chained
from six import class_types

ops = {
    b'+' : operator.add,
    b'-' : operator.sub,
    b'*' : operator.mul,
    b'//' : operator.truediv,  # use operator.div for Python 2
    b'%' : operator.mod,
    b'^' : operator.xor,
}

def calcul(op1, oper, op2):
    print(f"Op {op1}, ope {oper}, op {op2}")
    op1, op2 = int(op1), int(op2)
    return ops[oper](op1, op2)

chall = remote('static-01.heroctf.fr', 8000)

i = 0
chall.recvline()
chall.recvline()
while True:
    print(f"Calcul {i}")
    calc = chall.recvline()
    print(f"calcule = {calc}")
    nb = calc.split()
    if "exec" in str(nb[0]):
        break
    res = calcul(nb[0], nb[1], nb[2])
    res = str(int(res)).encode()
    print(f"res = {res}")
    chall.sendline(res)
    chall.recvline()
    i += 1

chall.interactive()
