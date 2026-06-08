# Email Finder

A local web app for finding and verifying professional email addresses without any paid APIs.

## Features

- ✅ Find professional email addresses using common patterns
- ✅ Verify emails via DNS checks (no API key required)
- 🔍 Resolve company domains from web searches
- 📊 Show verification status (Verified, Likely, Not Found)
- 🎯 Display email patterns and resolved domains
- 🔄 Option to show all candidate emails tried
- 🌀 Loading spinner during verification

## Setup

### Prerequisites
- Python 3.7+
- pip (Python package manager)

### Installation

1. Clone this repository or download the files
2. Install dependencies:

```bash
pip install -r requirements.txt
```

### Running the App Locally

```bash
python app.py
```

The app will be available at: [http://localhost:5000](http://localhost:5000)

### Deploying to Railway.app

1. **Install Railway CLI** (optional but recommended):
   ```bash
   npm i -g @railway/cli
   ```

2. **Login to Railway**:
   ```bash
   railway login
   ```

3. **Initialize Railway project**:
   ```bash
   railway init
   ```

4. **Deploy**:
   ```bash
   railway up
   ```

5. **Alternative: Deploy via GitHub**:
   - Create a new project on [Railway.app](https://railway.app)
   - Connect your GitHub repository
   - Railway will automatically detect the Python app and deploy it
   - Set environment variables if needed (none required for this app)

6. **Access your deployed app**:
   - After deployment completes, Railway will provide you with a live URL
   - Your app will be available at `https://your-app-name.up.railway.app`

## Usage

1. Enter the person's **Full Name** and **Last Name**
2. Enter the **Company Name**
3. Optionally check "Show all candidates" to see all email patterns tried
4. Click "Find Email"
5. Wait for the verification process (may take a few seconds)
6. View the results with verification status

## How It Works

1. **Domain Resolution**: Searches for the company's official website and extracts the root domain
2. **Pattern Generation**: Creates email candidates using common patterns:
   - `firstname@domain.com`
   - `lastname@domain.com`
   - `firstname.lastname@domain.com`
   - `f.lastname@domain.com`
   - `flastname@domain.com`
   - `firstname_lastname@domain.com`

3. **DNS Verification**: Checks each candidate via DNS:
   - **✅ Verified**: Domain has valid MX records (can receive email)
   - **🟡 Likely**: Domain has MX records (accepts email)
   - **❌ Not Found**: Domain doesn't exist or has no mail servers

## Limitations

- Web search for domain resolution may not always find the correct domain
- DNS verification cannot detect catch-all emails without SMTP
- Some domains may block DNS queries

## Dependencies

- Flask - Web framework
- requests - HTTP requests
- beautifulsoup4 - HTML parsing
- dnspython - DNS resolution
- tldextract - Domain extraction

## License

This project is for educational and personal use only. Do not use for spam or unauthorized email collection.