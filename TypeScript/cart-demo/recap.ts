interface IProduct {
  id: number;
  name: string;
  price: number;
}

const myAnotherCart: IProduct[] = [
  { id: 1, name: '사과', price: 1000 },
  { id: 2, name: '바나나', price: 1500 },
  { id: 3, name: '딸기', price: 2000 },
  { id: 4, name: '포도', price: 3000 },
];

function printCartList(cart: IProduct[]) {
  cart.forEach((item) => {
    console.log(`id:${item.id} name:${item.name} price: ${item.price}`);
  });
}

function printCostSum(cart: IProduct[]) {
  console.log(cart.reduce((acc, item) => acc + item.price, 0));
}

function printTwiceCost(cart: IProduct[]) {
  const twicedCostCartList = cart.map((item) => ({
    id: item.id,
    name: item.name,
    price: item.price * 2,
  }));
  console.log(twicedCostCartList);
}

printCartList(myAnotherCart);
printCostSum(myAnotherCart);
printTwiceCost(myAnotherCart);
