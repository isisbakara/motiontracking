

def adder():
    s = 4
    y = 3
    x = s + y
    return x

#This function strips information from strings
def stripper():
    love = "success"
    love.strip("s")
    k= love.strip("s")
    return k

#This function passes in parameters: it will append data to a list
def appendNumbersToList(number):
    Sleepy = [3, 55, 6, 0, 2,22,432]
    Sleepy.append (number)
    return Sleepy




print adder()
print "I am so damn sleepy" + stripper()
print appendNumbersToList("bed time")

