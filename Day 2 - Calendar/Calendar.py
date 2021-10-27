from tkinter import *
import calendar

def showCalendar():

    box = Tk()
    box.title("Calendar")
    box.geometry("550x600")
    find_year = int(year_field.get())
    first_label = Label(box, text='CALENDAR', bg='grey', font=("Arial", 30, 'bold'))
    first_label.grid(row=1, column=1)
    box.config(background="#FFD1C7")
    cal_data = calendar.calendar(find_year)
    cal_year = Label(box, text=cal_data, font="consolas 10 bold", justify=LEFT)
    cal_year.grid(row=2, column=1, padx=20)
    box.mainloop()


if __name__ == "__main__":

    gui = Tk()
    gui.config(background="#C8FFC7")
    gui.title("CALENDAR")
    gui.geometry("250x250")
    cal = Label(gui, text="CALENDAR", bg="lavender", font=("Helvetica", 30, 'bold', 'underline'))
    year = Label(gui, text="Enter Year", bg="peach puff", padx=10, pady=10)
    year_field = Entry(gui)
    show = Button(gui, text="Show Calendar", fg="Black", bg="lavender", command=showCalendar)
    Exit = Button(gui, text="CLOSE", bg="peach puff", command=exit)
    cal.grid(row=1, column=1)
    year.grid(row=3, column=1)
    year_field.grid(row=4, column=1)
    show.grid(row=5, column=1)
    Exit.grid(row=7, column=1)
    gui.mainloop()
