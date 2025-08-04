# Jarvis API Configuration Guide

This guide will help you configure the necessary API keys and credentials for your Jarvis voice assistant.

## 1. WolframAlpha API (for calculations)

### Steps:
1. Go to [WolframAlpha Developer Portal](https://developer.wolframalpha.com/)
2. Sign up for a free account
3. Create a new app to get your API key
4. Copy your API key

### Configuration:
- Open `Calculatenumbers.py`
- Replace `"YOUR_WOLFRAMALPHA_API_KEY"` with your actual API key
- Example: `apikey = "ABCD12-EFGH345678"`

## 2. NewsAPI (for news reading)

### Steps:
1. Go to [NewsAPI.org](https://newsapi.org/)
2. Sign up for a free account
3. Get your API key from the dashboard
4. Copy your API key

### Configuration:
- Open `NewsRead.py`
- Replace `"YOUR_NEWS_API_KEY"` with your actual API key
- Example: `API_KEY = "abcd1234efgh5678ijkl9012mnop3456"`

## 3. Gmail Configuration (for sending emails)

### Steps:
1. Enable 2-Factor Authentication on your Google Account
2. Go to [Google Account Settings](https://myaccount.google.com/)
3. Navigate to Security → App passwords
4. Generate an app password for "Mail"
5. Copy the 16-character app password

### Configuration:
- Open `sendemail.py`
- Replace `"your_email@gmail.com"` with your actual Gmail address
- Replace `"your_app_password"` with your 16-character app password
- Add recipient mappings in the `recipient_mapping` dictionary

### Example:
```python
sender_email = "myemail@gmail.com"
sender_password = "abcd efgh ijkl mnop"  # 16-character app password

recipient_mapping = {
    "mom": "mom@example.com",
    "friend": "friend@gmail.com",
    "work": "colleague@company.com"
}
```

## 4. Testing Your Configuration

After configuring all APIs:

1. Test WolframAlpha: Say "calculate 2 plus 2"
2. Test NewsAPI: Say "news" and choose a category
3. Test Email: Say "write an email" and follow prompts

## Important Security Notes:

- Never commit your actual API keys to version control
- Keep your credentials secure and private
- Use environment variables for production deployments
- For Gmail, always use App Passwords, never your regular password

## Troubleshooting:

- **WolframAlpha**: Ensure your API key is valid and has remaining quota
- **NewsAPI**: Free tier has limited requests per day
- **Gmail**: Make sure 2FA is enabled and you're using an App Password
- **Recipients**: Ensure recipient names in the dictionary match what you say to Jarvis

## Free Tier Limitations:

- **WolframAlpha**: 2,000 queries/month
- **NewsAPI**: 1,000 requests/month
- **Gmail**: Standard Gmail sending limits apply

Happy coding with Jarvis! 🤖
