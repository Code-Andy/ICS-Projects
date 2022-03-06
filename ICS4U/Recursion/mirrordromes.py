'''
Given a string, calculate the amount of mirrordromes that 
exist within a given string (including single letter mirrors).

A mirrordrome is a word that can be mirrored if cut in half and folded over on itself.

Single letters that are considered mirrors in this program include:
i, l, m, n, o, t, u, v, w, x

Letters that are considered mirrored opposites in this program include:
b <-> d, p <-> q, s <-> z

Examples:
If you ran iterativeCalculate("dob") you would get a return value of 2 ("dob" and "o" are both mirrordromes).
If you ran recursiveCalculate("totally") you would get a return value of 7 ("t", "t", "o", "l", "l", "ll", and "tot" are all mirrordromes)
'''

singleLetters = ['i', 'l', 'm', 'n', 'o', 't', 'u', 'v', 'w', 'x']
mirrorLetters = {'b': 'd', 'p': 'q', 's': 'z'}


def recursiveCalculate(word):
    word[0]
