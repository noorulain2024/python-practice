str = "i am studying python from apna college"
print(str.endswith("ege"))

str = "i am studying python from apna college"
str = str.capitalize()
print(str)

str = "i am a student of apna college and studying python from apna college"
str = print(str.replace("student","developer"))

str = "i am a student of apna college and studying python from apna college"
print(str.find("s"))

str = "i am a student of apna college and studying python from apna college"
print(str.count("college"))

#wap to input users first name and print its length
name = input("enter your name:")
print("enter the length of your name:",len(name))

str = "this is dollar sign $ and this $ is used in america"
print(str.count("$"))


age = 18
if(age>=14):
    print("can vote")
else:
    print("cannot vote")
    
    
    
# lists in python lists are build_in datatype that uses data of different type
student = ["noor", 23.4, "female", "nowshera"]
print(student[0])
student[0] = "noorulain"
print(student)

# methods of list
list = [1,2,3]
list.append(4)
print(list)

list = [4,7,3,2,7,1]
list.sort()
print(list.sort(reverse=True))
print(list)

list = [1,2,3,5,6,7]
list.insert(1,9)
print(list)

list=[1,2,3,4]
list.pop(1)
print(list)

tup= (1,2,3,4,5,5,5,)
print(tup.index(4))


movie1= "change"
movie2= "the"
movie3= "habit"
list = ["change", "the", "habit"]
print(list)

list= [1,2,4]
list_copy= list.copy()
list_copy.reverse()
if(list_copy == list):
    print("palindrome")
else:
    print("not palindrame")
    
toup = ("c", "d", "a", "a", "b","b", "a")
print(toup.count("a"))

# dictionary
dict={
    "name" : "noor",
    "agr" : "26",
    "class" : "bscs",
    "topic": ["dictionary", "set"],
    "age" : (12,14,25,35)
}
print(dict["name"])
print(dict["class"])
print(dict["age"])

student={ 
    "name": "noor",
    "cgpa": {
        "oop": 3.1,
        "data strutre": 2.8,
        "physics": 3.0
    }
         
}
new_dic={"city": "gujranwala"}
student.update(new_dic)
print(student)

collection={1,2,3,4,"hellow", "world"}
print(collection)
print(len(collection))

collection = set()
collection.add(1)
collection.add(2)
collection.add("apnacollege")
collection.remove(2)
print(collection)

set = {1,2,3}
set1 = {3,4,5}
print(set.intersection(set1))





