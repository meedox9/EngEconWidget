from tkinter import *
from time import sleep

# Creating Window and add atributes
root = Tk()
root.geometry('550x290')
root.title('Engineering Economics Calculator')
root.configure(bg='grey')
root.resizable(0, 0)

# Creating Direction Label
WinTitle = Label(root, text="Enter Variables:", font='Helvetica 11 bold', bg='grey', fg='white').grid(row=1, column=2)

# interest entry box
interest = Label(root, text="i:", font='Helvetica 11 bold', bg='grey', fg='white').grid(row=2, column=1, padx=10)
e_interest = Entry(root, width=10, borderwidth=3)
e_interest.grid(row=2, column=2, pady=20)
interestsign = Label(root, text="%      ", font='Helvetica 11 bold', bg='grey', fg='white').grid(row=2, column=3)

# period entry box
period = Label(root, text="N: ", font='Helvetica 11 bold', bg='grey', fg='white').grid(row=2, column=4)
e_period = Entry(root, width=10, borderwidth=3)
e_period.grid(row=2, column=5, pady=20)
l_period = Label(root, text="Years", font='Helvetica 11 bold', bg='grey', fg='white').grid(row=2, column=6)

# result box
e_result = Entry(root, width=10, borderwidth=3)
e_result.grid(row=5, column=8)
l_result = Label(root, text="Result:", bg='grey', fg='white', font='Helvetica 11 bold')
l_result.grid(row=5, column=7)

l_error = Label(root, text=" ", font='Helvetica 9 bold', bg='grey', fg='white')
l_error.grid(row=11, column=8)

#error handling for result box 1 
def reset_label(new_label):
    l_result.destroy()
    ne = Label(root, text=new_label, bg='grey', fg='white', font='Helvetica 11 bold')
    ne.grid(row=5, column=7)


#error handling for result box 2
def reset_label2(new_label2):
    l_error.destroy()
    ne = Label(root, text=new_label2, bg='grey', fg='white', font='Helvetica 9 bold')
    ne.grid(row=11, column=7)



def fp_calc():
    e_result.delete(0, END)
    for cast in (int, float):
        try:
            i = cast(e_interest.get())
            n = cast(e_period.get())
            num1 = (1 + (i / 100)) ** n
            num = round(num1, 5)
            label = "F/P ="
            reset_label(label)
            e_result.insert(0, num)
            break
        except ValueError:
            pass
        except OverflowError:
            pass


def pf_calc():
    e_result.delete(0, END)
    for cast in (int, float):
        try:
            i = cast(e_interest.get())
            n = cast(e_period.get())
            num1 = 1 / ((1 + (i / 100)) ** n)
            num = round(num1, 5)
            label = "P/F ="
            reset_label(label)
            e_result.insert(0, num)
            break
        except ValueError:
            pass
        except OverflowError:
            pass


def af_calc():
    e_result.delete(0, END)
    for cast in (int, float):
        try:
            i = cast(e_interest.get())
            n = cast(e_period.get())
            num1 = ((i / 100) / (((1 + (i / 100)) ** n) - 1))
            num = round(num1, 5)
            label = "A/F ="
            reset_label(label)
            e_result.insert(0, num)
            break
        except ValueError:
            pass
        except OverflowError:
            pass


def fa_calc():
    e_result.delete(0, END)
    for cast in (int, float):
        try:
            i = cast(e_interest.get())
            n = cast(e_period.get())
            num1 = ((((1 + (i / 100)) ** n) - 1) / (i / 100))
            num = round(num1, 5)
            label = "F/A ="
            reset_label(label)
            e_result.insert(0, num)
            break
        except ValueError:
            pass
        except OverflowError:
            pass


def ap_calc():
    e_result.delete(0, END)
    for cast in (int, float):
        try:
            i = cast(e_interest.get())
            n = cast(e_period.get())
            num1 = (((i / 100) * ((1 + (i / 100)) ** n)) / (((1 + (i / 100)) ** n) - 1))
            num = round(num1, 5)
            label = "A/P ="
            reset_label(label)
            e_result.insert(0, num)
            break
        except ValueError:
            pass
        except OverflowError:
            pass


def pa_calc():
    e_result.delete(0, END)
    for cast in (int, float):
        try:
            i = cast(e_interest.get())
            n = cast(e_period.get())
            num1 = ((((1 + (i / 100)) ** n) - 1) / ((i / 100) * ((1 + (i / 100)) ** n)))
            num = round(num1, 5)
            label = "P/A ="
            reset_label(label)
            e_result.insert(0, num)
            break
        except ValueError:
            pass
        except OverflowError:
            pass


def i_effective():
    for cast in (int, float):
        label1 = "                            "
        try:
            ie_result.delete(0, END)
            i = cast(e_interest_s.get())
            n = cast(e_period_m.get())
            num1 = (((1 + ((i / 100) / n)) ** n) - 1) * 100
            num = round(num1, 5)
            ie_result.insert(0, num)
            reset_label2(label1)
            break
        except ValueError:
            pass
        except OverflowError:
            label = "Number too big!"
            reset_label2(label)


################################### First Row Buttons #############################################


# creating Compound Amount Factor button
fp = Button(root, text='(F/P, i, N)', bg='slate grey', fg='white', command=fp_calc)
fp.grid(row=4, rowspan=1, column=2)

# creating Sinking Fund Factor button
af = Button(root, text='(A/F, i, N)', bg='slate grey', fg='white', command=af_calc)
af.grid(row=5, rowspan=1, column=2, pady=10)

# creating Capital Recovery Factor button
ap = Button(root, text='(A/P, i, N)', bg='slate grey', fg='white', command=ap_calc)
ap.grid(row=7, rowspan=1, column=2)

################################### Second Row Buttons #############################################

# creating Present Worth Factor button
fp = Button(root, text='(P/F, i, N)', bg='slate grey', fg='white', command=pf_calc)
fp.grid(row=4, rowspan=1, column=5)

# creating Uniform Series Compound Factor button
af = Button(root, text='(F/A, i, N)', bg='slate grey', fg='white', command=fa_calc)
af.grid(row=5, rowspan=1, column=5)

# creating Series Present Worth Factor button
ap = Button(root, text='(P/A, i, N)', bg='slate grey', fg='white', command=pa_calc)
ap.grid(row=7, rowspan=1, column=5)


################################### Second Calculator #############################################
# interest s entry box
interest_s = Label(root, text="i\u209B:", font='Helvetica 11 bold', bg='grey', fg='white').grid(row=9, column=1)
e_interest_s = Entry(root, width=10, borderwidth=3)
e_interest_s.grid(row=9, column=2, pady=20)

# interest result box
ie_result = Entry(root, width=10, borderwidth=3)
ie_result.grid(row=10, column=8)
l_ie_result = Label(root, text="i\u2091 =", bg='grey', fg='white', font='Helvetica 11 bold')
l_ie_result.grid(row=10, column=7)
l_ie_interest_sign = Label(root, text="%", font='Helvetica 11 bold', bg='grey', fg='white').grid(row=10, column=9)

# period entry box
period_m = Label(root, text="n:", font='Helvetica 11 bold', bg='grey', fg='white').grid(row=9, column=4)
e_period_m = Entry(root, width=10, borderwidth=3)
e_period_m.grid(row=9, column=5)

# interest e  button
interest_e = Button(root, text='i\u2091= (1+(r/n))\u207F', font='Helvetica 10 bold', bg='slate grey', fg='white', command=i_effective)
interest_e.grid(row=10, column=3)

#loop program
root.mainloop()
