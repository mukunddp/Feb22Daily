# var = 15                # int
# variable = "word"       # str
# a = True                # bool
# b = False               # bool
# c = 15.5                # flaot
#
# # different ways to declare a variable
# _name_1655_hasbds = 'Mukund Parve'
# a_z_A_Z_0_9 = 15
#
# age = 18
# Age = 18
# Name = 'Mukund'
# NAME = 'Mukund Parve'
#
# print(NAME)             # ctrl + /
# print(Name)
#
# # Doc String
#
# doc = """
#     This is a doc string
#     and will be used to comment multiple line
# """
# print(doc)
# del doc             # delete a variable
# # a = 451
# print(doc)


# # Input
# name = input('This is input :')    #'15.5'
# print('This is data stored in name :', name)
# print('This is data stored in name :'+ name)  # concatinate
#
# print(type(name))
# age = int(input('Type your age: '))
# print(age + 5)
# print(type(age))
# age = bool(int(input('Type your age: ')))
# print(age)
# print(type(age))




# print(name + 'Mukund', sep='#')           #
# print(age, 'Mukund', sep='#')
# #
# print(institute, name, sep=' ')    #
# print(address, end='\n')      #
# # # end = '\n'
# sep = ' '
# print('I am ', name , ' My age is', age, 'I am learinig python from', institute)


name = 'Mukund'
age = 25
institute = 'Tech Amplifiers'
address = 'Narhe, Pune'

# print(f'I am Mukund Parve, my age is 25. I am teaching Python in Tech Amplifiers which is situated in Narhe, Pune')
print(f'I am {name}, my age is {age}. I am teaching Python in {institute} which is situated in {address}')
# print(f"""I am {name}, my age is {age}.
#  I am teaching Python in {institute}
#  which is situated in {address}""")