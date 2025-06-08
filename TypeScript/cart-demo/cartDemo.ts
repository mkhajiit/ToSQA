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

function doubleCost(cart: IProduct[]) {
  const double = cart.map((item) => {
    return { id: item.id, name: item.name, price: item.price * 2 };
  });
  console.log(double);
}

printCartItemList(myCart);
printTotalCost(myCart);
doubleCost(myCart);
