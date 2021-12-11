import vk_api
import time, datetime

vk = vk_api.VkApi()
vk.auth()
dt = datetime.datetime.today()
id_1 = '361649916' #Леня
id_2 = '499686451'
mess_2 = 'тест'
a = dt.hour
s = 'не забудь про фейт, каждый день в 16 по мск' #текст cообщения
#meth = 'messages.send'
values = {'out':1, 'count':100, 'time_offset':60}
def f_messages(id_id,s):
    vk.method('messages.send', {'user_id':id_id,'message':s})

def mes_datetime():
    dt = datetime.datetime.today()
    mess = (str(dt.year)+" год\n"+str(dt.month)+" месяц\n"+str(dt.day)+
            " день\n"+str(dt.hour)+" час\n"+str(dt.minute)+" минут\n"+
            str(dt.second)+' секунд\n'+str(dt.microsecond)+' микросекунд')
    return mess

done = True
while done:
    dt = datetime.datetime.today()
    s = mes_datetime()
    f_messages(id_1,str(s))
    time.sleep(3500)
    if dt.hour != b:
        f_messages(id_2,mess_2)
        f_messages(id_2,s)
        b = dt.hour
