counter = 0
while counter < 100:
    print(counter)
    if counter == 50:
        break
    counter = counter + 1

print("Done")    

counter = 0
while counter < 100:
    counter = counter + 1
    if counter % 3 == 0:
        continue
    print(counter)
    
    

print("Done")    