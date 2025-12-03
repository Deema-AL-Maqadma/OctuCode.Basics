# مشروع كتابة الاسماء كاملة وىاختصاراتها
names=input("Enter the first and the last name of your frinds separated by a comma :").split(", ")
abbreviated_names=[]
print("--->>> Full Names :")
for name in names:
    name_parts=name.split()#لتقسيم اجزاء الاسم
    print(name_parts)
    first_name=name_parts[0]# لاحضار الجزء الاول من الاسم
    last_name=name_parts[1]# لاحضار الجزء الثاني من الاسم
    first_initial=first_name[0]#لاحضار الحرف الاول من كل جزء
    last_initial=last_name[0]
    abbreviation=first_initial+"."+last_initial+"."
    abbreviated_names.append(abbreviation)
print("--->>> Abbreviated Names :")
for x in abbreviated_names:
    print(x)
print("**************************************")
my_name="Deema"
print(my_name[0:5:1])# slicing
print(my_name[:5:1])# slicing هيبدا من البداية
print(my_name[::1])# slicingهيبدا من الاول للاخر
print(my_name[::-1])# slicing يعتبر القسم الاول النهاية والقسم الوسط البداية ويتحرك بالسالب يعني بالعكس
print("**************************************")
# اخذ جملة من المستخدم وطباعتها بالعكس
sentence=input("Enter a sentance :")
word=sentence.split()# تقسيم لكلمات الجملة وتخزينها في قائمة
print(word)#يطبع قائمة بكلمات الجملة
reversed_word=word[::-1]
print(reversed_word)# القائمة معكوسة
reversed_sentence=" ".join(reversed_word)# لتحويل القائمة المعكوسة لجملة
print("Reversed sentence : ",reversed_sentence)
