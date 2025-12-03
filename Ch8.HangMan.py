import random
words=["good","bad","ugly"]
random_word = random.choice(words)#لاختيار كلمة عشوائية من لاقائمة
display = ["_"]*len(random_word)#اعرض مسافات بنفس عدد الحروف
print(' '.join(display))#لعرض المسافات ككلمة وليس كائمة
lives=6 # عدد المحاولات المسموحة
while '_'in display and lives>0 :
    gessed=input("Please gessed a letter :  ").lower()#اطلب تخمين كلمة
    if gessed  not in random_word:
        lives-=1
    #لوالحرف صح بدله مع المسافة واعرض
    for position in range(len(random_word)):
        if random_word[position]== gessed:
            display[position]=gessed

    print(display)
    print(f"---> You have {lives} more tries ")

#بعد اللوب بدي اعرف السبب يلي خلاه يطلع منه اما الفوز او الخسارة
if lives==0:
    print("""
       --->>> You lose !
          
          +----+
             |     |
            0      |
          / | \    |
          /   \    |
                   |
          =========
          """)
else :
    print("""
          ****************
       --->>> You WIN !
          ****************
          """)
