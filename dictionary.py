#Dictionaries are used to store data values in key:value pairs.
dic = {
    'vehicle':'car',
    'color':'blue',
    'year':2010
}
print(dic['vehicle'])   #o/p car
x = dic.get("color")
print(x)                #o/p blue

#combine two lists to dictionary
a = [1,2,3]
b = [9,8,7]
com = dict(zip(a,b))
print(com)

#list as value
c = {1:2, 2:['hi','hemlo']}
print(c[2][1])
