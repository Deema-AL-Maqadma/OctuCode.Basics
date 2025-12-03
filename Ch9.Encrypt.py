# مشروع تشفير الكلمات باستخدام مفتاح عبارة عن الرقم 
import string
def encrypt(message,shift):
    alphabet = string.ascii_lowercase
    encrypt_message=" "
    for letter in message:
        if letter.lower() in alphabet:
            original_position = alphabet.index(letter.lower())
            new_position = (original_position + shift)% 26 # للتشفير بنجمع و لفك التشفير نطرح
            encrypted_letter = alphabet[new_position]
            #حافظ على حالة الحرف
            if letter.isupper():#اذا كان الحرف كبير عند التشفير هطبعه كبير
                encrypted_letter=encrypted_letter.upper()

            encrypt_message += encrypted_letter # ضيف الحرف المشفر للمسج المشفرة

        else:
            encrypt_message+= letter # في حال ما كان المدخل حرف نطبعه فالتشفير كما هو
    print(encrypt_message)
    
# ناخذ الرسالة من المستخدم وعدد حروف الانتقال (المفتاح)
user_message = input("Enter a message : \n")
shift_number = int(input("Enter a shift number : \n"))

print("--->>> The Encrypt Message <<<---")
encrypt(message= user_message,shift= shift_number)
print("*******************************************")