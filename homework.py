'''1'''
# mydict = {'a1':10 , 'a10' : 7 , 'a2' : 9 , 'a4' : 5 }
# sorted_dict = {}
# sorted_keys = sorted(mydict,key=mydict.get)
# for i in sorted_keys:
#     sorted_dict[i]=mydict[i]
# print(sorted_dict)

'''2'''
# usk = input('enter the key')
# usv = input('enter value')
# dic = {usk:usv}
# print(dic)

'''3'''
# dicti = {'aper' : 12 , 'ynger' : 34, 'egho' : 56  }
# user_key =input('enter the key: ')
# print(user_key in dicti.keys())


'''4'''
# dic = {'a': 50, 'b': 700}
# dict2 = {'c': 400, 'd': 600}
# dic.update(dict2)
# print(dic)

'''5'''
# mydict = {'a':1,'b':2,'c':12}
# total = 1
# for i in mydict:
#     total*=mydict[i]
# print(total)

'''6'''
# dic = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# sorted_dict = {}
# sorted_values= sorted(dic.values())[:2:-1]
# sorted_keys = sorted(dic, key= dic.get)[:2:-1]
# for i,k in zip(sorted_keys,sorted_values):
#     sorted_dict[i] = k

# print(sorted_dict)
'''next homework'''

'''1'''
# dict_students = {}
# for i in range(10):
#     student_name = input('enter the name: ')
#     student_score = int(input('enter studnet scoere in (1-10)'))
#     dict_students[student_name]=student_score
# print(dict_students)

'''2,3'''
# stundents_count = int(input('enter count of stundent: '))
# dict_students = {}
# total = 0
# bad_students = {}
# for i in range(stundents_count):
#     student_name = input('enter the name: ')
#     student_score = int(input('enter studnet scoere in (1-10): '))
#     total+=student_score
#     dict_students[student_name]=student_score
# mijin = total/stundents_count
# print(f'mijin scory {mijin}')
# # 3part
# for i in dict_students:
#     if dict_students[i] < mijin:
#         bad_students[i] = dict_students[i]
# print(f'bad students--> {bad_students}')

'''4'''
# student_count = int(input('enter the count of stundent: '))
# students_andscors = {}

# good_students = {}
# for i in range(student_count):
#     student_name = input('enter the student name: ')
#     student_score = int(input('enter the score: '))
  
#     students_andscors[student_name]=student_score

# for i in students_andscors:
#     if students_andscors[i] >= 5:
#         good_students[i] = students_andscors[i]
# print(good_students)


'''5'''
# student_count = int(input('enter the count of stundent: '))
# students_andscors = {}

# bed_students = {}
# for i in range(student_count):
#     student_name = input('enter the student name: ')
#     student_score = int(input('enter the score: '))
  
#     students_andscors[student_name]=student_score

# for i in students_andscors:
#     if students_andscors[i] <= 5:
#         bed_students[i] = students_andscors[i]
# print(bed_students)

'''6'''

# student_reting = {'rafo':10 , 'aremn' : 8 , 'aram' : 5 , 'artyom' : 9, 'vghul': 3 , 'erik' : 1}
# user_name = input('enter the name : ')
# if user_name in student_reting:
#     print(user_name,  student_reting[user_name])
# else:
#     print('this name is not in students')

'''7'''
## s = 'a,2,b,5,c,8,a,4,e,11'.split(',')
# s = input('enter the tarer tver): ').split(',')
# s_key = []
# s_value = []
# print(s)
# dict_1 = {}
# for i in s:
#     if i.isnumeric():
#         s_value.append(i)
#     else:
#         s_key.append(i)

# for j,k in zip(s_key,s_value):
#     dict_1[j]=k
# print(dict_1)

'''8'''
# dict_word = {}
# # word = 'exercises'
# word = input('enter the word: ')
# word_withoutdublikat = ''
# for i in word:
#     if i not in word_withoutdublikat:
#         word_withoutdublikat+=i

# print(word_withoutdublikat)
# for i in word_withoutdublikat:
#     dict_word[i] = word.count(i) 

# print(dict_word)

'''9'''
# old_list = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}]
# new_list = []

# for i in old_list:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

