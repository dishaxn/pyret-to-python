def moon_weight(earth_weight: int) -> int:
    return earth_weight * (1/6)
    
print(moon_weight(75))
print(moon_weight(45))
print(moon_weight(67))
print(moon_weight(60))

def add_shipping(order_amt: float) -> float:
    """add shipping cost to order total"""
    if order_amt <= 10:
        return order_amt + 4
    elif order_amt <= 30:
        return order_amt + 8
    else:
        return order_amt + 12
        
print(add_shipping(25))
print(add_shipping(55))
print(add_shipping(16))
print(add_shipping(18))
print(add_shipping(4))

def myfunc(age):
 if age >= 18:
  return "You are eligible to vote"
 else:
   return "You are not eligible to vote"

print(myfunc(19))
print(myfunc(13))

def compare(x,y):
    if x > y:
        print("x is greater than y")
    else:
        if x < y:
            print("x is lesser then y")
        else:
            print("x and y are equal")
            
compare(10,9)
compare(9,10)
compare(10,10)

words = ["banana", "bean", "carrot", "leaf"]
print(words)

print(words)
print(words[0])
print(words[3])
print(len(words))

data = [10, 21, 34, 0, -2, -13, 46]

print(data)
print(len(data))
print(data[2])
print(data.index(34))
print(data.index(10))
print(data.index(-2))

def my_sum(l: list):
    run_total = 0
    for num in l:
        run_total = run_total + num
    return(run_total)
    
print(my_sum([1, 2, 3]))
print(my_sum([2, 5, -8, 9]))

def all_z_words(wordlist : list) -> list:
    """produce list of words from the input that contains z"""
    zlist = []
    for wd in wordlist:
        if "z" in wd:
            zlist = zlist + [wd]
    return(zlist)
    
print(all_z_words(["horse", "zebra", "quiz", "cat"]))
print(all_z_words(["cans", "zoo", "octopus", "animal"]))
