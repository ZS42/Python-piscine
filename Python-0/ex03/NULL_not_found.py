def NULL_not_found(object: any) -> int:
#your code here
# Why do we check obj is None instead of == None?
# Python has a singleton object None, and we want to check identity, not just value.
# None should only be one thing in memory.
# isinstance is overkill for None, since you're not checking a whole class hierarchy, just checking if it's the exact None object.
    if object is None:
        print(f"Nothing : {object} {type(object)}")
# Because NaN is not equal to anything, not even itself we convert to string which is then comparable
    elif isinstance(object, float) and str(object) == 'nan':
        print(f"Cheese : {object} {type(object)}")
# must explicitly exclude False bc False == 0 otherwise would not reach case of Fake = False
    elif isinstance(object, int) and object == 0 and object is not False:
        print(f"Zero : {object} {type(object)}")
# no need to print value of object as {object} bc it will be empty string. Also tester.py doesnt have this extra empty space
# Empty : <class 'str'>$ now vs Empty :  <class 'str'>$ with {object} so in this case type is enough no need for value
    elif isinstance(object,str) and object == '':
        print(f"Empty : {type(object)}")
    elif isinstance(object, bool) and object is False:
        print(f"Fake : {object} {type(object)}")
    else:
        print("Type not found")
        return 1
    return 0