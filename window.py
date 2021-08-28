from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("414x896")
window.configure(bg = "#ebf2fa")
canvas = Canvas(
    window,
    bg = "#ebf2fa",
    height = 896,
    width = 414,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

img0 = PhotoImage(file = f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 241, y = 789,
    width = 20,
    height = 40)

img1 = PhotoImage(file = f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 142, y = 793,
    width = 41,
    height = 33)

img2 = PhotoImage(file = f"img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b2.place(
    x = 64, y = 789,
    width = 20,
    height = 40)

img3 = PhotoImage(file = f"img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b3.place(
    x = 64, y = 709,
    width = 20,
    height = 40)

img4 = PhotoImage(file = f"img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b4.place(
    x = 153, y = 709,
    width = 20,
    height = 40)

img5 = PhotoImage(file = f"img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b5.place(
    x = 241, y = 709,
    width = 20,
    height = 40)

img6 = PhotoImage(file = f"img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b6.place(
    x = 64, y = 629,
    width = 20,
    height = 40)

img7 = PhotoImage(file = f"img7.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b7.place(
    x = 153, y = 629,
    width = 20,
    height = 40)

img8 = PhotoImage(file = f"img8.png")
b8 = Button(
    image = img8,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b8.place(
    x = 241, y = 629,
    width = 20,
    height = 40)

img9 = PhotoImage(file = f"img9.png")
b9 = Button(
    image = img9,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b9.place(
    x = 64, y = 549,
    width = 20,
    height = 40)

img10 = PhotoImage(file = f"img10.png")
b10 = Button(
    image = img10,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b10.place(
    x = 153, y = 549,
    width = 20,
    height = 40)

img11 = PhotoImage(file = f"img11.png")
b11 = Button(
    image = img11,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b11.place(
    x = 241, y = 549,
    width = 20,
    height = 40)

img12 = PhotoImage(file = f"img12.png")
b12 = Button(
    image = img12,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b12.place(
    x = 64, y = 469,
    width = 20,
    height = 40)

img13 = PhotoImage(file = f"img13.png")
b13 = Button(
    image = img13,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b13.place(
    x = 146, y = 473,
    width = 33,
    height = 33)

img14 = PhotoImage(file = f"img14.png")
b14 = Button(
    image = img14,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b14.place(
    x = 241, y = 469,
    width = 20,
    height = 40)

img15 = PhotoImage(file = f"img15.png")
b15 = Button(
    image = img15,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b15.place(
    x = 309, y = 777,
    width = 62,
    height = 63)

img16 = PhotoImage(file = f"img16.png")
b16 = Button(
    image = img16,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b16.place(
    x = 330, y = 709,
    width = 20,
    height = 40)

img17 = PhotoImage(file = f"img17.png")
b17 = Button(
    image = img17,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b17.place(
    x = 330, y = 629,
    width = 20,
    height = 40)

img18 = PhotoImage(file = f"img18.png")
b18 = Button(
    image = img18,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b18.place(
    x = 330, y = 549,
    width = 20,
    height = 40)

img19 = PhotoImage(file = f"img19.png")
b19 = Button(
    image = img19,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b19.place(
    x = 330, y = 469,
    width = 20,
    height = 40)

img20 = PhotoImage(file = f"img20.png")
b20 = Button(
    image = img20,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b20.place(
    x = 64, y = 395,
    width = 20,
    height = 33)

img21 = PhotoImage(file = f"img21.png")
b21 = Button(
    image = img21,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b21.place(
    x = 149, y = 395,
    width = 26,
    height = 33)

img22 = PhotoImage(file = f"img22.png")
b22 = Button(
    image = img22,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b22.place(
    x = 237, y = 398,
    width = 27,
    height = 27)

img23 = PhotoImage(file = f"img23.png")
b23 = Button(
    image = img23,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b23.place(
    x = 328, y = 399,
    width = 24,
    height = 24)

canvas.create_text(
    290.0, 160.5,
    text = "120",
    fill = "#002a3c",
    font = ("Abel-Regular", int(89.57142639160156)))

canvas.create_text(
    256.0, 234.0,
    text = "50 - 10 - 10 - 10 + 100",
    fill = "#427aa1",
    font = ("Abel-Regular", int(22.39285659790039)))

window.resizable(False, False)
window.mainloop()