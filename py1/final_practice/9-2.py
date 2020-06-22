from tkinter import *

window = Tk()
window.title("투자금 계산기 생성하기")

opt1 = StringVar()
opt2 = StringVar()
opt3 = StringVar()

result = DoubleVar()

def toja():
    t1 = float(opt1.get())
    t2 = float(opt2.get())
    t3 = float(opt3.get())

    r = t1 * (1 + t3) ** (t2 * 12)
    result.set(r)

Label(window, text="투자금").grid(row=0, column=0, sticky=W)
Entry(window, textvariable=opt1).grid(row=0, column=1, padx=5,pady=2, columnspan=2)

Label(window, text="기간").grid(row=1, column=0, sticky=W)
Entry(window, textvariable=opt2).grid(row=1,column=1, padx=5, pady=2, columnspan=2)

Label(window, text="월이율").grid(row=2, column=0, sticky=W)
Entry(window, textvariable=opt3).grid(row=2,column=1, padx=5, pady=2, columnspan=2)

Label(window, text="미래 가치").grid(row=3, column=0, sticky=W)
Label(window, textvariable=result, state="disabled").grid(row=3,column=1, padx=5, pady=2, columnspan=2)

Button(window, text="계산하기", command=toja).grid(row=4, column=2, sticky=E)

window.mainloop()