total_perc=int(input("Enter your degree total score percentage: "))

message=""
if total_perc>=75:
    message="Excellent"
elif total_perc < 75 and total_perc >= 50:
    message="Very Good"    
else:
    message="Neeed improvement"    

print(message) 

#(visa_valid == True and uae_license == True) or (gcc_license == True)
#empty string-default boolean value false
#0-false,non-zero-true
#[]-false,[2,4]-true
name="Upc"
if name:
    print(name)
else:
    print("name is empty")



