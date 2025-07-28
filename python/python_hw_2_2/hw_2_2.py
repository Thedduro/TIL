# 아래에 코드를 작성하시오.
                 
class Product:
    product_count = 0
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.product_count += 1

    def display_info(self, name, price):
        print(f'상품명: {self.name}, 가격: {self.price}원')


p1 = Product('사과', 1000)
p1.display_info(p1.name, p1.price)  # 상품명: 사과, 가격: 1000원
p2 = Product('바나나', 1500)
p2.display_info(p2.name, p2.price)  # 상품명: 바나나, 가격: 1500원
# 상품 개수 출력
print(f'총 상품 수: {Product.product_count}')  # 상품 개수: 2