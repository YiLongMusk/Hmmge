import util

startyear = int(input())
period = int(input())
period += 1
ticks = int(input())

util.write(filename = r"temp.txt", start = startyear, period = period)
util.plot(filename = r"temp.txt", startyear = startyear, endyear = startyear + (period - 1), ticks = ticks)
