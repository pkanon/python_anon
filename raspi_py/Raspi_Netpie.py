import microgear.client as client
import time

gearkey = 'O74S4Aenf9KlG8z'# key 
gearsecret = 'vON0xUmvkmwnYT6hoxZatBmHv' # secret
appid = 'PEATraining' # ชื่อแอพของเรา 
client.create(gearkey,gearsecret,appid,{'debugmode': True}) # สร้างข้อมูลสำหรับใช้เชื่อมต่อ


def callback_connect() :
    print ("Now I am connected with netpie")

def callback_message(topic, message) :
    print (topic, ": ", message)
 
def callback_error(msg) :
    print(msg)

client.on_connect = callback_connect # แสดงข้อความเมื่อเชื่อมต่อกับ netpie สำเร็จ
client.setalias("Raspi") # ตั้งชื่้อ
client.on_message= callback_message # ให้ทำการแสดงข้อความที่ส่งมาให้
client.on_error = callback_error # หากมีข้อผิดพลาดให้แสดง
client.subscribe("/test") # ชื่อช่องทางส่งข้อมูล ต้องมี / นำหน้า และต้องใช้ช่องทางเดียวกันจึงจะรับส่งข้อมูลระหว่างกันได้
client.connect() # เชื่อมต่อ ถ้าใช้ True เป็นการค้างการเชื่อมต่อ
i=0
while True:
    client.publish("/temp",i) # ส่งข้อมูลไปให้ temp
    time.sleep(5) # หน่วงเวลาการส่งข้อมูล 3 วินาที
    i+=1
    print(i)

