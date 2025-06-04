export function buyTank(money: number) {
  if (money > 100) {
    console.log('K2 흑표 전차 구매 완료');
  } else if (money <= 100 && money > 30) {
    console.log('고물 셔먼 전차 구매 완료');
  } else {
    console.log('거래 실패');
  }
}
