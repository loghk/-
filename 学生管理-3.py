
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
        count.append(int(i['ѧ��']))
    print(count)
    for n in range(1,max):
        s1 = students_info[n].get('ѧ��')
        s2 = students_info[n+1].get('ѧ��')
        if  int(s1)<int(s2):
            temp = students_info[n+1]
            students_info[n+1] = students_info[n]
            students_info[n] = temp


    return students_info
'''
def show_all():
    print('\t\tѧ��\t\t\t����\t\t\t�༶\t\t\t�ɼ�1\t\t�ɼ�2\t\t�ɼ�3')
    for i in students_info:
        print('\t\t'+i['ѧ��']+'\t\t'+i['����']+'\t\t'+i['�༶']+'\t\t\t'+i['�ɼ�1']+'\t\t\t'+i['�ɼ�2']+'\t\t\t'+i['�ɼ�3'])

def show_solo(i):
    print('\t\tѧ��\t\t����\t\t�༶\t\t�ɼ�1\t\t�ɼ�2\t\t�ɼ�3')
    print('\t\t'+i['ѧ��']+'\t\t'+i['����']+'\t\t'+i['�༶']+'\t\t'+i['�ɼ�1']+'\t\t\t'+i['�ɼ�2']+'\t\t\t'+i['�ɼ�3'])

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
            if i['ѧ��'] != num:
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
    change_student_info = input('������Ҫ���ĵ�ѧ��ѧ��:')
    return change_student_info
def student_del():
    print('***********************************************************')
    print('\n')
    del_student_info = input('������Ҫɾ����ѧ��ѧ��:')
    return del_student_info
def student_add():
    student_info = {}
    while True:
        student_info['ѧ��'] = input('����Ҫ��ӵ�ѧ��ѧ��:')
        student_info['����'] = input('����Ҫ��ӵ�ѧ������:')
        student_info['�༶'] = input('����Ҫ��ӵ�ѧ���༶:')
        student_info['�ɼ�1'] = input('����Ҫ��ӵ�ѧ���ɼ�1:')
        student_info['�ɼ�2'] = input('����Ҫ��ӵ�ѧ���ɼ�2:')
        student_info['�ɼ�3'] = input('����Ҫ��ӵ�ѧ���ɼ�3:')
        s1 = student_info['�ɼ�1']
        s2 = student_info['�ɼ�2']
        s3 = student_info['�ɼ�3']
        if check_xuehao(student_info['ѧ��']):
            if check_name(student_info['����']):
                if check_score(int(s1),int(s2),int(s3)):
                    if check_repeat(student_info['ѧ��']):
                        if s1 != '' or s2 != '' or s3 != '':
                            if check_score2(s1,s2,s3):
                                return student_info
                            else:print('�ɼ�����Ϊ������!')
                        else:print('�ɼ�����Ϊ��!')
                    else:print('ѧ���ѱ�ռ��!')
                else:print('�ɼ�������0~100֮��!')
            else:print('��������Ϊ������!')
        else:print('ѧ�ű���Ϊ������!')
def main():
    print('***********************************************************')
    print('                           ѧ������ϵͳ                      ')
    print('            1.���ѧ����Ϣ                   2.ɾ��ѧ����Ϣ    ')
    print('            3.����ѧ����Ϣ                   4.����ѧ����Ϣ    ')
    print('            5.��ʾ�Ѵ��ѧ����Ϣ              6.�˳�����')
    print('***********************************************************')
def oper_1():  # ���ѧ����Ϣ�Ĳ���
    os.system('cls')
    students_info.append(student_add())
    return students_info
def oper_2():  # ɾ��ѧ����Ϣ�Ĳ���
    os.system('cls')
    if students_info:
        n = student_del()
        for i in students_info:
            for value in i.values():
                if n == value:
                    students_info.remove(i)
                    break
    else:
        print('ϵͳ��û��ѧ����Ϣ!')
def oper_3():  # ����ѧ����Ϣ�Ĳ���
    os.system('cls')
    if students_info:
        n = student_change()
        for i in students_info:  # ���Ҫ���ĵ�ѧ����Ϣ
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
            student_info['ѧ��'] = input('������ĺ��ѧ��:')
            student_info['����'] = input('������ĺ������:')
            student_info['�༶'] = input('������ĺ�İ༶:')
            students_info.append(student_info)
        elif flag == 0:
            print('û�и�����Ϣ!')
    else:
        print('û��ѧ����Ϣ!')
    return student_info
def oper_4():  # ����ѧ����Ϣ�Ĳ���
    print('***********************************************************')
    print('\n')
    # global sign
    if students_info:
        num = input('����Ҫ���ҵ�ѧ��ѧ��:')
        for i in students_info:
            if num in i.values():
                show_solo(i)
                flag = 0
                break
            if num not in i.values():
                flag = 1
        if flag == 1:
            print('û��Ҫ���ҵ�ѧ����Ϣ!')
    else:
        print('û��ѧ����Ϣ!')
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
        first_get = input('������Ҫִ�еĲ���:')
        if first_get == '1':  # ����ѧ����Ϣ
            oper_1()
            os.system('cls')

        elif first_get == '2':  # ɾ��ѧ����Ϣ
            oper_2()

        elif first_get == '3':  # ����ѧ����Ϣ
            print(oper_3())

        elif first_get == '4':  # ����ѧ����Ϣ
            oper_4()

        elif first_get == '5':  # ��ʾ�Ѵ����ѧ����Ϣ
            if len(students_info) == 0:
                print('\t\t��ǰû��ѧ����Ϣ��')
                print('\t\t�����ѧ����Ϣ����ѡ��')
                input()
            else:
                show_all()
                input()
                os.system('cls')

        elif first_get == '6':  # �˳�ϵͳ
            with open(filename, 'w') as f_n:
                json.dump(students_info, f_n)
                exit()
else:
    while 1:
        #if students_info:
         #   print(students_info[0])
        main()
        first_get = input('������Ҫִ�еĲ���:')
        if first_get == '1':  # ����ѧ����Ϣ
            oper_1()
            os.system('cls')


        elif first_get == '2':  # ɾ��ѧ����Ϣ
            oper_2()

        elif first_get == '3':  # ����ѧ����Ϣ
            print(oper_3())

        elif first_get == '4':  # ����ѧ����Ϣ
            oper_4()

        elif first_get == '5':  # ��ʾ�Ѵ����ѧ����Ϣ
            if len(students_info) == 0:
                print('\t\t��ǰû��ѧ����Ϣ��')
                print('\t\t�����ѧ����Ϣ����ѡ��')
                input()
            else:
                show_all()
                input()
                os.system('cls')

        elif first_get == '6':  # �˳�ϵͳ
            with open(filename, 'w') as f_n:
                json.dump(students_info, f_n)
            exit()




