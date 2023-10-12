# class employee with fn, ln, sal, email
# func to change salary and print employee data
class Employee():

    def __init__(self, fn, ln, salary):
        self.fn = fn
        self.ln = ln
        self.salary = salary
        self.email = fn+"."+ln+"@test.com"

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
        self.languages.extend(languages)
        # for language in languages:
        #     self.languages.append(language)

# # emp1 smith, salary = $100k
# emp1 = Employee("bob emp1", "smith", 100000)
# print (emp1)

# # emp1 new salary = $105k
# emp1.change_salary(105000)
# print ("---------------")
# print (emp1)

# emp1 developer with java, c++ languages
# dev1 = Developer("bob dev1", "smith", 100000, ["java", "c++"])
# print ("---------------")
# print (dev1)
# #emp1 developer add languages python
# dev1.add_languages(["python", "javascript"])
# print ("---------------")
# print (dev1)

# #dev1 change salary to $120k
# dev1.change_salary(120000)
# print ("---------------")
# print (dev1)

# # Multiple Inheritance

class GrandPa():
    def grandPaFunc(self, msg):
        print (f"I am a {msg} at Grandpa's home")

class Parent(GrandPa):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg

    def parentFunc(self):
        print (f"I am a {self.msg} at Parent's home")

class GrandSon(Parent):
    def sonFunc(self, msg):
        print (f"I am a {msg} at GrandSon's home")

# son = GrandSon("grandson")
# son.grandPaFunc("grandson")
# son.parentFunc()
# son.sonFunc("grandson")

# parent = Parent("parent")
# parent.grandPaFunc("parent")
# parent.parentFunc()

# gpa = GrandPa()
# gpa.grandPaFunc("grandpa")


