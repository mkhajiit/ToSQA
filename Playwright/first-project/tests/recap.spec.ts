import test, { expect } from '@playwright/test';

test.beforeEach(async ({ page }) => {
  await page.goto('https://www.saucedemo.com/');
  await page.fill('#user-name', 'standard_user');
  await page.fill('#password', 'secret_sauce');
  await page.click('#login-button');
});

test('로그인 성공 확인', async ({ page }) => {
  await expect(page).toHaveURL('https://www.saucedemo.com/inventory.html');

  await page.waitForTimeout(2000);
});

test('로그아웃 테스트', async ({ page }) => {
  await page.click('#react-burger-menu-btn');
  await page.click('#logout_sidebar_link');

  await expect(page).toHaveURL('https://www.saucedemo.com/');
});
