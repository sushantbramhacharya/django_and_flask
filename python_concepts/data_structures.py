#Loop Using Range
for x in range(5):
    #[0,1,2,3,4]
    print(x)

print()

#List Data Structure
list=[1,2,6,3,7,5]
for x in list:
    print(x)
print()

#Heterogenous Lists
list2=[1,"Hello",True,23.42,3,7,5]
print(list2)
print()
for item in list2:
    print(item)
print()

#Odd Even Program in List
list3=[2,4,63,4,7,46,87,45,2]
for item in list3:
    if item %2!=0:
        print(item)

print()
list3.sort(reverse=True)
list3.pop()
print(list3)

#Dictionary
dict=[
    {
        "name": "Ram",
        "age": 10,
        "location": "Kathmandu",
        "subject": ["math", "nepali", "science"],
        "college": {
            "name": "LEC",
            "phone": "1234",
            "faculty": ["BCA", "BCT", "BCE"]
        }
    },
    {
        "name": "Shyam",
        "age": 20,
        "location": "Lalitpur",
        "subject": ["EPH", "Social", "English"],
        "college": {
            "name": "Patan Multiple",
            "phone": "23213",
            "faculty": ["BCA", "Bsc CSIT", "BBA", "MCA"]
        }
    },
    {
        "name": "Hari",
        "age": 22,
        "location": "Bhaktapur",
        "subject": ["math", "physics", "chemistry"],
        "college": {
            "name": "Khwopa College",
            "phone": "9876",
            "faculty": ["BSc", "BBA", "BE Civil"]
        }
    },
    {
        "name": "Sita",
        "age": 19,
        "location": "Pokhara",
        "subject": ["biology", "chemistry", "english"],
        "college": {
            "name": "Pokhara University",
            "phone": "5678",
            "faculty": ["BSc Nursing", "BPharm", "BBA"]
        }
    },
    {
        "name": "Gita",
        "age": 18,
        "location": "Chitwan",
        "subject": ["accounting", "economics", "business studies"],
        "college": {
            "name": "Chitwan College of Medical Sciences",
            "phone": "4321",
            "faculty": ["MBBS", "BDS", "BSc Nursing"]
        }
    }
]

for item in dict:
    print(item["name"])
    print(item["location"])
    print(item["age"]+15)
    print(item["college"]["name"])
    print("-------------Faculty are:-------------")
    for faculty in item["college"]["faculty"]:
        print(faculty)
    print()
    
# Python Tuple is a collection of Python objects much like a list but Tuples are immutable in nature i.e. the elements in the tuple cannot be added or removed once created. Just like a List, a Tuple can also contain elements of various types.

# Python Set is an unordered collection of data that is mutable and does not allow any duplicate element. Sets are basically used to include membership testing and eliminating duplicate entries.