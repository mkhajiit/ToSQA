import test, { expect } from '@playwright/test';

test.beforeEach(async ({ page }) => {
  await page.goto('https://opensource-demo.orangehrmlive.com/');
});

test('로그인 성공 테스트', async ({ page }) => {
  await page.getByPlaceholder('Username').fill('Admin');
  await page.getByPlaceholder('Password').fill('admin123');

  // name: 텍스트 콘텐츠를 의미
  await page.getByRole('button', { name: 'Login' }).click();

  await expect(page).toHaveURL(
    'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
  );

  await page.waitForTimeout(3000);
});