'''10'''
# user_name = input('Hello enter your name: ')
# print('Which two words traditionally appear onscreen at the termination of a feature film?')'''1'''
# mydict = {'a1':10 , 'a10' : 7 , 'a2' : 9 , 'a4' : 5 }
# sorted_dict = {}
# sorted_keys = sorted(mydict,key=mydict.get)
# for i in sorted_keys:
#     sorted_dict[i]=mydict[i]
# print(sorted_dict)

'''2'''
# usk = input('enter the key')
# usv = input('enter value')
# dic = {usk:usv}
# print(dic)

'''3'''
# dicti = {'aper' : 12 , 'ynger' : 34, 'egho' : 56  }
# user_key =input('enter the key: ')
# print(user_key in dicti.keys())


'''4'''
# dic = {'a': 50, 'b': 700}
# dict2 = {'c': 400, 'd': 600}
# dic.update(dict2)
# print(dic)

'''5'''
# mydict = {'a':1,'b':2,'c':12}
# total = 1
# for i in mydict:
#     total*=mydict[i]
# print(total)

'''6'''
# dic = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
# sorted_dict = {}
# sorted_values= sorted(dic.values())[:2:-1]
# sorted_keys = sorted(dic, key= dic.get)[:2:-1]
# for i,k in zip(sorted_keys,sorted_values):
#     sorted_dict[i] = k

# print(sorted_dict)
'''next homework'''

'''1'''
# dict_students = {}
# for i in range(10):
#     student_name = input('enter the name: ')
#     student_score = int(input('enter studnet scoere in (1-10)'))
#     dict_students[student_name]=student_score
# print(dict_students)

'''2,3'''
# stundents_count = int(input('enter count of stundent: '))
# dict_students = {}
# total = 0
# bad_students = {}
# for i in range(stundents_count):
#     student_name = input('enter the name: ')
#     student_score = int(input('enter studnet scoere in (1-10): '))
#     total+=student_score
#     dict_students[student_name]=student_score
# mijin = total/stundents_count
# print(f'mijin scory {mijin}')
# # 3part
# for i in dict_students:
#     if dict_students[i] < mijin:
#         bad_students[i] = dict_students[i]
# print(f'bad students--> {bad_students}')

'''4'''
# student_count = int(input('enter the count of stundent: '))
# students_andscors = {}

# good_students = {}
# for i in range(student_count):
#     student_name = input('enter the student name: ')
#     student_score = int(input('enter the score: '))
  
#     students_andscors[student_name]=student_score

# for i in students_andscors:
#     if students_andscors[i] >= 5:
#         good_students[i] = students_andscors[i]
# print(good_students)


'''5'''
# student_count = int(input('enter the count of stundent: '))
# students_andscors = {}

# bed_students = {}
# for i in range(student_count):
#     student_name = input('enter the student name: ')
#     student_score = int(input('enter the score: '))
  
#     students_andscors[student_name]=student_score

# for i in students_andscors:
#     if students_andscors[i] <= 5:
#         bed_students[i] = students_andscors[i]
# print(bed_students)

'''6'''

# student_reting = {'rafo':10 , 'aremn' : 8 , 'aram' : 5 , 'artyom' : 9, 'vghul': 3 , 'erik' : 1}
# user_name = input('enter the name : ')
# if user_name in student_reting:
#     print(user_name,  student_reting[user_name])
# else:
#     print('this name is not in students')

'''7'''
## s = 'a,2,b,5,c,8,a,4,e,11'.split(',')
# s = input('enter the tarer tver): ').split(',')
# s_key = []
# s_value = []
# print(s)
# dict_1 = {}
# for i in s:
#     if i.isnumeric():
#         s_value.append(i)
#     else:
#         s_key.append(i)

# for j,k in zip(s_key,s_value):
#     dict_1[j]=k
# print(dict_1)

'''8'''
# dict_word = {}
# # word = 'exercises'
# word = input('enter the word: ')
# word_withoutdublikat = ''
# for i in word:
#     if i not in word_withoutdublikat:
#         word_withoutdublikat+=i

# print(word_withoutdublikat)
# for i in word_withoutdublikat:
#     dict_word[i] = word.count(i) 

# print(dict_word)

'''9'''
# old_list = [{'key1':'value1'},{},{},{'key1':'value1'},{'key2':'value2'}]
# new_list = []

# for i in old_list:
#     if i not in new_list:
#         new_list.append(i)
# print(new_list)

'''10'''
# user_name = input('Hello enter your name: ')
print('Which two words traditionally appear onscreen at the termination of a feature film?')