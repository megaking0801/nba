import requests
from bs4 import BeautifulSoup
url = 'https://www.nba.com/games'

r = requests.get(url)
soup = BeautifulSoup(r.text,'lxml')

#aaa = soup.find(class_='DayButton_button__XeZqa DatePickerWeek_day__9fg0G DatePickerWeek_today__jfviJ DatePickerWeek_dayActive__CJfoK')
year = soup.find('p',class_='DatePickerInfo_dpi__uCTFB GameDatePicker_gdpInfo__1bvDG')
game = soup.find('p',class_='GameCardMatchup_gameSeriesText__zqvUF')
time = soup.find('p', class_='GameCardMatchupStatusText_gcsText__PcQUX')
#button = soup.find('button', class_='DayButton_button__XeZqa DatePickerWeek_day__9fg0G DatePickerWeek_today__jfviJ DatePickerWeek_dayActive__CJfoK')



yeartext = year.get_text(strip=True)#哪年哪月
print(yeartext)
gametext = game.get_text(strip=True)#誰打誰
print(gametext)
timetext = time.get_text(strip=True)#幾點
print(timetext)
#datetext = date.get_text(strip=True)#星期幾
#print(datetext)
#datenumbertext = datenumber.get_text(strip=True)#幾號
#print(datenumbertext)

teams = soup.find_all('span', class_="MatchupCardTeamName_teamName__9YaBA")
if teams:
    print("matchup:")
    a=[]
    for away in teams:
        awaytext = away.get_text(strip=True)
        a.append(awaytext)
        string = "".join(a)
    a_string = string[:4]
    b_string = string[4:10]
    print(a_string+"vs"+b_string)

scores = soup.find_all('p', class_="MatchupCardScore_p__dfNvc GameCardMatchup_matchupScoreCard__owb6w")
if scores:
    print("score:")
    b=[]
    for score in scores:
        scoretext = score.get_text(strip=True)
        b.append(awaytext)
        string = "".join(b) 
    print(b)



headers = {
        "Authorization": "Bearer " + "4W4sgsNVxhtn6MFLl3uw9IqcOVRPIaeD1WMUyIAhZZ7",
        "Content-Type": "application/x-www-form-urlencoded"
    }
params = {"message": "\n"+yeartext+","+"\n"+gametext+"\n"+timetext+"\n"+a_string+" vs "+b_string}
 
r = requests.post("https://notify-api.line.me/api/notify",headers=headers, params=params)












'''
elements = soup.find_all('span', class_='Jc(fe) Fw(600) D(f) Ai(c) C($c-trend-up)')#當日價格上漲的為trend-up#股價
elements2 = soup.find_all('div', class_="Lh(20px) Fw(600) Fz(16px) Ell")#股名

#elements3 = soup.find_all('span', class_='Mend(4px) Bds(s)', style="border-color: transparent transparent rgb(255, 51, 58); border-width: 0px 5px 7px;")#漲跌ㄨ

if elements:
        a = []
        b = []
        c = []
        for element in elements:
            text1 = element.get_text(strip=True)
            a.append(text1)
        for element in elements2:
            text = element.get_text(strip=True)
            b.append(text)

print("每日台灣市值前10ETF股名及股價")
print("")
for i in range(9):
    print("股名：",b[i]," ","股價：",a[i])
    i = i+1'''