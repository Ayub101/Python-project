import webScarpper as wscp
import threading as th
import send_email as se
import time as tm

price_list = []


def check(price,name,times,tm_fr,id):
    while True:
        wb = wscp.webScrapper()
        link = wb.get(name)
        lis = wb.scrapgog(link["Google"])
        for infor in lis :
            if name == infor.get('name'):
                real_pirce = infor.get('price')
                address = infor.get('address')
                real_pirce = real_pirce[1:len(real_pirce)-3]
                real_pirce = int(real_pirce.replace(",",''))
                print(real_pirce)
                price_list.append(real_pirce)
        price_list.sort()
        if price > price_list[0]:
            email = se.send_email()
            email.send_rem(name,address,id)
            break
        else:
            if tm_fr=="Hr":
                times = times*3600
                tm.sleep(times)
            elif tm_fr == "Min":
                times = times*60
                tm.sleep(times)

def threa(price,name,time,tm_fr,id):
    t1 = th.Thread(target=lambda :[check(price,name,time,tm_fr,id)])
    t1.start()


#check(20000,'Redmi Note 10 Shadow Black 6GB+128GB',3,'Hr','kayub4947@gmail.com')
#threa(20000,'Redmi Note 10 Shadow Black 6GB+128GB',3,'Hr','kayub4947@gmail.com')
