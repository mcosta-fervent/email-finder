# Railway Deployment Guide for Email Finder

This guide provides step-by-step instructions for deploying the Email Finder app to Railway.app.

## 🚀 Quick Deployment (Recommended)

### Method 1: Deploy via GitHub (Easiest)

1. **Push your code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/your-username/email-finder.git
   git push -u origin main
   ```

2. **Go to Railway.app**
   - Visit [https://railway.app](https://railway.app)
   - Sign in with GitHub

3. **Create New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your email-finder repository

4. **Configure Deployment**
   - Railway will automatically detect it's a Python app
   - Click "Deploy"

5. **Wait for Deployment**
   - Railway will install dependencies and start your app
   - This usually takes 1-2 minutes

6. **Access Your App**
   - Once deployment completes, click the generated URL
   - Your app will be live at `https://your-app-name.up.railway.app`

### Method 2: Deploy via Railway CLI

1. **Install Railway CLI**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login to Railway**
   ```bash
   railway login
   ```

3. **Initialize Railway Project**
   ```bash
   cd email_finder
   railway init
   ```
   - Select "Python" as the project type
   - Follow the prompts

4. **Deploy**
   ```bash
   railway up
   ```

5. **Access Your App**
   - Railway will provide the live URL after deployment

## 📋 Deployment Configuration

### Files Required for Railway

Your project should include these files:

- `app.py` - Main Flask application
- `requirements.txt` - Python dependencies
- `Procfile` - Tells Railway how to start the app
- `runtime.txt` - Specifies Python version (optional)
- `.gitignore` - Specifies files to ignore

### Procfile

The `Procfile` contains:
```
web: gunicorn -b :$PORT app:app
```

This tells Railway to:
- Use Gunicorn as the production server
- Bind to the port provided by Railway (`$PORT`)
- Run the `app` object from `app.py`

### Environment Variables

**REQUIRED**: `ABSTRACT_API_KEY`

This app requires the AbstractAPI key to be set:

1. **Get your API key from AbstractAPI:**
   - Go to [https://www.abstractapi.com/api/email-validation](https://www.abstractapi.com/api/email-validation)
   - Sign up for a free account
   - Get your API key from the dashboard
   - Free tier provides 100 email validations per month

2. **Add the API key to Railway:**
   - Go to your Railway project dashboard
   - Click on the "Variables" tab
   - Click "New Variable"
   - Enter `ABSTRACT_API_KEY` as the name
   - Paste your AbstractAPI key as the value
   - Click "Add"

3. **Redeploy your app:**
   - After adding the variable, Railway will automatically redeploy your app
   - Alternatively, you can manually trigger a redeploy

### Requirements

Make sure `requirements.txt` includes:
```
Flask==3.0.3
requests==2.31.0
beautifulsoup4==4.12.2
dnspython==2.6.1
tldextract==5.1.2
gunicorn==21.2.0
```

**Note**: `smtplib` (Python built-in) is no longer needed as we use AbstractAPI for email validation.

## 🔧 Environment Variables

This app uses AbstractAPI for email validation. You need to set up the following environment variable:

### ABSTRACT_API_KEY

1. **Get your API key from AbstractAPI:**
   - Go to [https://www.abstractapi.com/api/email-validation](https://www.abstractapi.com/api/email-validation)
   - Sign up for a free account
   - Get your API key from the dashboard
   - Free tier provides 100 email validations per month

2. **Add the API key to Railway:**
   - Go to your Railway project dashboard
   - Click on the "Variables" tab
   - Click "New Variable"
   - Enter `ABSTRACT_API_KEY` as the name
   - Paste your AbstractAPI key as the value
   - Click "Add"

3. **Redeploy your app:**
   - After adding the variable, Railway will automatically redeploy your app
   - Alternatively, you can manually trigger a redeploy

The `ABSTRACT_API_KEY` is required for email validation to work.

## 💰 Pricing

Railway offers a free tier that's perfect for this app:
- **$5/month free credit** (enough for this app)
- **512MB RAM** (sufficient for email finding)
- **1GB storage** (more than enough)
- **Custom domains** (with paid plan)

## 🎯 Post-Deployment Tips

### 1. Set Up Custom Domain (Optional)
- Go to project settings
- Click "Domains"
- Add your custom domain
- Configure DNS with your domain registrar

### 2. Monitor Logs
- Go to project dashboard
- Click "Logs" tab
- View real-time application logs
- Debug any issues

### 3. Scale Your App
- Click "Settings"
- Adjust resources if needed
- Increase RAM for heavier usage

### 4. Set Up Automatic Deployments
- Connect GitHub repository
- Enable "Auto-deploy on push"
- Railway will redeploy on every git push

### 5. Monitor API Usage
- AbstractAPI free tier provides 100 validations/month
- Each email candidate counts as one API call (typically 6 candidates per search)
- Monitor your usage at [AbstractAPI Dashboard](https://www.abstractapi.com/dashboard)
- Upgrade plan if you need more validations

## 🛠️ Troubleshooting

### Common Issues

**Issue: App crashes on startup**
- Check logs for error messages
- Make sure all dependencies are in `requirements.txt`
- Verify `Procfile` is correct

**Issue: Email validation not working**
- Check if `ABSTRACT_API_KEY` is set correctly
- Verify your API key is valid at AbstractAPI
- Check Railway logs for error messages

**Issue: Domain resolution failing**
- Try different company names
- Some companies have complex websites
- The app falls back to simple domain guessing

### Debugging

Add this to your `app.py` for better debugging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

View logs in Railway dashboard to see detailed debugging info.

## 🔄 Updates

To update your deployed app:

1. Make changes to your code
2. Update `requirements.txt` if new dependencies added
3. Push to GitHub:
   ```bash
   git add .
   git commit -m "Your changes"
   git push
   ```
4. Railway will automatically redeploy (if auto-deploy enabled)

## 📈 Performance Considerations

- **API Limits**: AbstractAPI free tier limited to 100 validations/month
- **Rate Limiting**: Add 1-second delay between checks to avoid rate limits
- **Caching**: Consider caching results for frequent searches
- **Workers**: Railway free tier uses 1 worker (sufficient for this app)

## 🚨 Important Notes

1. **This is a development/demo app** - Not intended for production spam
2. **Respect privacy and terms of service** of companies you search
3. **Railway free tier has limits** - Monitor your usage
4. **AbstractAPI key is required** for email validation

Your Email Finder app is now ready for Railway deployment! 🎉