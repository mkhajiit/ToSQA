import myCart, { IProduct } from '../constants/myCart';

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

printCartList(myCart);
printCostSum(myCart);
printTwiceCost(myCart);
