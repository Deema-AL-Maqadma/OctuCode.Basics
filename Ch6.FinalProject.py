# لاختيار نص عشوائي بنستخدم srring module
import random
import string
print(string.ascii_letters)# كل الحروف
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits) # الارقام كنص
print(string.punctuation) #الرموز
print("************************************")
#لازالة كل الرموز المدخلة من الجملة وطباعة الحروف فقط
sentence=input("Please type a sentance :")
new_sentence=""
for x in sentence:#  لوب على الجملة يتحقق من الكاراكتر اذا مش رمز (حرف)ضيفه للجملة الجديدة
    if x not in string.punctuation:
        new_sentence+=x
print("--->>> Here is the same sentance without punctuation : \n",new_sentence)
print("************************************")
numbers=[0,1,2,3,4,5,6,7,8,9]
print(random.choice(numbers))#لاختيار قيمة عشوائية واحدة
print(random.choices(numbers , k = 3))#لاختياراكثر من قيمة عشوائية بناء على قيمة kوممكن يكرر القيمة
print("************************************")
# Final Project ( Password Generator !!!)
print("----->>> Welcome to the Password Generator ! <<<-----")
char=int(input("Enter the total number of characters in the password : "))
letter=int(input("Enter the number of letters in the password :"))
number=int(input("Enter the number of numbers in the password :"))
symbol=int(input("Enter the number of symbols in the password :"))
if (letter+number+symbol)==char:
    letter_random=random.choices(string.ascii_letters,k=letter)
    number_random=random.choices(string.digits,k=number)
    symbol_random=random.choices(string.punctuation,k=symbol)
    new_password=letter_random+number_random+symbol_random
    random.shuffle(new_password) #لتغير الترتيب عشوائيا
    strong_password="".join(new_password)#الكلمة مخزنة كقائمة بحولها لنص عادي باستخدام الميثود جوين
    print("--->>> Strong password :",strong_password)
else:
    print("Invalid input. The sum of letters, numbers, and symbols doesn't match the password length !")

