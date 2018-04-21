
import os
import json

filename = 'students_info.json'
students_info = []
student_info = {}
''' def xuehao_sort():
    max = len(students_info)
    count=[]
    #flag = 1
    #n = 0
    for i in students_info:
        count.append(int(i['学号']))
    print(count)
    for n in range(1,max):
        s1 = students_info[n].get('学号')
        s2 = students_info[n+1].get('学号')
        if  int(s1)<int(s2):
            temp = students_info[n+1]
            students_info[n+1] = students_info[n]
            students_info[n] = temp


    return students_info
'''
def show_all():
    print('\t\t学号\t\t\t姓名\t\t\t班级\t\t\t成绩1\t\t成绩2\t\t成绩3')
    for i in students_info:
        print('\t\t'+i['学号']+'\t\t'+i['姓名']+'\t\t'+i['班级']+'\t\t\t'+i['成绩1']+'\t\t\t'+i['成绩2']+'\t\t\t'+i['成绩3'])

def show_solo(i):
    print('\t\t学号\t\t姓名\t\t班级\t\t成绩1\t\t成绩2\t\t成绩3')
    print('\t\t'+i['学号']+'\t\t'+i['姓名']+'\t\t'+i['班级']+'\t\t'+i['成绩1']+'\t\t\t'+i['成绩2']+'\t\t\t'+i['成绩3'])

def check_score(s1,s2,s3):
    if s1<=100 and s1>=0 and s2<=100 and s2>=0 and s3<=100 and s3>=0:
        return True
    else:return False

def check_score2(s1,s2,s3):
    if s1.isdigit():
        if s2.isdigit():
            if s3.isdigit():
                return True
            else:return False
        else:return False
    else:return False

def check_repeat(num):
    if students_info:
        for i in students_info:
            if i['学号'] != num:
                return True
        else:
            return False
    else:
        return True

def check_xuehao(num):
    if num.isdigit():
        return True
    else:
        return False


def check_name(name):
    if name.isalpha():
        return True
    else:
        return False


def student_change():
    print('***********************************************************')
    print('\n')
    change_student_info = input('输入想要更改的学生学号:')
    return change_student_info
def student_del():
    print('***********************************************************')
    print('\n')
    del_student_info = input('输入想要删除的学生学号:')
    return del_student_info
def student_add():
    student_info = {}
    while True:
        student_info['学号'] = input('输入要添加的学生学号:')
        student_info['姓名'] = input('输入要添加的学生姓名:')
        student_info['班级'] = input('输入要添加的学生班级:')
        student_info['成绩1'] = input('输入要添加的学生成绩1:')
        student_info['成绩2'] = input('输入要添加的学生成绩2:')
        student_info['成绩3'] = input('输入要添加的学生成绩3:')
        s1 = student_info['成绩1']
        s2 = student_info['成绩2']
        s3 = student_info['成绩3']
        if check_xuehao(student_info['学号']):
            if check_name(student_info['姓名']):
                if check_score(int(s1),int(s2),int(s3)):
                    if check_repeat(student_info['学号']):
                        if s1 != '' or s2 != '' or s3 != '':
                            if check_score2(s1,s2,s3):
                                return student_info
                            else:print('成绩必须为纯数字!')
                        else:print('成绩不能为空!')
                    else:print('学号已被占用!')
                else:print('成绩必须在0~100之间!')
            else:print('姓名必须为纯文字!')
        else:print('学号必须为纯数字!')
def main():
    print('***********************************************************')
    print('                           学生管理系统                      ')
    print('            1.添加学生信息                   2.删除学生信息    ')
    print('            3.更改学生信息                   4.查找学生信息    ')
    print('            5.显示已存的学生信息              6.退出程序')
    print('***********************************************************')
def oper_1():  # 添加学生信息的操作
    os.system('cls')
    students_info.append(student_add())
    return students_info
def oper_2():  # 删除学生信息的操作
    os.system('cls')
    if students_info:
        n = student_del()
        for i in students_info:
            for value in i.values():
                if n == value:
                    students_info.remove(i)
                    break
    else:
        print('系统里没有学生信息!')
def oper_3():  # 更改学生信息的操作
    os.system('cls')
    if students_info:
        n = student_change()
        for i in students_info:  # 查出要更改的学生信息
            for value in i.values():
                if n == value:
                    flag = 1
                    break
                elif n != value:
                    flag = 0
            if flag == 1:
                break
        if flag == 1:
            print(i)
            for j in students_info:
                for value in j.values():
                    if n == value:
                        students_info.remove(j)
            student_info['学号'] = input('输入更改后的学号:')
            student_info['姓名'] = input('输入更改后的姓名:')
            student_info['班级'] = input('输入更改后的班级:')
            students_info.append(student_info)
        elif flag == 0:
            print('没有该生信息!')
    else:
        print('没有学生信息!')
    return student_info
def oper_4():  # 查找学生信息的操作
    print('***********************************************************')
    print('\n')
    # global sign
    if students_info:
        num = input('输入要查找的学生学号:')
        for i in students_info:
            if num in i.values():
                show_solo(i)
                flag = 0
                break
            if num not in i.values():
                flag = 1
        if flag == 1:
            print('没有要查找的学生信息!')
    else:
        print('没有学生信息!')
    input()
    os.system('cls')
try:
    with open(filename) as f_n:
        students_info = json.load(f_n)
except FileNotFoundError:
    f = open(filename, 'w+')
    f.write("[]")
    f.close()
    while 1:
        main()
        first_get = input('请输入要执行的操作:')
        if first_get == '1':  # 增加学生信息
            oper_1()
            os.system('cls')

        elif first_get == '2':  # 删除学生信息
            oper_2()

        elif first_get == '3':  # 更改学生信息
            print(oper_3())

        elif first_get == '4':  # 查找学生信息
            oper_4()

        elif first_get == '5':  # 显示已储存的学生信息
            if len(students_info) == 0:
                print('\t\t当前没有学生信息！')
                print('\t\t请添加学生信息后再选择！')
                input()
            else:
                show_all()
                input()
                os.system('cls')

        elif first_get == '6':  # 退出系统
            with open(filename, 'w') as f_n:
                json.dump(students_info, f_n)
                exit()
else:
    while 1:
        #if students_info:
         #   print(students_info[0])
        main()
        first_get = input('请输入要执行的操作:')
        if first_get == '1':  # 增加学生信息
            oper_1()
            os.system('cls')


        elif first_get == '2':  # 删除学生信息
            oper_2()

        elif first_get == '3':  # 更改学生信息
            print(oper_3())

        elif first_get == '4':  # 查找学生信息
            oper_4()

        elif first_get == '5':  # 显示已储存的学生信息
            if len(students_info) == 0:
                print('\t\t当前没有学生信息！')
                print('\t\t请添加学生信息后再选择！')
                input()
            else:
                show_all()
                input()
                os.system('cls')

        elif first_get == '6':  # 退出系统
            with open(filename, 'w') as f_n:
                json.dump(students_info, f_n)
            exit()




