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

## 🔧 Environment Variables

This app doesn't require any environment variables, but if you need to add any:

1. Go to your Railway project
2. Click on "Variables" tab
3. Add any required variables
4. Redeploy

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

## 🛠️ Troubleshooting

### Common Issues

**Issue: App crashes on startup**
- Check logs for error messages
- Make sure all dependencies are in `requirements.txt`
- Verify `Procfile` is correct

**Issue: SMTP verification not working**
- Some companies block SMTP checks
- This is expected behavior
- The app handles this gracefully

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

- **SMTP Timeouts**: Each email check has 3-second timeout
- **Rate Limiting**: Add 1-second delay between checks to avoid blocking
- **Caching**: Consider caching domain lookups for frequent searches
- **Workers**: Railway free tier uses 1 worker (sufficient for this app)

## 🚨 Important Notes

1. **This is a development/demo app** - Not intended for production spam
2. **Respect privacy and terms of service** of companies you search
3. **Railway free tier has limits** - Monitor your usage
4. **SMTP verification may be blocked** by some companies

Your Email Finder app is now ready for Railway deployment! 🎉