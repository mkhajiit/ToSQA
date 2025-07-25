import { defineConfig } from '@playwright/test';

export default defineConfig({
  projects: [
    {
      name: 'first',
      testDir: './Playwright/first-project/tests',
    },
    {
      name: 'second',
      testDir: './Playwright/second-project/tests',
    },
    {
      name: 'orangeHRM',
      testDir: './Playwright/orangeHRM/tests',
    },
  ],
  use: {
    headless: false,
    launchOptions: {
      slowMo: 300, // 이렇게 넣어야 타입스크립트 오류 안 남
    },
  },
});
