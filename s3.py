# name = "sara"
# age = 11

# message = name + ' has ' + str(age) + ' years old.'
# print(message)


# name = input('enter your name: ')
# age = input('enter your age: ')
# message = name + ' has ' + age + ' years old.'
# print(message)

# number1 = input('enter a number: ')
# number2 = input('enter a number: ')

# print(int(number1) + int(number2))


# name = input('enter your name: ')
# age = input('enter your age: ')
# message = '%s has %s years old' % (name, age)
# print(message)

# ex1
# برنامه ای بنویسید که نام، نام خانوادگی  و نام پدرتان از ورودی دریافت نماید و
# پیغامی ماشبه زیر نمایش دهد:
# sama jokar's father's name is mohammad

name = input('enter your name: ')
family = input('enter your family: ')
father_name = input("enter your father's name ")
print(name + " " + family + "'s " + "father name is " + father_name)

print("%s %s's father name is %s"%(name, family, father_name))

print(f"{name} {family}'s father name is {father_name}")

# ex2 برنامه ای بنویسید که سه عدد را از ووردی در یافت نماید و
# حاصل عبارت زیر را محاسبه و نمایش دهد
# عدد اول - عدد دوم + عدد سوم
n1 = int(input('enter a number: '))
n2 = int(input('enter a number: '))
n3 = int(input('enter a number: '))
print(n3 + n2 - n1)