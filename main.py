"""
This is ATM made on Tkinter
made by Zubareva Tatyna, 20704
PIN = 0000
"""


from tkinter import *
import time
import itertools

tk = Tk()

# tk.update()
tk.title("Space bank")
tk.geometry("530x682")

my_canvas = Canvas(tk, width = 530, height = 682, bd = 0, highlightthickness = 0)
my_canvas.pack(fill = "both", expand = True)

# tk.resizable(False, False)
my_canvas.config(bg = "#1B1B1D")

photo = PhotoImage(file = "main background.png")
background_label = my_canvas.create_image(0, 0, image = photo, anchor = 'nw')
# background_label = my_canvas.create_image(266, 342, image = photo)
# background_label = Label(tk, image=photo)
# background_label.place(x=0, y=0, relwidth=1, relheight=1)


cards = []


cards.append(PhotoImage(file = "card1.png"))
cards.append(PhotoImage(file = "card2.png"))
cards.append(PhotoImage(file = "card3.png"))
cards.append(PhotoImage(file = "card4.png"))
cards.append(PhotoImage(file = "card5.png"))
cards.append(PhotoImage(file = "card6.png"))
cards.append(PhotoImage(file = "card7.png"))
cards.append(PhotoImage(file = "card8.png"))
cards.append(PhotoImage(file = "card9.png"))
cards.append(PhotoImage(file = "card10.png"))
button_image1 = PhotoImage(file = "putcard.png")
cards.reverse()

money = []
money.append(PhotoImage(file = "money1.png"))
money.append(PhotoImage(file = "money2.png"))
money.append(PhotoImage(file = "money3.png"))
money.append(PhotoImage(file = "money4.png"))
money.append(PhotoImage(file = "money5.png"))
money.append(PhotoImage(file = "money6.png"))
money.append(PhotoImage(file = "money7.png"))
money.append(PhotoImage(file = "money8.png"))
money.append(PhotoImage(file = "money9.png"))
money.append(PhotoImage(file = "money10.png"))
money.append(PhotoImage(file = "money1.png"))
money.reverse()

screens = []
screens.append(PhotoImage(file = "screen1.png"))
screens.append(PhotoImage(file = "screen2.png"))
screens.append(PhotoImage(file = "screen3.png"))
screens.append(PhotoImage(file = "screen4.png"))
screens.append(PhotoImage(file = "screen5.png"))
screens.append(PhotoImage(file = "screen6.png"))





money1 = my_canvas.create_image(430, 590, image = money[10])

card1 = my_canvas.create_image(430, 400, image = cards[0])

start_image = PhotoImage(file = "start_screen.png")
enter_pin_im = PhotoImage(file = "pin_screen.png")
money_enter = PhotoImage(file = "money_screen.png")
take_money_screen = PhotoImage(file = "take_money.png")
middle_menu_screen = PhotoImage(file = "middle_screen.png")
pay_nali = PhotoImage(file = "pay_nal.png")
balance = PhotoImage(file = "balance.png")
take_card = PhotoImage(file = "take_card.png")
nal_screen = PhotoImage(file = "nal.png")
button_image2 = PhotoImage(file = "receipt.png")
button_image3 = PhotoImage(file = "sq.png")
button_image4 = PhotoImage(file = "0.png")
button_image5 = PhotoImage(file = "000.png")
button_image6 = PhotoImage(file = "1.png")
button_image7 = PhotoImage(file = "2.png")
button_image8 = PhotoImage(file = "3.png")
button_image9 = PhotoImage(file = "4.png")
button_image10 = PhotoImage(file = "5.png")
button_image11 = PhotoImage(file = "6.png")
button_image12 = PhotoImage(file = "7.png")
button_image13 = PhotoImage(file = "8.png")
button_image14 = PhotoImage(file = "9.png")
button_image15 = PhotoImage(file = "point.png")
button_image16 = PhotoImage(file = "cancel.png")
button_image17 = PhotoImage(file = "clear.png")
button_image18 = PhotoImage(file = "enter.png")



def put_card():
    '''
    animation for putting card in
    :return:
    '''

    global temp, after_id
    after_id = tk.after(500, put_card)
    if temp + 8 > -1:
        my_canvas.itemconfigure(card1, image=cards[temp + 8])
        temp -= 1
    else:
        stop_tick()
        my_canvas.itemconfigure(card1, image=cards[0])
        temp = 0
        checking_pin()

def stop_tick():
    tk.after_cancel(after_id)

PIN = "0000"

def checking_pin():
    global value
    '''
    entering widget
    :return:
    '''
    my_canvas.create_image(260, 150, image=enter_pin_im)

    # pin_entry.lower()
    pin_entry.tkraise()
    pin_window = my_canvas.create_window(190, 200, anchor = 'nw', window = pin_entry)
    value = pin_entry.get()
    if value == PIN:
        pin_entry.destroy()
        menu()

