const { test, expect } = require('@playwright/test');

test.describe('Tichi Application - Login Automation Suite', () => {

    test.beforeEach(async ({ page }) => {
        // Navigate to the target application environment
        await page.goto('https://tichi-app-webapp-stage.web.app');
    });

    test('Successful Login with Valid Credentials', async ({ page }) => {
        // Elements should be replaced with actual IDs/Test IDs if available
        await page.fill('input[type="email"]', 'valid.user@example.com');
        await page.fill('input[type="password"]', 'SecurePassword123!');
        await page.click('button:has-text("Log In")');

        // Assert successful redirection to Dashboard
        await expect(page).toHaveURL(/.*dashboard/);
        await expect(page.locator('.welcome-message')).toBeVisible();
    });

    test('Login Failure with Invalid Email Format', async ({ page }) => {
        await page.fill('input[type="email"]', 'invalidemailformat');
        await page.fill('input[type="password"]', 'Password123');
        await page.click('button:has-text("Log In")');

        // Assert that validation triggers and prevents login
        const errorMessage = page.locator('.error-message');
        await expect(errorMessage).toBeVisible();
        await expect(errorMessage).toContainText('Please enter a valid email address');
    });
});
