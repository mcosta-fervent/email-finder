#!/usr/bin/env python3
"""
Email Finder Backend
Finds and verifies professional email addresses using domain resolution and SMTP verification
"""

import os
import re
import socket
import smtplib
import dns.resolver
import time
from flask import Flask, request, jsonify, render_template
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup
import tldextract

app = Flask(__name__)

# Configure templates folder
app.template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')

# Configure static folder
app.static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')

def resolve_company_domain(company_name):
    """
    Search for company website and extract root domain
    Skip social media, Wikipedia, and other non-official sites
    """
    try:
        # First try simple domain guess
        simple_domain = f"{company_name.lower().replace(' ', '')}.com"
        try:
            # Check if domain has MX records
            dns.resolver.resolve(simple_domain, 'MX')
            return simple_domain
        except:
            pass

        # Try to find company website via search
        search_url = f"https://www.google.com/search?q={company_name}+official+website"
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

        response = requests.get(search_url, headers=headers, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract search results
        for link in soup.find_all('a'):
            href = link.get('href')
            if href and href.startswith('/url?q='):
                url = href.split('/url?q=')[1].split('&')[0]
                domain = tldextract.extract(url).registered_domain

                # Skip social media and common non-official sites
                skip_domains = ['linkedin', 'wikipedia', 'crunchbase', 'facebook', 'twitter', 'instagram', 'youtube', 'glassdoor']
                if any(skip in domain.lower() for skip in skip_domains):
                    continue

                # Check if domain has MX records
                try:
                    dns.resolver.resolve(domain, 'MX')
                    return domain
                except:
                    continue

        return None

    except Exception as e:
        print(f"Error resolving domain: {e}")
        return None

def generate_email_candidates(first_name, last_name, domain):
    """
    Generate email candidates from common patterns
    """
    first = first_name.lower()
    last = last_name.lower()

    patterns = [
        f"{first}@{domain}",
        f"{last}@{domain}",
        f"{first}.{last}@{domain}",
        f"{first[0]}.{last}@{domain}",
        f"{first}{last}@{domain}",
        f"{first}_{last}@{domain}"
    ]

    return list(set(patterns))  # Remove duplicates

def verify_email_smtp(email, timeout=3):
    """
    Verify email via SMTP without sending mail
    Returns: 'verified', 'likely' (catch-all), or 'invalid'
    """
    domain = email.split('@')[1]

    try:
        # Get MX records
        mx_records = dns.resolver.resolve(domain, 'MX')
        mx_hosts = sorted([str(record.exchange) for record in mx_records], key=lambda x: x.lower())

        if not mx_hosts:
            return 'invalid'

        # Try each MX server
        for mx_host in mx_hosts:
            try:
                # Connect to SMTP server
                with smtplib.SMTP(timeout=timeout) as server:
                    server.set_debuglevel(0)
                    server.connect(mx_host, 25)

                    # SMTP conversation
                    server.helo(server.local_hostname)
                    server.mail('test@example.com')

                    # Check if address is accepted
                    code, _ = server.rcpt(email)

                    if code == 250:
                        return 'verified'
                    elif code == 251 or code == 252:
                        # These might indicate catch-all
                        return 'likely'
                    else:
                        return 'invalid'

            except (smtplib.SMTPConnectError, smtplib.SMTPException, socket.timeout, socket.gaierror) as e:
                continue

        return 'invalid'

    except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers, dns.resolver.Timeout) as e:
        return 'invalid'
    except Exception as e:
        print(f"SMTP verification error for {email}: {e}")
        return 'invalid'

@app.route('/')
def index():
    """Serve the main page"""
    return render_template('index.html')

@app.route('/find_email', methods=['POST'])
def find_email():
    """Find and verify email address"""
    try:
        data = request.json
        first_name = data.get('first_name', '').strip()
        last_name = data.get('last_name', '').strip()
        company_name = data.get('company_name', '').strip()
        show_all = data.get('show_all', False)

        if not first_name or not last_name or not company_name:
            return jsonify({
                'error': 'Please provide first name, last name, and company name'
            }), 400

        # Step 1: Resolve domain
        domain = resolve_company_domain(company_name)

        if not domain:
            return jsonify({
                'error': f'Could not resolve domain for {company_name}'
            }), 404

        # Step 2: Generate candidates
        candidates = generate_email_candidates(first_name, last_name, domain)

        # Step 3: Verify candidates
        results = []
        best_email = None
        best_status = None
        best_pattern = None

        for email in candidates:
            status = verify_email_smtp(email)
            results.append({
                'email': email,
                'status': status
            })

            # Track best result
            if status == 'verified' and best_status != 'verified':
                best_email = email
                best_status = status
                best_pattern = email.split('@')[0]
            elif status == 'likely' and best_status not in ['verified', 'likely']:
                best_email = email
                best_status = status
                best_pattern = email.split('@')[0]
            elif not best_email:
                best_email = email
                best_status = status
                best_pattern = email.split('@')[0]

            # Small delay between checks
            time.sleep(1)

        # Step 4: Return results
        response = {
            'best_email': best_email,
            'status': best_status,
            'pattern': best_pattern,
            'domain': domain,
            'candidates': results if show_all else []
        }

        return jsonify(response)

    except Exception as e:
        print(f"Error in find_email: {e}")
        return jsonify({
            'error': f'An error occurred: {str(e)}'
        }), 500

if __name__ == '__main__':
    # For local development
    app.run(debug=True, port=5000)

# For production (Railway will use Gunicorn)