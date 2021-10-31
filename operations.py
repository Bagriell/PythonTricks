
#* ---- UNDERSCORES ---- 

for _ in range(2):                      # For loop that doesn't use counter
    print("Hi Earth!")
a, _, b = (1, 2, 3)                     # ignoring value
properInteger = 100_000                 # underscore integers

#* ---- LOOPS & CONDITIONALS ----

sum(i for i in range(10) )              # loops in function calls
result = 1 < 3 < 5                      # chained operators
result = True if False else True        # Ternary
if 5 in [1,3,5,7]:                      
    print('True if 5 is in the list')

# Dict Compréhension
arr = [1, 2, 3, 4, 5]
a = {arrplusone: arrplusone+1 for arrplusone in arr}
print(f'a = {a}')  
