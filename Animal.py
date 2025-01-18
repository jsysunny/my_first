class Animal:
    def sound(self):
        print("소리내다")
    def move(self):
        print("움직이다")
    
class Cat(Animal):
    def sound(self):
        print("야옹~",end=" ")
        super().sound()

cat=Cat()
cat.sound()
animal=Animal()
animal.sound()

