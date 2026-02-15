from re import Match
Jar_1_cap = 5 # set jug 1 cap as 5
Jar_2_cap = 3 # set jug 4 cap as 3
target = 4

def Target(Jar_1,Jar_2,target): # method to check if we reached the target
if(Jar_1 == target or Jar_2 == target):
print("SUCCES!")
return True
else:
print(f"Current: Jar_1={Jar_1}L, Jar_2={Jar_2}L")
return False

Jar_1 = 0
Jar_2 = 0

print(f"Cap: Jar_1={Jar_1_cap}L, Jar_2={Jar_2_cap}L, Target={target}L")

while True: #operations to perform
print("\n1. JAR 1 TO JAR 2")
print("2. JAR 2 TO JAR 1")
print("3. EMPTY JAR 1")
print("4. EMPTY JAR 2")
print("5. FILL JAR 1")
print("6. FILL JAR 2")
print("7. EXIT")

Target(Jar_1, Jar_2, target) # called the method and passed these values

move = int(input("Enter move 1-7 : ")) # used Switch cased for interaction

match move:
case 1: # JAR 1 TO JAR 2
pour = min(Jar_1, Jar_2_cap - Jar_2)
Jar_2 += pour
Jar_1 -= pour
print("MOVED JAR 1 TO JAR 2")

case 2: # JAR 2 TO JAR 1
pour = min(Jar_2, Jar_1_cap - Jar_1)
Jar_1 += pour
Jar_2 -= pour
print("MOVED JAR 2 TO JAR 1")

case 3: # EMPTY JAR 1
Jar_1 = 0
print("EMPTY JAR 1")

case 4: # EMPTY JAR 2
Jar_2 = 0
print("EMPTY JAR 2")

case 5: # FILL JAR 1
Jar_1 = Jar_1_cap
print("FILL JAR 1")

case 6: # FILL JAR 2
Jar_2 = Jar_2_cap

print("FILL JAR 2")

case 7: # EXIT
print("EXIT")
break

case _:
print("Invalid move!")

if Target(Jar_1, Jar_2, target):
break
