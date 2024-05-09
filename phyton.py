# Bir classdan istifadə edərək 2 metod yazın.
# İlk metodda dəyər olaraq bir list içərisində rəqəmləri alın  və onu bir listə əlavə edin ( bu şəkildə olacaq: mylist=[1,2,3,4,5])
# Daha sonra bir metod daha yazın. Bu metodda isə bizim bir argumentimiz olacaq (Hədəf rəqəm). Burada ilk metodda aldığımız listin 
# dəyərləri içərisində hər hansı 2 rəqəmin cəmi verilmiş hədəf rəqəmə bərabərdirsə həmin rəqəmlərin indexlərini qaytarın. Əgər belə
# rəqəmlər yoxdursa -1 cavabı qaytarın. 

# Əlavə olaraq argumentləri hansı metodunuzda istifadə etmək istədiyiniz barəsində sərbəstsiniz və əlavə arqumentlərdən istifadə edəbilərsiniz.

class MyClass:
    def __init__(self):
        self.mylist = []

    def add_numbers(self, numbers):
        self.mylist.extend(numbers)

    def tap(self, number):
        cut_indexler = []
        for i in range(len(self.mylist)):
            for j in range(i + 1, len(self.mylist)):
                if self.mylist[i] + self.mylist[j] == number:
                    cut_indexler.append((i, j))
        if cut_indexler:
            return cut_indexler
        else:
            return 0


obj = MyClass()
obj.add_numbers([1, 2, 5 ])
print("List:", obj.mylist)
number = 7
result = obj.tap(number)
if result != 0:
    print(f" Cemi {number} olanin indexi: {result}")
else:
    print(-1)

