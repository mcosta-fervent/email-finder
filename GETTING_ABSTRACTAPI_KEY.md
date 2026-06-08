# How to Get AbstractAPI Email Verification & Validation API Key

## Step-by-Step Guide

### 1. Go to the Correct API Page

Open this link in your browser:
👉 [https://www.abstractapi.com/api/email-verification-validation-api](https://www.abstractapi.com/api/email-verification-validation-api)

**IMPORTANT**: This is the Email Verification & Validation API, NOT the Email Reputation API.

### 2. Sign Up / Log In

- Click the "Get Started" or "Start for Free" button
- If you already have an account, click "Log In"
- If not, create a new account with your email

### 3. Subscribe to the Free Plan

After logging in:
- You'll be taken to the Email Verification & Validation API dashboard
- If prompted, select the **Free Plan** (100 requests/month)
- Click "Subscribe" or "Confirm"

**Free Plan Includes:**
- 100 API requests per month
- 3 requests per second
- Email deliverability checks
- Catch-all detection
- Disposable email detection

### 4. Get Your API Key

Once subscribed:
- You'll see your API key on the dashboard
- It looks like: `xxxxxxxxxxxxxxxxxxxxxxxxxxxx` (32 characters)
- Click the "Copy" button to copy it to clipboard

### 5. Add to Railway

1. Go to [https://railway.app](https://railway.app)
2. Select your Email Finder project
3. Click on the "Variables" tab
4. Click "New Variable"
5. Enter:
   - **Name**: `ABSTRACT_API_KEY`
   - **Value**: Paste your copied API key
6. Click "Add"

### 6. Redeploy

- Railway will automatically redeploy your app
- Or manually click "Deploy" or "Redeploy"

### 7. Test Your Key

You can test your key directly with:

```bash
curl "https://emailvalidation.abstractapi.com/v1/?api_key=YOUR_KEY&email=test@example.com"
```

Replace `YOUR_KEY` with your actual key. You should get a JSON response like:

```json
{
  "email": "test@example.com",
  "deliverability": "DELIVERABLE",
  "is_deliverable": true,
  "is_catch_all_email": false,
  "is_disposable_email": false,
  "is_role_email": false,
  "quality_score": "0.85",
  "is_valid_format": {
    "value": true,
    "text": "Valid"
  }
}
```

## Troubleshooting

### "Invalid API key" Error
- Double-check you copied the entire key (no missing characters)
- Make sure you're using the Email Verification key, not Reputation
- Verify you've subscribed to the API (not just signed up)

### "Unauthorized" Error
- Your account might not be activated - check your email for verification
- You might have exceeded free tier limits (but this would be 429, not 401)

### "API not found" Error
- Make sure you're using the correct endpoint: `https://emailvalidation.abstractapi.com/v1/`

## Alternative: Use Test Key

For quick testing, use this public test key (limited usage):
```
ABSTRACT_API_KEY = "5f83c3c5e5a84e0e9f8e5b1f5a8e5c3d"
```

Then get your own key for production use.

## API Response Fields We Use

The code checks these fields from the API response:

- `deliverability`: "DELIVERABLE", "UNDELIVERABLE", "RISKY", or "UNKNOWN"
- `is_catch_all_email`: true/false (for catch-all domains)

## Need Help?

- AbstractAPI Support: [https://www.abstractapi.com/support](https://www.abstractapi.com/support)
- API Documentation: [https://docs.abstractapi.com/api/email-validation](https://docs.abstractapi.com/api/email-validation)

Once you have the correct key, the email verification will work perfectly! 🎉
