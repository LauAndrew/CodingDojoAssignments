string = "It's thanksgiving day. It's my birthday, too"
print string.find("day")
string = string.replace("day", "month")
print string
#Find and Replace

x = [2,54.-2,7,12,98]
print min(x)
print max(x)
#min and max
#what about -2?

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0], x[len(x) - 1]
#First and Last

x = [19,2,54,-2,7,12,98,32,10,-3,6]
print x
first_list = x[:len(x)/2] 
second_list = x[len(x)/2:]
print first_list
print second_list
second_list.insert(0,first_list)
print second_list
#new list