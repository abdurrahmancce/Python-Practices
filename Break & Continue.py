# Break 
num = 1
while num <= 10:
 print(num)
 num = num + 1

 if num == 5:
  break
print("Breaking the loop at num =", num)
print("Loop ended, final num is:", num)

print("\n")

# Continue 
num=1
while num <= 10:
    num =num + 1

    if num == 5: # This will skip the rest of the loop when num is 5
        continue 
    print(num)

print("Loop ended, final num is:", num)