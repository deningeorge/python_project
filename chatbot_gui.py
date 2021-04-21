from tkinter import *
root=Tk()
root.title('chat box')
root.geometry('400x500')


main_menu=Menu(root)

#submenu
file_menu=Menu(root)
file_menu.add_command(label='New..')
file_menu.add_command(label='save as..')
file_menu.add_command(label='Exit..')


main_menu.add_cascade(label='File',menu_=file_menu)
main_menu.add_command(label='Edit')
main_menu.add_command(label='Quit')
root.config(menu=main_menu)

chatWindow=Text(root,bd=1,bg='skyblue', width=80,height=15)
chatWindow.place(x=6,y=6,height=385,width=370)

messageWindow=Text(root,bg='skyblue', width=27,height=4)
messageWindow.place(x=120,y=400,height=88,width=260)

Button=Button(root,text='send',bg='blue',activebackground='light blue',width=11,height=4, font=('Arial',25))
Button.place(x=6,y=400,height=85,width=110)
scrollbar=Scrollbar(root,command=chatWindow.yview())
scrollbar.place(x=375,y=5,height=385)


root.mainloop()