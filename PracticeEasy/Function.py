# function
#(block of code that perform the specific task)
# reduce redundancy(repitation of code)
def calc_sum(a,b):
    sum=a+b
    print(sum)
    return sum
calc_sum(10,20)
calc_sum(10,15)


#def calc_sum(a,b):# parameters
 #   return a+b
#sum=calc_sum(1,2)
#print (sum)

#Average
def calc_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg

calc_avg(1,2,3)
# functions in python
# built in function 
# -> print()
# -> len(),type(),range()
print("aftab afridi") #sep=" "
print("abdul basit") #end ="\n" for next line

print("aftab afridi ", end="")
print("ali khan")

def calc_prod(a,b=2): 
    print(a*b)
    return a*b
calc_prod(1)

cities=["delhi","karachi","swat","peshawar"]
fruits=["apple","mango","banana","peas"]
def print_len(list):
    print(len(list))

def print_list(list):
    for item in list:
        print(item,end=" ")

#print_list(fruits)
#print()

# Waf in which convert usd into pakistani rupees

def converter (usd_val):
    pkr_val=usd_val*304
    print(usd_val,"USD=", pkr_val, "PKR")
    
converter(3)

def calc_fact(n):
    fact=1
    
    for i in range(1,n+1):
        fact*=i
    print(fact)
    
calc_fact(4)
    


