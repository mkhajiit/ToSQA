import test, { expect } from '@playwright/test';

test('페이지 타이틀 확인', async ({ page }) => {
  await page.goto('https://www.saucedemo.com/');

  const title = await page.title();
  console.log(title);
  await page.locator('#login-button').click();
  expect(title).toBe('Swag Labs');
});
