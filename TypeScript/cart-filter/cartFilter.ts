import myCart, { IProduct } from '../constants/myCart';

function printFilteredItemList(cart: IProduct[]) {
  const filtered = cart.filter((item) => item.price >= 1500);
  filtered.forEach((item) => console.log(`상품명: ${item.name}, 가격: ${item.price}원`));
}

function printFilteredItemSum(cart: IProduct[]) {
  const filteredList = cart.filter((item) => item.price >= 1500);
  console.log(
    '필터된 상품들의 가격합:',
    filteredList.reduce((acc, item) => acc + item.price, 0)
  );
}

function printAverageItem(cart: IProduct[]) {
  const average = cart.reduce((acc, item) => acc + item.price / cart.length, 0);
  console.log('카트에 담긴 제품들 가격의 평균:', average);
}

function printSortedItem(cart: IProduct[]) {
  const sorted = cart.sort((a, b) => b.price - a.price); // 가격 역순으로 정렬
  console.log('카트의 제품을 가격 높은순으로 정렬:', sorted);
}

function printName(cart: IProduct[]) {
  const nameList = cart.map((item) => item.name);
  console.log('카트에 담긴 제품들의 이름:', nameList);
}
printFilteredItemList(myCart);
printFilteredItemSum(myCart);
printAverageItem(myCart);
printSortedItem(myCart);
printName(myCart);
