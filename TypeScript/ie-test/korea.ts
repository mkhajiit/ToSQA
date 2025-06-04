import readline from 'readline/promises';
import { buyGun } from './gun';
import { buyTank } from './tank';

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

async function ask(question: string): Promise<string> {
  return rl.question(question);
}

async function buyWeapon() {
  for (let i = 0; i < 2; i++) {
    const gunMoney = await ask('총포상에게 지급할 돈을 입력하세요: ');
    buyGun(Number(gunMoney));
    const tankMoney = await ask('탱크 구입에 사용할 돈을 입력하세요:');
    buyTank(Number(tankMoney));
  }

  rl.close();
}

buyWeapon();
