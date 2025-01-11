import random
n=10
lst=[]

#Khởi tạo list với ngẫu nhiên 10 ptu trong [-100,100]
def listrandom():
   ptu=random.randint(-100,100)
   lst.append(ptu)
for i in range(n):
    listrandom()
print('List gốc: ',lst)

#Thêm ptu vào list
m=int(input('Số phần tử muốn thêm vào list: '))
for j in range(m):
    ptu=int(input(f'Phần tử thêm vào thứ {j+1}: '))
    lst.append(ptu)

#Kiểm tra k xuất hiện bao nhiêu lần trong list
k=int(input('k = '))
print(f'Số lần xuất hiện giá trị {k} = {lst.count(k)}')

#Tính tổng các số hoàn thiện trong list
def checksohoanthien():
    sohoanthien=0
    numhoanthien=[]
    for num in lst:
        if num<=0: continue
        uocso=[1]
        s=0
        for p in range (2, int(num**0.5)+1):
            if num%p==0:
                uocso.append(p)
                if p!=num//p: uocso.append(num//p)
        s=sum(uocso)
        if s==num:
            sohoanthien+=1
            numhoanthien.append(num)
    return sohoanthien, numhoanthien
sohoanthien,numhoanthien=checksohoanthien()
print(f'Số số hoàn thiện trong list = {sohoanthien}')
if numhoanthien!=[]: print(f'--> Đó là số: {numhoanthien}')

#Sắp xếp tăng, giảm dần
lst_copy=lst.copy()
for increase1 in range (len(lst_copy)):
    for increase2 in range (increase1+1,len(lst_copy)):
        if lst_copy[increase2]<lst_copy[increase1]:
            temp=lst_copy[increase1]
            lst_copy[increase1]=lst_copy[increase2]
            lst_copy[increase2]=temp
print(lst_copy)
for decrease1 in range (len(lst_copy)):
    for decrease2 in range (decrease1+1,len(lst_copy)):
        if lst_copy[decrease2]>lst_copy[decrease1]:
            temp=lst_copy[decrease1]
            lst_copy[decrease1]=lst_copy[decrease2]
            lst_copy[decrease2]=temp
print(lst_copy)

#Xóa
#Xóa phần tử ở chỉ số
x=int(input('Xóa phần tử ở chỉ số: '))
xoa_1ptu=lst.copy()
xoa_1ptu.pop(x)
print(xoa_1ptu)
#Xóa số âm
xoa_soam=lst.copy()
listkhongam=[]
for num in xoa_soam:
    if num>=0: listkhongam.append(num)
print('Xóa giá trị âm: ',end='')
print(listkhongam)
#Xóa toàn bộ ds
del lst 