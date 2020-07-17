class Cat:
    color = 'red'
    sound = '야옹 '

    #생성자 메소드
    def __init__(self , name , color, sound):
        self.name = name
        self.color = color
        self.sound = sound
    
    def meow(self,name,sound):
        print('우리 고양이는 못생긴 {} 이에요. '.format(name))
        print("길냥이 {}색깔이 {}구요 자주 {} {} 거려요".format(self.name,self.color, self.sound ,sound))

     gang_cat = Cat('미옹','컬러풀한','미아옹' )
    # jong_cat = Cat('태경','똥이')
     gang_cat.meow('라온','미옹')
    # jong_cat.meow('라온')