# 배송비 계산하기
# 조건 - 주문 상품가격이 20,000원 미만이면 배송비(2,500원) 포함, 아니면 무료배송


def price(unitprice, quantity):
    delevery_fee = 2500 #배송비
    price = unitprice * quantity #상품가격 = 단위당 상품가격 * 수량
    if price < 20000:
        price += delevery_fee
        return price
    else:
        return price

# 15000원 2개 구매
p1 = price(15000, 2)  # 15000원 2개 구매
p2 = price(5000, 3)   #  5000원 3개 구매

print("상품 가격1은 " + format(p1, ',d') + "원 입니다.")
print("상품 가격2은 " + format(p2, ',d') + "원 입니다.")
