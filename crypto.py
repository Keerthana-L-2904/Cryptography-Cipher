import onetimepad
from tkinter import *

root = Tk()
root.title("CRYPTOGRAPHY CIPHER CONVERTER")
root.geometry("700x200")  

def encryptMessage():
    plain_txt = entry1.get()
    cipher_txt = onetimepad.encrypt(plain_txt, 'random')    
    entry2.delete(0, END)  
    entry2.insert(0, cipher_txt)
def decryptMessage():
    cipher_txt1 = entry3.get()
    plain_txt1 = onetimepad.decrypt(cipher_txt1,'random')
    entry4.delete(0, END)
    entry4.insert(0, plain_txt1)

label_1 = Label(root, text='Plain Text')
label_1.grid(row=10, column=0)

label_2 = Label(root, text='Encrypted Text')
label_2.grid(row=11, column=0)

label_3 = Label(root, text="Cipher Text")
label_3.grid(row=10, column=2)

label_4 = Label(root, text="Decrypted Text")
label_4.grid(row=11, column=2)


entry1 = Entry(root)
entry1.grid(row=10, column=1, padx=20, pady=10)

entry2 = Entry(root)
entry2.grid(row=11, column=1, padx=20, pady=10)

entry3 = Entry(root)
entry3.grid(row=10, column=3, padx=20, pady=10)

entry3_key = Entry(root)
entry3_key.grid(row=11, column=3, padx=20, pady=10)

entry4 = Entry(root)
entry4.grid(row=11, column=3, padx=20, pady=10)


enc_button = Button(root, text="ENCRYPT", bg="#4CAF50", fg="white", padx=20, pady=10, command=encryptMessage)
enc_button.grid(row=13, column=1, padx=20, pady=20)


dec_button = Button(root, text="DECRYPT", bg="#FF5722", fg="white", padx=20, pady=10, command=decryptMessage)
dec_button.grid(row=13, column=3, padx=20, pady=20)


root.mainloop()

