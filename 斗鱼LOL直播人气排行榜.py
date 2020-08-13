import   requests
import  pprint
from bs4 import  BeautifulSoup
import  os
import  jsonpath
#01 确定爬去的地址
url = 'https://www.douyu.com/g_LOL'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'}
#02 发送请求
response = requests.get(url=url,headers=headers)

#03 解析网页代码
html = response.text
soup = BeautifulSoup(html, 'html.parser')
#strs = soup.prettify()
#print(strs)
hot_html = soup.find_all('span',{'class':'DyListCover-hot is-template'})
hots_list = []
for  hots  in  hot_html:
    hots_list.append(hots.text[:-1])
hots_list = list(map(float, hots_list))  #把热度字符改成数字类型
#print(hots_list)
name_html = soup.find_all('h2',{'class':'DyListCover-user is-template'})
names_list = []
for  names  in  name_html:
    names_list.append(names.text)
#print(names_list)
item_dict = {}
for  name,hot in zip(names_list,hots_list):
    #print(name,hot)
    item_dict[name] = hot
#print(item_dict)
# 打印数组元素
#print(item_dict.items())

#排序热度
change_score = sorted(item_dict.items(),key = lambda x:x[1],reverse = True)
#print(change_score)

#04、数据输出
if os.path.exists('英雄联盟直播人气排行02.txt'):
        os.remove('英雄联盟直播人气排行02.txt')
for count,hot_name in  enumerate(change_score):
    print('斗鱼英雄联盟直播排行：第{}名是:{}: 人气是：{}万 \n'.format(count+1,change_score[count][0],change_score[count][1]))
    #写入文件
    f = open('英雄联盟直播人气排行02.txt','a',encoding='UTF-8')
    f.write('斗鱼英雄联盟直播排行：第{}名是:{}: 人气是：{}万 \n'.format(count+1,change_score[count][0],change_score[count][1]))
    #关闭文件
    f.close()




