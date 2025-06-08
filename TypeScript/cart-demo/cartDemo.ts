import myCart, { IProduct } from '../constants/myCart';

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