def clear_num():
    global value
    value = pin_entry.get()[:-1]
    pin_entry.delete(0, END)
    pin_entry.insert(0, value)

def delete_num():
    global value
    value = ''
    pin_entry.delete(0, END)
    pin_entry.insert(0, value)

def clear_num_money():
    global sum
    sum = money_entry.get()[:-1]
    money_entry.delete(0, END)
    money_entry.insert(0, sum)

def delete_num_money():
    global sum
    sum = ''
    money_entry.delete(0, END)
    money_entry.insert(0, sum)

def press_num(num):
    '''
    returning the pressed number
    :param num:
    :return:
    '''
    pincode = pin_entry.get() + num
    pin_entry.delete(0, END)
    pin_entry.insert(0, pincode)
    # my_canvas.update()

def new_buttons():
    '''
    changing button functions
    :return:
    '''
    n1.configure(command = lambda: press_num_money("1"))
    n2.configure(command= lambda:press_num_money("2"))
    n3.configure(command= lambda:press_num_money("3"))
    n4.configure(command= lambda:press_num_money("4"))
    n5.configure(command= lambda:press_num_money("5"))
    n6.configure(command= lambda:press_num_money("6"))
    n7.configure(command= lambda:press_num_money("7"))
    n8.configure(command= lambda:press_num_money("8"))
    n9.configure(command= lambda:press_num_money("9"))
    n11.configure(command= lambda:press_num_money("0"))
    e3.configure(command=animation_money)
    e2.configure(command=clear_num_money)
    e1.configure(command=delete_num_money)

def new_buttons2():
    '''
    changing button functions
    :return:
    '''
    n1.configure(command = lambda: press_num_new("1"))
    n2.configure(command= lambda:press_num_new("2"))
    n3.configure(command= lambda:press_num_new("3"))
    n4.configure(command= lambda:press_num_new("4"))
    n5.configure(command= lambda:press_num_new("5"))
    n6.configure(command= lambda:press_num_new("6"))
    n7.configure(command= lambda:press_num_new("7"))
    n8.configure(command= lambda:press_num_new("8"))
    n9.configure(command= lambda:press_num_new("9"))
    n11.configure(command= lambda:press_num_new("0"))
    e3.configure(command=put_nal)
    e2.configure(command=clear_num_money)
    e1.configure(command=delete_num_money)


def animation_money():

    '''
    animation for getting money
    :return:
    '''

    global temp, after_id
    after_id = tk.after(500, animation_money)
    if temp + 6 > -1:
        my_canvas.itemconfigure(money1, image=money[temp + 6])
        temp -= 1
    else:
        stop_tick()
        my_canvas.itemconfigure(money1, image=money[0])
        temp = 0

    my_canvas.create_image(260, 150, image=take_money_screen)
    money_entry.destroy()
    # time.sleep(0.5)
    middle_menu()

money2 = list(reversed(money))
def put_nal():
    '''
    putting nal
    :return:
    '''
    new_entry.destroy()
    my_canvas.create_image(260, 150, image=nal_screen)
    global temp, after_id
    after_id = tk.after(500, put_nal)
    if temp + 6 > -1:
        my_canvas.itemconfigure(money1, image=money2[temp + 6])
        temp -= 1
    else:
        stop_tick()
        my_canvas.itemconfigure(money1, image=money2[0])
        temp = 0
    s3.configure(command=stop_work)
    s6.configure(command=menu)


def middle_menu():
    '''
    screen for middle menu
    :return:
    '''
    # time.sleep(0.5)

    my_canvas.create_image(260, 150, image=middle_menu_screen)
    s2.configure(command = stop_work)
    s5.configure(command = menu)

def menu():
    '''
    menu
    :return:
    '''
    start_im = my_canvas.create_image(260, 150, image=start_image)
    s2.configure(command=get_balance)
    s5.configure(command=pay_nal)
    # s4.configure(command = put_money)
    # s5.configure(command=real_money)
    # s6.configure(command = transaction)

cards2 = list(reversed(cards))
after_id3 = ''

def get_balance():
    '''

    :return:
    '''
    my_canvas.create_image(260, 150, image=balance)
    s3.configure(command=stop_work)
    s6.configure(command=menu)


def stop_work():
    '''
    stopping work
    :return:
    '''
    my_canvas.create_image(260, 150, image=take_card)
    global temp, after_id3
    after_id3 = tk.after(500, stop_work)
    if temp + 6 > -1:
        my_canvas.itemconfigure(card1, image=cards2[temp + 6])
        temp -= 1
    else:
        stop_tick()
        my_canvas.itemconfigure(card1, image=cards2[0])
        temp = 0
        my_canvas.create_image(430, 400, image=cards[0])

