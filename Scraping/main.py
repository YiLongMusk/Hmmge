import util
import tkinter as tk

window_width = 500
window_height = 300

root = tk.Tk()
root.title("Average Temperature Over Years")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

main_title = tk.Label(root, text = "What Years do You Want to Graph?", foreground = "white", background = "black")
main_title.pack()

year_entry1 = tk.Entry(root, width = 30)
year_entry1.place(x = center_x, y = center_y)
year_entry1.focus_set()
year_entry1.pack()

year_entry2 = tk.Entry(root, width = 30)
year_entry2.place(x = center_x, y = center_y)
year_entry2.pack()

def get_years():
    global entry, year1, year2
    string = year_entry1.get()
    main_title.configure(text = string)
    year1 = int(year_entry1.get())
    year2 = int(year_entry2.get())

tk.Button(root, text = "Submit", width = 20, command = lambda:[get_years(), root.destroy()]).pack(pady = 20)

root.mainloop()

startyear = year1
period = year2 - year1

ticks = period / 10

if ticks <= 1:
    ticks = 1
elif ticks <= 2:
    ticks = 2
elif ticks <= 5:
    ticks = 5
elif ticks <= 10:
    ticks = 10

period += 1

util.write(filename = r"temp.txt", start = startyear, period = period)
util.plot(filename = r"temp.txt", startyear = startyear, endyear = startyear + (period - 1), ticks = ticks)

file = open(r"temp.txt","r+")
file.truncate(0)
file.close()
