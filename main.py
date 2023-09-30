import customtkinter
from tkinter import messagebox
from tkinter import *

window = customtkinter.CTk()
window.geometry('300x300')
window.resizable(FALSE,FALSE)

window.config(bg='#000')
window.title('HxH')


gon = PhotoImage(file="gonprime.png")

gon = gon.subsample(2,2)

gonLabel = Label(image=gon, 
                 bg="black"
                 )

gonLabel.place(x=40,
               y=160
               )


font1 = customtkinter.CTkFont(family="Consolas", 
                              size=20, 
                              weight="bold", 
                              slant="roman"
                              ) 


entry = customtkinter.CTkEntry(window, 
                               font=font1,
                               text_color='#9be0d0', 
                               width=280, 
                               height=50
                               )
entry.place(x=10, y=10)


def button_click(number):
    entry.insert(END, number)


def clear():
    entry.delete(0,END)


def calculate():

    try:
        equation = entry.get()
        newEQ = equation.replace('x', '*')
        result = eval(newEQ)
        clear()
        entry.insert(0, result)
    except ZeroDivisionError:
        messagebox.showerror('Erro', 'Can not divide by 0!')
    except:
        messagebox.showerror('Error', 'invalid values!')


b1 = customtkinter.CTkButton(window, command=lambda: button_click('7'),font=font1, text_color='#9be0d0', text='7', fg_color='#000',hover_color='#2a1142', bg_color='#000',border_color='#fff',border_width=2,cursor='hand2', width=60)
b1.place(x=10, y=80)
b2 = customtkinter.CTkButton(window, command=lambda: button_click('8'),font=font1, text_color='#9be0d0', text='8', fg_color='#000',hover_color='#2a1142', bg_color='#000',border_color='#fff',border_width=2,cursor='hand2', width=60)
b2.place(x=80, y=80)
b3 = customtkinter.CTkButton(window, command=lambda: button_click('9'),font=font1, text_color='#9be0d0', text='9', fg_color='#000',hover_color='#2a1142', bg_color='#000',border_color='#fff',border_width=2,cursor='hand2', width=60)
b3.place(x=150, y=80)
b4 = customtkinter.CTkButton(window, command=lambda: button_click('4'),font=font1, text_color='#9be0d0', text='4', fg_color='#000',hover_color='#2a1142', bg_color='#000',border_color='#fff',border_width=2,cursor='hand2', width=60)
b4.place(x=10, y=125)
b5 = customtkinter.CTkButton(window, command=lambda: button_click('5'),font=font1, text_color='#9be0d0', text='5', fg_color='#000',hover_color='#2a1142', bg_color='#000',border_color='#fff',border_width=2,cursor='hand2', width=60)
b5.place(x=80, y=125)
b6 = customtkinter.CTkButton(window, command=lambda: button_click('6'),font=font1, text_color='#9be0d0', text='6', fg_color='#000',hover_color='#2a1142', bg_color='#000',border_color='#fff',border_width=2,cursor='hand2', width=60)
b6.place(x=150, y=125)
b7 = customtkinter.CTkButton(window, command=lambda: button_click('1'),font=font1, text_color='#9be0d0', text='1', fg_color='#000',hover_color='#2a1142', bg_color='#000',border_color='#fff',border_width=2,cursor='hand2', width=60)
b7.place(x=10, y=170)
b8 = customtkinter.CTkButton(window, command=lambda: button_click('2'),font=font1, text_color='#9be0d0', text='2', fg_color='#000',hover_color='#2a1142', bg_color='#000',border_color='#fff',border_width=2,cursor='hand2', width=60)
b8.place(x=80, y=170)
b9 = customtkinter.CTkButton(window, command=lambda: button_click('3'),font=font1, text_color='#9be0d0', text='3', fg_color='#000',hover_color='#2a1142', bg_color='#000',border_color='#fff',border_width=2,cursor='hand2', width=60)
b9.place(x=150, y=170)
b10 = customtkinter.CTkButton(window, command=lambda: button_click('0'),font=font1, text_color='#9be0d0', text='0', fg_color='#000',hover_color='#2a1142', bg_color='#000',border_color='#fff',border_width=2,cursor='hand2', width=60)
b10.place(x=10, y=215)
b11= customtkinter.CTkButton(window, command=lambda: button_click('.'),font=font1, text_color='#9be0d0', text='.', fg_color='#000',hover_color='#2a1142', bg_color='#000',border_color='#fff',border_width=2,cursor='hand2', width=60)
b11.place(x=80, y=215)
b12 = customtkinter.CTkButton(window, command=clear,font=font1, text_color='#9be0d0', text='C', fg_color='#000',hover_color='#2a1142', bg_color='#000',border_color='#fff',border_width=2,cursor='hand2', width=60)
b12.place(x=150, y=215)
b13 = customtkinter.CTkButton(window,font=font1, command=calculate, text_color='#9be0d0', text='=', fg_color='#071c14',hover_color='#2a1142', bg_color='#000',border_color='#fff',border_width=2,cursor='hand2', width=120)
b13.place(x=10, y=255)
b14 = customtkinter.CTkButton(window,font=font1, command=lambda: button_click('+'), text_color='#fff', text='+', fg_color='#071c14',hover_color='#2a1142', bg_color='#000',border_color='#fff',border_width=2,cursor='hand2', width=60)
b14.place(x=220, y=80)
b15 = customtkinter.CTkButton(window,font=font1, command=lambda: button_click('-'), text_color='#fff', text='-', fg_color='#071c14',hover_color='#2a1142', bg_color='#000',border_color='#fff',border_width=2,cursor='hand2', width=60)
b15.place(x=220, y=125)
b16 = customtkinter.CTkButton(window,font=font1, command=lambda: button_click('x'), text_color='#fff', text='x', fg_color='#071c14',hover_color='#2a1142', bg_color='#000',border_color='#fff',border_width=2,cursor='hand2', width=60)
b16.place(x=220, y=170)
b17 = customtkinter.CTkButton(window,font=font1, command=lambda: button_click('/'), text_color='#fff', text='/', fg_color='#071c14',hover_color='#2a1142', bg_color='#000',border_color='#fff',border_width=2,cursor='hand2', width=60)
b17.place(x=220, y=215)


window.mainloop()