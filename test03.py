#รับค่า/ป้อนทางแป้นพิมพ์ ใช้ฟังชั่น input() โดยสิ่งที่ป้อนเป็น string

#ตัวแปร variable เป็น identifier
#identifier คือชื่อที่ dev. ตั้งชื่อมาเอง ต้องเป็นไปตามกฎการตั้งชื่อของภาษานั้นๆ

std_id = input('ป้อนรหัสนักศึกษา : ')
std_name = input('ป้อนชื่อนักศึกษา : ')
stdYearBorn = input('ป้อนปีเกิด : ')
print('---------------------------')
print(f"ยินดีต้อนรับ {std_id} ชื่อ {std_name}")
stdAge = 2023 - int(stdYearBorn)  #ต้องแปลง string เป็น number -> int( ), float( )
print(f"คุณเกิดปี {stdYearBorn} อายุ {stdAge}")



