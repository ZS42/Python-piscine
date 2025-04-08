ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}
#your code here
#mutable so can just change
ft_list[1] = "World!"
#immmutable but can reassign the whole uple
ft_tuple = ("Hello", "UAE!")
#mutabe but unordered so had to remove all and then add new otherwise order affected
#above is incorrect. Order affected anyway
#ft_set.remove("Hello")
ft_set.remove("tutu!")
#ft_set.add("Hello")
ft_set.add("Abu Dhabi!")
#mutable so can modify value using key
ft_dict["Hello"] = "42 Abu Dhabi!"
print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)