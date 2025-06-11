import test, { expect } from '@playwright/test';

test('회원가입 테스트', async ({ page }) => {
  await page.goto('https://automationexercise.com/');
  await page.click('a[href="/login"]');

  await page.fill('[data-qa="signup-name"]', 'myName');
  await page.fill('[data-qa="signup-email"]', 'test123yj@gmail.com');

  await page.click('[data-qa="signup-button"]');

  await expect(page).toHaveURL('https://automationexercise.com/signup');

  await page.waitForTimeout(2000);
});
