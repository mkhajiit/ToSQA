// import test, { expect } from '@playwright/test';

// test.beforeEach(async ({ page }) => {
//   await page.goto('https://opensource-demo.orangehrmlive.com/');
// });
// test('로그인 성공 테스트', async ({ page }) => {
//   await page.fill('[name = "username"]', 'Admin');
//   await page.fill('[name = "password"]', 'admin123');
//   await page.click('.orangehrm-login-button');

//   await expect(page).toHaveURL(
//     'https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index'
//   );

//   await page.waitForTimeout(4000);
// });

// test('로그인 실패 테스트', async ({ page }) => {
//   await page.fill('[name = "username"]', 'Admin12');
//   await page.fill('[name = "password"]', 'admin12345');
//   await page.click('.orangehrm-login-button');

//   await expect(page.locator('.oxd-alert.oxd-alert--error')).toBeVisible();
// });
