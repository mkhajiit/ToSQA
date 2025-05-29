import test, { expect } from '@playwright/test';

test('페이지 타이틀 확인', async ({ page }) => {
  await page.goto('https://www.saucedemo.com/');

  await page.locator('#login-button').click();
  const text = await page.locator('.error-message-container.error').textContent();
  expect(text).toBe('Epic sadface: Username is required');

  await page.waitForTimeout(3000);
});
