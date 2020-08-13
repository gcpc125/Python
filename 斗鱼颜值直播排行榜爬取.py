# Python
import  requests
import  pprint
import  jsonpath
import  os
#01、确定爬取的URL地址
url = ('https://www.douyu.com/gapi/rknc/directory/yzRec/1')
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'}
#02、发送请求
response = requests.get(url= url,headers = headers)
json_data = response.json()
#pprint.pprint(json_data)

#03、解析网页源代码
names = jsonpath.jsonpath(json_data,'$..nn')   #  提取主播名字
hots  = jsonpath.jsonpath(json_data,'$..ol')   # 提取主播热度

item_dict = {}
for  name,hot in zip(names,hots):
    #print(name,hot)
    item_dict[name] = hot
#print(item_dict)
# 打印数组元素
#print(item_dict.items())

#排序热度
change_score = sorted(item_dict.items(),key = lambda x:x[1],reverse = True)
#print(change_score)

#04、数据输出
if os.path.exists('斗鱼颜值直播人气排行01.txt'):
        os.remove('斗鱼颜值直播人气排行01.txt')
for count,hot_name in  enumerate(change_score):
    print('斗鱼颜值直播排行：第{}名是:{}: 人气是：{} \n'.format(count+1,change_score[count][0],change_score[count][1]))
    #写入文件
    f = open('斗鱼颜值直播人气排行01.txt','a',encoding='UTF-8')
    f.write('斗鱼颜值直播排行：第{}名是:{}: 人气是：{} \n'.format(count+1,change_score[count][0],change_score[count][1]))
    #关闭文件
    f.close()




