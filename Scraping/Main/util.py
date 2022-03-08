from urllib.request import Request as Req, urlopen as Urlopen
from bs4 import BeautifulSoup as Soup
import matplotlib.pyplot as plt
import matplotlib.ticker as plticker
import matplotlib.pylab as pylab
import tkinter as tk

def scrape(year, month):
    year_real = str(year + 1909)
    month_real = str(month + 1)

    url = f"https://climate.weather.gc.ca/climate_data/daily_data_e.html?hlyRange=%7C&dlyRange=1889-10-01%7C2022-01-30&mlyRange=1889-01-01%7C2007-02-01&StationID=707&Prov=BC&urlExtension=_e.html&searchType=stnProv&optLimit=yearRange&StartYear=1920&EndYear=1921&selRowPerPage=25&Line=1&lstProvince=&timeframe=2&Day=7&Year={year_real}&Month={month_real}#"
    client = Req(url, headers={"User-Agent": "Mozilla/5.0"})
    html = Urlopen(client).read()
    Urlopen(client).close()
    soup = Soup(html, "html.parser")
    data = soup.findAll("td")

    if int(month_real) == 2:
        if int(year_real) % 4 == 0:
            if int(year_real) % 100 == 0:
                if int(year_real) % 400 == 0:
                    num = 332
                else:
                    num = 321
            else:
                num = 332
        else:
                num = 321
    elif int(month_real) < 8:
        if int(month_real) % 2 == 0:
            num = 343
        else:
            num = 354
    else:
        if int(month_real) % 2 == 0:
            num = 354
        else:
            num = 343

    return data[num].text, year_real, month_real

def write(filename = r"data.txt", start = 1909, period = 100):
    for year in range(period):
        for month in range(12):
            temp, year_real, month_real = scrape(year + (start - 1909), month)
            temp = temp.removesuffix("LegendCarer^")

            file = open(filename, "a")
            file.writelines(f"{year_real} {month_real} {temp}\n")

def read(filename = r"data.txt"):
    file = open(filename, "r")
    raw_data = file.readlines()
    data = []
    for datas in raw_data:
        data.append(datas.rstrip("\n"))

    return data

def arrange(filename = r"data.txt"):
    raw_data = read(filename)

    yearx = []
    tempy = []

    temps = []
    avg = 0
    i = 1
    for datas in raw_data:
        if i == 13 or i == 1:
            data = datas.split()
            year = data[0]

            yearx.append(year)
            i = 1

        data = datas.split()
        temps.append(data[2])

        if i == 12:
            for temp in temps:
                avg += float(temp)

            avg = avg / 12
            tempy.append(round(avg, 1))

            temps = []

        i += 1

    return yearx, tempy

def plot(filename = r"data.txt" , startyear = 1909, endyear = 1999, ticks = 5):
    yearx, tempy = arrange(filename = filename)

    fig, ax = plt.subplots()
    ax.plot(yearx, tempy)
    loc = plticker.MultipleLocator(base = ticks)
    ax.xaxis.set_major_locator(loc)
    plt.grid()

    plt.title(f"Average Temperature {startyear} - {endyear}", fontsize = 16)
    plt.xlabel("Year", fontsize = 12)
    plt.ylabel("Temperature (Celsius)", fontsize = 12)
    fig = pylab.gcf()
    fig.canvas.set_window_title("Graph")

    plt.show()

def ui():
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

        return year1, year2

    tk.Button(root, text = "Submit", width = 20, command = lambda:[get_years(), root.destroy()]).pack(pady = 20)

    root.mainloop()
