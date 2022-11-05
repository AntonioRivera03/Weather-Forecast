from requests_html import HTMLSession
from lxml import html


def currentWeather(location):
    s = HTMLSession()   
    x = s.get(f'https://google.com/search?q=weather+{location}')
    temp = (x.html.find('span#wob_tm', first=True).text)
    condition = (x.html.find('span#wob_dc',first=True).text)
    return (f'{location} : {temp}° | {condition}\n{forecast(x)}')

def forecast(x):
    tree = html.fromstring(x.content)
    temp2 = tree.xpath('//*[@id="wob_dp"]/div[2]/div[3]/div[1]/span[1]/text()')[0]
    temp3 = tree.xpath('//*[@id="wob_dp"]/div[3]/div[3]/div[1]/span[1]/text()')[0]
    temp4 = tree.xpath('//*[@id="wob_dp"]/div[4]/div[3]/div[1]/span[1]/text()')[0]
    temp5 = tree.xpath('//*[@id="wob_dp"]/div[5]/div[3]/div[1]/span[1]/text()')[0]
    temp6 = tree.xpath('//*[@id="wob_dp"]/div[6]/div[3]/div[1]/span[1]/text()')[0]
    temp7 = tree.xpath('//*[@id="wob_dp"]/div[7]/div[3]/div[1]/span[1]/text()')[0]
    temp8 = tree.xpath('//*[@id="wob_dp"]/div[8]/div[3]/div[1]/span[1]/text()')[0]
    day1 = tree.xpath('//*[@id="wob_dp"]/div[1]/div[3]/div[1]/span[1]/text()')[0]
    day2 = tree.xpath('//*[@id="wob_dp"]/div[2]/div[1]/text()')[0]
    day3 = tree.xpath('//*[@id="wob_dp"]/div[3]/div[1]/text()')[0]
    day4 = tree.xpath('//*[@id="wob_dp"]/div[4]/div[1]/text()')[0]
    day5 = tree.xpath('//*[@id="wob_dp"]/div[5]/div[1]/text()')[0]
    day6 = tree.xpath('//*[@id="wob_dp"]/div[6]/div[1]/text()')[0]
    day7 = tree.xpath('//*[@id="wob_dp"]/div[7]/div[1]/text()')[0]
    day8 = tree.xpath('//*[@id="wob_dp"]/div[8]/div[1]/text()')[0]

    return (f'{day2}: {temp2} | {day3}: {temp3} | {day4}: {temp4}\n'
            f'{day5}: {temp5} | {day6}: {temp6} | {day7}: {temp7}')




local = input('Enter location to get weather at: ')
print(currentWeather(local))