# Library
your_library=[]
your_library.append(input("Enter the name of a book you own :"))
book=input("Enter the name of a nother book you own (or press 'Enter' to skip): ")
if book:
    your_library.append(book)
    print("Your Library :",your_library)
else:
    print("Your Library :",your_library)
your_wishlist=[]
your_wishlist.append(input("Enter the name of a book you wish to have in future :"))
book=input("Enter the name of a nother book wish to have in future (or press 'Enter' to skip): ")
if book:
    your_wishlist.append(book)
    print("Your Wishlist :",your_wishlist)
else:
    print("Your Wishlist :",your_wishlist)
have_book=input("Enter the name of a  book from your_wishlist that you have in actully quired (or press 'Enter' to skip): ")
if have_book in your_wishlist:
    your_wishlist.remove(have_book)
    your_library.append(have_book)
print("Your Library :",your_library)
print("Your Wishlist :",your_wishlist)
don_book=input("Enter the name of a  book from your_library that you wish to donate (or press 'Enter' to skip): ")
if don_book in your_library:
    your_library.remove(don_book)
print("Final library after Donations :",your_library)