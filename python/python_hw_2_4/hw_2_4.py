# 아래에 코드를 작성하시오.
class Animal:
    def __init__(self, name):
        self.name = name

    # Animal 클래스는 speak 메서드를 가진다. 이 메서드는 자식 클래스에서 오버라이딩된다.
    def speak(self):
        '''
            Animal class를 상속받을 자식 클래스들이 모두 speak 메서드를 각자의 역할로써 정의하고 있다.

            아무 기능도 하지 않을 speak 메서드를 왜 Animal 클래스에 정의 한걸까?
            나중에 만들 Dog, Cat 클래스가 Animal 클래스를 상속 받아서
            각각 speak 메서드를 따로 가지게 될 건데, 왜 굳이 Animal 클래스에 정의할까?

            Animal class를 상속받을 자식 클래스들이 모두 speak 메서드를 각자의 역할로써 정의하고 있다.
            즉, 하위 클래스들이 모두 공통적으로 speak 메서드를 가지고 있을 것이다라는 사실을 명시
        '''
        # 특별한 동작이 정의되어 있지 않네?
        pass    # 문법적으로 문제가 되지 않도록 pass 입력한다.

        
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
class Cat(Animal):
    def speak(self):
        return "Meow!"

class Flyer:
    def fly(self):
        return "Flying"

class Swimmer:
    def swim(self):
        return "Swimming"
    
class Duck(Flyer, Swimmer, Animal):

    def speak(self):
        return "Quack"
    
def make_animal_sound(instance): # 이 함수는 Animal 타입의 객체를 인자로 받아, 해당 객체의 speak 메서드를 호출하고 결과를 출력한다.
    print(instance.speak())


dog1 = Dog('치와와')
cat1 = Cat('페르시안 블루')
duck1 = Duck('거위')

make_animal_sound(dog1)  
make_animal_sound(cat1)  
make_animal_sound(duck1)  