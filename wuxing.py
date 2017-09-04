import datetime
import math
import ganzhi

tiangans = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
dizhis = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
wuxingDicForTiangan = {
    "甲":"阳木",
    "乙":"阴木",
    "丙":"阳火",
    "丁":"阴火",
    "戊":"阳土",
    "己":"阴土",
    "庚":"阳金",
    "辛":"阴金",
    "壬":"阳水",
    "癸":"阴水"
}
wuxingDicForDizhi = {
    "子":"阳水",
    "丑":"阴土",
    "寅":"阳木",
    "卯":"阴木",
    "辰":"阳土",
    "巳":"阴火",
    "午":"阳火",
    "未":"阴土",
    "申":"阳金",
    "酉":"阴金",
    "戌":"阳土",
    "亥":"阴水"
}

def calculateTime(tianganOfDay, time):  # tiangan%10 : 10
    tianganIndex = (2 * tianganOfDay - 1) % 10
    if time == 23 or time == 0 or time == 24:
        dizhi = dizhis[0]
    else:
        dizhiIndex = time / 2
        if dizhiIndex >= 0.5:
            dizhiIndex = math.ceil(dizhiIndex)
        else:
            dizhiIndex = round(dizhiIndex)
        dizhi = dizhis[dizhiIndex]
    return tiangans[(tianganIndex - 1 + dizhiIndex) % 10] + dizhi


def getShenChenBaZi(year, month, day, time):
    data = ganzhi.day(year, month, day)
    tianganOfDay = data[2]
    tianganOfDaySymbol = tiangans.index(tianganOfDay) + 1
    ganzhiOfTime = calculateTime(tianganOfDaySymbol, time)
    return data[0] + '-' + ganzhiOfTime


birthYear = input("please input your birth year: ")
birthMonth = input("please input your birth month: ")
birthDay = input("please input your birth day: ")
birthTime = input("please input your birth time: ")
# shenchenbazi = getShenChenBaZi(1991, 12, 15, 10)
# shenchenbazi = getShenChenBaZi(1994,5,8,9)
# shenchenbazi = getShenChenBaZi(1987,12,24,7)
shenchenbazi = getShenChenBaZi(int(birthYear), int(birthMonth), int(birthDay), int(birthTime))
print("你的生辰八字是: %s" % (shenchenbazi))