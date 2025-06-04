interface User {
  id: number;
  name: string;
  email?: string;
}

function printUserInfo(user: User): void {
  console.log(`ID:${user.id}`);
  console.log(`Name:${user.name}`);
  console.log(`E-mail:${user.email}`);
}

const jhInfo: User = {
  id: 123459,
  name: 'JHY',
  email: 'tk23@gmail.com',
};

printUserInfo(jhInfo);
