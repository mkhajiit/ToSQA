import test, { expect } from '@playwright/test';

// 파일 내 테스트들이 테스트 시작 전에 반드시 실행함
test.beforeEach(async ({ page }) => {
  await page.goto('https://www.saucedemo.com/');
  await page.fill('#user-name', 'standard_user');
  await page.fill('#password', 'secret_sauce');
  await page.click('#login-button');
});

// 로그인 성공 확인
test('로그인 성공 확인', async ({ page }) => {
  // const text = await page.locator('.error-message-container.error').textContent();
  await expect(page).toHaveURL('https://www.saucedemo.com/inventory.html');

  await page.waitForTimeout(3000);
});
