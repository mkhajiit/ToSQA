import myCart, { IProduct } from '../constants/myCart';

function printFilteredItemList(cart: IProduct[]) {
  const filtered = cart.filter((item) => item.price >= 1500);
  filtered.forEach((item) => console.log(`상품명: ${item.name}, 가격: ${item.price}원`));
}

function printFilteredItemSum(cart: IProduct[]) {
  const filteredList = cart.filter((item) => item.price >= 1500);
  console.log(filteredList.reduce((acc, item) => acc + item.price, 0));
}
printFilteredItemList(myCart);
printFilteredItemSum(myCart);
