
name = "Gab"
Years = ["2020", "2021", "2022", "2030"]

#* ---- STRINGS ----
print('STRINGS\n')

# Formatting
print(f'my name is {name}') 
print('my name is {}'.format(name))
print(name * 2)
print(" ".join(Years))



#* ---- LISTS ----
print('\nLISTS\n')

# Slicing: list[start:end:step]

print(Years[::2])                            # Take each 2th elem
print(Years[2:])                             # Take from 2th elem
print(Years[:2])                             # Take until 2th last elem
print(Years[::-1])                           # Reverse list
a=Years[:]; print(a)                         # Shallow copy
a[:2] = [2001, 2002]; print(a)              # Multiple assignation
del a[:2]; print(a)                         # Multiple deletion









