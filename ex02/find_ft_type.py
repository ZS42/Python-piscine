def all_thing_is_obj(object: any) -> int:
#your code here
#isinstance() returns true if exact type or its inheriting subclasses
#type() returns the type of an object
    if(isinstance(object, list)):
        print(f"List : {type(object)}")
    elif(isinstance(object, tuple)):
        print(f"Tuple : {type(object)}")
    elif(isinstance(object, set)):
        print(f"Set : {type(object)}")
    elif(isinstance(object,dict)):
        print(f"Dict : {type(object)}")
    elif(isinstance(object,str)):
        print(f"{object} is in the kitchen : {type(object)}")
    else:
        print("Type not found")
        return 42
    return 0
