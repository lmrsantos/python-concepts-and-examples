# class employee:
#     def __init__(self, fn, ln, sal):
#         self.fn = fn
#         self.ln = ln
#         self.sal = sal
#         self.email = fn+ln+'@test.com'

#     def changesal (self, sal):
#         self.sal = sal

# #ENHERITANCE
# class developer(employee):
#     def __init__(self, fn, ln, sal, proglang):
#         super().__init__(fn, ln, sal)
#         self.progLang = proglang

#     def addproglang(self, progLang):
#         self.progLang += [progLang]

# emp1 = employee('lm', 'santos', 263000)
# print (emp1.sal, emp1.email)

# emp1.changesal(380000)

# print (emp1.sal)

# dev1 = developer('carol', 'azevedo', 410000, ['Cobol'])

# print (dev1.sal, dev1.fn, dev1.progLang)

# dev1.changesal(540000)

# dev1.addproglang('Java')

# print (dev1.sal, dev1.fn, dev1.ln, dev1.email, dev1.progLang)


#class employee with fs, ln, sal, email / option to change salary
# class employee():
#     def __init__(self, fn, ln, sal):
#         self.fn = fn
#         self.ln = ln
#         self.sal = sal
#         self.email = fn+ln+'@test.com'

#     def changeSal(self, sal):
#         self.sal = sal

# #class developer with proglang / option to add proglang
# class developer(employee):
#     def __init__(self, fn, ln, sal, progLang):
#         super().__init__(fn, ln, sal)
#         self.progLang = [progLang]

#     def addproglang(self, progLang):
#         self.progLang += [progLang]

# #instanciate empl1
# emp1 = employee('emp1', 'smith', 100000)
# print (emp1.sal)

# #change emp1 salary
# emp1.sal = 120000
# print (emp1.sal)

# #instanciate dev1
# dev1 = developer('mike', 'withwork', 90000, 'Java')
# print (dev1.sal, dev1.progLang)

# #add progLang
# dev1.addproglang('Python')
# print (dev1.progLang)

# #change dev1 salary
# dev1.changeSal(85000)
# print (dev1.sal)


# class employee with fn, ln, sal, email
# func to change salary and print employee data
class Employee():

    def __init__(self, fn, ln, salary):
        self.fn = fn
        self.ln = ln
        self.salary = salary
        self.email = fn+"."+ln+"test.com"

    def __str__(self):
        return (f'FN: {self.fn}\nLN: {self.ln}\nSalary: {self.salary}')
    
    def change_salary(self, salary):
        self.salary = salary

# class with languages that developer knows 
# func to allow add new languages
class Developer (Employee):
    def __init__(self, fn, ln, salary, languages):
        super().__init__(fn, ln, salary)
        self.languages = languages

    def __str__(self):
        return super().__str__() + f'\nLanguages: {self.languages}'

    def add_languages(self, languages):
        for language in languages:
            self.languages.append(language)

# emp1 smith, salary = $100k
emp1 = Employee("bob emp1", "smith", 100000)
print (emp1)

# emp1 new salary = $105k
emp1.change_salary(105000)
print ("---------------")
print (emp1)

# emp1 developer with java, c++ languages
dev1 = Developer("bob dev1", "smith", 100000, ["java", "c++"])
print ("---------------")
print (dev1)
#emp1 developer add languages python
dev1.add_languages(["python", "javascript"])
print ("---------------")
print (dev1)

#dev1 change salary to $120k
dev1.change_salary(120000)
print ("---------------")
print (dev1)
