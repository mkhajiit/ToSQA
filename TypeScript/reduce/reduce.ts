const numberList: number[] = [10, 30, 70, 100, 180];

const sum: number = numberList.reduce((acc, item) => acc + item, 0);

console.log(sum);
