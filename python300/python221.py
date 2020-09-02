#221
def print_reverse(x):
    print(x[::-1])

#222
def print_score(scorelist):
    print(sum(scorelist)/len(scorelist))

#223
def print_even(evenlist):
    for i in evenlist:
        if i%2==0:
            print(i)

#224
def print_keys(mydict):
    for i in mydict.keys():
        print(i)

print_keys({"과일":"사과","채소":"토마토"})

#225
my_dict = {"10/26" : [100, 130, 100, 100],
           "10/27" : [10, 12, 10, 11]}
def print_value_by_key (my_dict, key) :
    print(my_dict[key])

print_value_by_key(my_dict, "10/26")

#226
def print_5xn(line):
    chunk_num = int(len(line) / 5)
    for x in range(chunk_num + 1):
        print(line[x * 5: x * 5 + 5])

#227
def print_mxn(line, num):
    chunk_num=int(len(line)/num)
    for x in range(chunk_num+1):
        print(line[x*num:x*num+num])

#228
def calc_monthly_salary(annual_pay) :
    monthly_pay = int(annual_pay / 12)
    return monthly_pay
#int로 casting 하면 floating point 숫자가 다 없어진다.

#229
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(a=100, b=200)

#230
def my_print (a, b) :
    print("왼쪽:", a)
    print("오른쪽:", b)

my_print(b=100, a=200)
#parameter 이름을 specify 하면 순서랑 관계 없이 특정한 parameter로 값이 붙는다.



