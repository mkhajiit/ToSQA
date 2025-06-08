export interface IProduct {
  id: number;
  name: string;
  price: number;
}
const myCart: IProduct[] = [
  { id: 1, name: '사과', price: 1000 },
  { id: 2, name: '바나나', price: 1500 },
  { id: 3, name: '딸기', price: 2000 },
  { id: 4, name: '수박', price: 3000 },
];

export default myCart;