def press_num_new(num):
    global sum
    '''
    return the value of money
    :return:
    '''
    sum = new_entry.get() + num
    new_entry.delete(0, END)
    new_entry.insert(0, sum)

def press_num_money(num):
    global sum
    '''
    return the value of money
    :return:
    '''
    sum = money_entry.get() + num
    money_entry.delete(0, END)
    money_entry.insert(0, sum)

def pay_nal():
    '''
    function for paying
    :return:
    '''
    my_canvas.create_image(260, 150, image=pay_nali)
    new_buttons2()
    new_entry.tkraise()
    money_window = my_canvas.create_window(190, 200, anchor='nw', window=new_entry)

def get_money():
    '''
    function for getting money
    :return:
    '''

    new_buttons()
    my_canvas.create_image(260, 150, image=money_enter)
    money_entry.tkraise()
    money_window = my_canvas.create_window(190, 200, anchor='nw', window=money_entry)



b1 = Button(tk, image = button_image1, highlightthickness = 0, bd = 0, command = put_card)
b1.place(x=356, y=292)
b2 = Button(tk, image = button_image2, highlightthickness = 0, bd = 0)
b2.place(x=32, y=292)

s1 = Button(tk, image = button_image3, highlightthickness = 0, bd = 0, command = get_money)
s1.place(x=36, y=58)
s2 = Button(tk, image = button_image3, highlightthickness = 0, bd = 0)
s2.place(x=36, y=128)
s3 = Button(tk, image = button_image3, highlightthickness = 0, bd = 0, command = stop_work)
s3.place(x=36, y=198)
s4 = Button(tk, image = button_image3, highlightthickness = 0, bd = 0, command = put_nal)
s4.place(x=462, y=58)
s5 = Button(tk, image = button_image3, highlightthickness = 0, bd = 0, command = pay_nal)
s5.place(x=462, y=128)
s6 = Button(tk, image = button_image3, highlightthickness = 0, bd = 0)
s6.place(x=462, y=198)

n1 = Button(tk, image = button_image6, highlightthickness = 0, bd = 0, command = lambda: press_num('1'))
n1.place(x=50, y=508)
n2 = Button(tk, image = button_image7, highlightthickness = 0, bd = 0, command = lambda: press_num('2'))
n2.place(x=106, y=508)
n3 = Button(tk, image = button_image8, highlightthickness = 0, bd = 0, command = lambda: press_num('3'))
n3.place(x=162, y=508)
n4 = Button(tk, image = button_image9, highlightthickness = 0, bd = 0, command = lambda: press_num('4'))
n4.place(x=50, y=544)
n5 = Button(tk, image = button_image10, highlightthickness = 0, bd = 0, command = lambda: press_num('5'))
n5.place(x=106, y=544)
n6 = Button(tk, image = button_image11, highlightthickness = 0, bd = 0, command = lambda: press_num('6'))
n6.place(x=162, y=544)
n7 = Button(tk, image = button_image12, highlightthickness = 0, bd = 0, command = lambda: press_num('7'))
n7.place(x=50, y=580)
n8 = Button(tk, image = button_image13, highlightthickness = 0, bd = 0, command = lambda: press_num('8'))
n8.place(x=106, y=580)
n9 = Button(tk, image = button_image14, highlightthickness = 0, bd = 0, command = lambda: press_num('9'))
n9.place(x=162, y=580)
n10 = Button(tk, image = button_image15, highlightthickness = 0, bd = 0).place(x=50, y=616)
n11 = Button(tk, image = button_image4, highlightthickness = 0, bd = 0, command = lambda: press_num('0'))
n11.place(x=106, y=616)
n12 = Button(tk, image = button_image5, highlightthickness = 0, bd = 0).place(x=162, y=616)




e1 = Button(tk, image = button_image16, highlightthickness = 0, bd = 0, command = delete_num)
e1.place(x=230, y=508)
e2 = Button(tk, image = button_image17, highlightthickness = 0, bd = 0, command = clear_num)
e2.place(x=230, y=544)
e3 = Button(tk, image = button_image18, highlightthickness = 0, bd = 0, command = checking_pin)
e3.place(x=230, y=580)

pin_entry = Entry(tk, width=10, font=('Nunito Sans', 20), justify = CENTER, highlightthickness = 0, fg = '#DEBEE4', bg ='#1A181F', bd = 0, show = '*')
money_entry = Entry(tk, width=10, font=('Nunito Sans', 20), justify = CENTER, highlightthickness = 0, fg = '#DEBEE4', bg ='#1A181F', bd = 0)
new_entry = Entry(tk, width=10, font=('Nunito Sans', 20), justify = CENTER, highlightthickness = 0, fg = '#DEBEE4', bg ='#1A181F', bd = 0)

temp = 0
after_id = ''
after_id2 = ''














tk.mainloop()