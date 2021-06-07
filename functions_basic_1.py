#1
def number_of_food_groups():
    return 5
# i predict print "5"
# it is right prediction
print(number_of_food_groups())


#2
def number_of_military_branches():
    return 5
# i predict crash because there is no function "number_of_days_in_a_week_silicon_or_triangle_sides"
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#i got it right

#3
def number_of_books_on_hold():
    return 5
    return 10
#i predict "5" because return 10 will be ignored after return 5 and it wont crash because its part of the function 
print(number_of_books_on_hold())


#4
def number_of_fingers():
    return 5
    print(10)
# i predict print "5" because print(10) line never gets reached
print(number_of_fingers())
# easy and i got it right

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
# i predict print None because by default if not specified return type then its None which is equivalent to null or undefined
print(x)
#easy right

#6
def add(b,c):
    print(b+c)
# i predict crash because we are adding None 
print(add(1,2) + add(2,3))
# i had my doubts on this because i thought None was gonna be the return but i knew that you cant add values that are not there and computer would have troubles on operating on two values that are aren't there

#7
def concatenate(b,c):
    return str(b)+str(c)
# i predict 25
print(concatenate(2,5))

# easy win 
#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
# i predict 100 and then 10
# easy money i am right
print(number_of_oceans_or_fingers_or_continents())


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
# my prediction is that its gonna be 7 and then 14 and then 21
#and i am right
#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#its obviously 8
#and i am right
#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
#i predict 500 then 500 then 300 then 500
#and i got it right

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
#i predict same output as the previous problem
# and yes it is indeed


#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
#i predict 500 500 300 300
#got it right

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#prediction is print 1 3 and then 2
#right predictions

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
#i predict 1 3 5 and then 10
#correct