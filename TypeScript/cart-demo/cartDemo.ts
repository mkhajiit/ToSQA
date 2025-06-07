interface IProduct {
  id: number;
  name: string;
  price: number;
}

const myCart: IProduct[] = [
  { id: 1, name: '사과', price: 1000 },
  { id: 2, name: '바나나', price: 1500 },
  { id: 3, name: '딸기', price: 2000 },
];

function printCartItemList(cart: IProduct[]) {
  cart.forEach((item) => {
    console.log(`id:${item.id} 이름:${item.name}, 가격:${item.price}`);
  });
}

function printTotalCost(cart: IProduct[]) {
  const result = cart.reduce((total, item) => total + item.price, 0);
  console.log(result);
}

printCartItemList(myCart);
printTotalCost(myCart);
