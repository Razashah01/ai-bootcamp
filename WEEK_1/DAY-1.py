# # print("Hello world")

# # video lec-1

#                                     ## OOP CONCEPT IN PYTHON 
# class employee:  #class define
#     num_of_emps= 0
#     raise_amount = 1.04
#     def __init__(self,first,last,pay):  # constructor
#         self.first= first
#         self.last= last
#         self.pay=pay
#         self.email=first +'.'+ last + '@company.com'
#         employee.num_of_emps += 1 

#     def fullname(self):
#         return '{} {}'. format(self.first,self.last)  # function for calling employee full name.
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#     @classmethod
#     def set_raise_amount(cls,amount):
#         cls.raise_amount= amount
#     @classmethod
#     def from_string (cls,emp_str):
#         first, last, pay = emp_str.split('-')
#         return cls(first,last,pay)
#     @staticmethod  # static method 
#     def is_workday(day):
#         if day.weekday == 5 or day.weekday == 6:
#             return False
#         return True

# emp_1= employee('raza','shah',90000)
# emp_2= employee('Ali','Imam',70000)
# emp_3= employee('hassan','Imam',80000)
# emp_4= employee('Ali','naqi',980000)
# emp_5= employee('Muhammad','taqi',120000)



# # print(emp_1.email)
# # print(emp_2.email)
# # print(emp_1.fullname()) 
# # print(emp_2.fullname()) 

#                                             # Python OOP Tutorial 2: Class Variables

# # emp_1.raise_amount = 1.05

# # print(emp_1.__dict__)  ## dict shows the dictionary of emp_1

# # print(employee.raise_amount)

# # print(emp_1.raise_amount)
# # print(emp_2.raise_amount)
# # print(emp_3.raise_amount)
# # print(emp_4.raise_amount)

# print("Total Number of Employees is:",employee.num_of_emps)
 
#                                  #Python OOP Tutorial 3: classmethods and staticmethods

# # emp_str_1='syed-raza-65000'
# # emp_str_2='ali-raza-55000'
# # emp_str_3='hassan-raza-75000'

# # first, last, pay= emp_str_1.split('-')
# # emp_4= employee(first,last,pay)

# # print(emp_4.pay)
# # print(emp_4.email)

# #static method to check working day or holiday. 
#  #function is done

# # import datetime    
# # my_date= datetime.date(2026,10,18)
# # print(employee.is_workday(my_date))




#                                 # Python OOP Tutorial 4: Inheritance - Creating Subclasses

# class developer(employee):
#     raise_amount = 1.10
#     def __init__(self, first, last, pay,prog_lang):
#         super().__init__(first, last, pay)
#         self.prog_lang = prog_lang
# dev_1= developer('john','doe', 75000,'pyhton' )
# dev_2= developer('jason','white', 115000,'java')

# class manager(employee):
#     raise_amount= 1.07
#     def __init__(self, first, last, pay,employees=None):
#         super().__init__(first, last, pay)
#         if employees is None: 
#             self.employees =[]
#         else: 
#             self.employees = employees

#     def add_emp(self, emp):
#         if emp not in self.employees:
#             self.employees.append(emp)

#     def remove_emp(self, emp):
#         if emp in self.employees:
#             self.employees.remove(emp)

#     def print_emps(self):
#         for emp in self.employees:
#             print('-->',emp.fullname())
# mang_1= manager('sue','doe', 75000,[emp_4])
# mang_2= manager('michelle','micky', 75000,[emp_1])


# # print(mang_1.email)
# mang_1.add_emp(dev_1)
# mang_2.add_emp(dev_2)

# # print(mang_2.employees)


# # print(dev_1.email)
# # print(dev_2.email)

# # print(help(developer))   check out
# # print(dev_1.pay)
# # dev_1.apply_raise()
# # print(dev_1.pay)

# # print(dev_1.prog_lang)
# print(isinstance(developer, employee))



#                                     ##     Python OOP Tutorial 5: Special (Magic/Dunder) Methods


# class employee:  #class define
#     num_of_emps= 0
#     raise_amount = 1.04
#     def __init__(self,first,last,pay):  # constructor
#         self.first= first
#         self.last= last
#         self.pay=pay
#         self.email=first +'.'+ last + '@company.com'
#         employee.num_of_emps += 1 

#     def fullname(self):
#         return '{} {}'. format(self.first,self.last)  # function for calling employee full name.
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)
#     def __repr__(self):  #dunder method / special method
#         return "employee ('{}', '{}' ,'{}','{}' )". format(self.first,self.last,self.pay,self.email)
#     def __str__(self):   #dunder method 
#         return '{} - {}'.format(self.fullname() , self.email)

# emp_1= employee('raza','shah',90000)
# emp_2= employee('Ali','Imam',70000)

# # print(emp_1)
# # print(emp_2)
# # print(repr(emp_1))
# # print(str(emp_1))

# print(len(emp_1.fullname()))


                                    ## Python OOP Tutorial 6: Property Decorators - Getters, Setters, and Deleters
# class employee:
#     def __init__(self,first,last):
#       self.first= first
#       self.last=last
#     #   self.email= first + '.'  + last +'@company.com'
#     @property
#     def email(self):
#        return '{}.{} @company.com'. format(self.first,self.last)    ## decortore for changing the email(name) as we change the first name
#     @property
#     def fullname(self):  ## decortore for changing the first name
#        return '{} {}'.format(self.first,self.last)
#     @fullname.setter
#     def fullname(self,name): # setter property for changing the full name
#         first,last = name.split(' ')
#         self.first=first
#         self.last=last
#     @fullname.deleter
#     def fullname(self): # deleter property for deleting the full name
#        print('Full Name Deleted!')
#        self.first=None
#        self.last=None
            
        
    
# emp_1= employee('john','doe')

# print(emp_1.first)
# print(emp_1.fullname)
# print(emp_1.email)

# emp_1.fullname= 'raza shah'
# print(emp_1.first)
# print(emp_1.fullname)
# print(emp_1.email)

# del emp_1.fullname


name = "Raza"
city = "Lahore"
Years_of_study = 4

print(f"My name is: {name}, I'm from : {city}, I studied for :{Years_of_study} years")

if(years_of_study > 3):
        print("senior student")
else:
        print("Junior Student")