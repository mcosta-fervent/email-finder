# Improving Email Address Accuracy

## Understanding the Limitations

The current DNS-only verification has some inherent limitations:

1. **Cannot verify specific mailbox exists** - Only checks if domain can receive email
2. **Cannot detect catch-all emails** - Some domains accept all emails
3. **Depends on pattern guessing** - We generate common patterns, but can't know for sure

## How to Get Better Results

### 1. Provide Accurate Input

**First Name & Last Name:**
- Use full legal names (not nicknames)
- Example: "Jonathan" instead of "Jon"
- Avoid middle names unless commonly used

**Company Name:**
- Use official company name
- Example: "Acme Corporation" not "Acme Corp" or "Acme"
- Check company website for exact name

### 2. Understand Common Email Patterns

Most companies use one of these patterns:

1. **first.last@company.com** (Most common - 60-70%)
   - john.doe@company.com
   - mary.smith@company.com

2. **firstinitiallast@company.com** (20-25%)
   - jdoe@company.com
   - msmith@company.com

3. **first@company.com** (5-10%)
   - john@company.com
   - mary@company.com

4. **firstlast@company.com** (5-10%)
   - johndoe@company.com
   - marysmith@company.com

### 3. Check Multiple Sources

**Company Website:**
- Look for "Contact Us" or "Team" pages
- Check email format of listed contacts

**LinkedIn:**
- Search for the person on LinkedIn
- Some profiles show email patterns
- Check if they list contact info

**Email Signature:**
- If you've received emails from the company
- Check the sender's email format

### 4. Use the "Show All Candidates" Option

When searching, check "Show all candidates" to see all patterns tried.

If you know the company's pattern, you can:
- Manually select the most likely one
- Try variations based on known patterns

### 5. Common Company-Specific Patterns

Some companies have unique patterns:

**Large Corporations:**
- Often use: first.last@company.com
- Sometimes: first_initial+last@company.com

**Startups/Tech:**
- Often use: first@company.com
- Sometimes: nickname@company.com

**Government/Education:**
- Often use: first.last@department.company.edu
- Sometimes: last_first@company.edu

**International Companies:**
- Varies by country/culture
- Example (Germany): last.f@company.de
- Example (France): first-last@company.fr

### 6. When Results Are Wrong

**If getting "Not Found" for valid domains:**
- Domain may have strict DNS configuration
- Try searching with different company name variations
- Some companies use parent company domains

**If patterns seem wrong:**
- The most common pattern (first.last) may not be what the company uses
- Try checking known emails from that company
- Company culture affects naming (formal vs informal)

### 7. Alternative Verification Methods

If you need to verify an email exists:

**Send a Test Email:**
- Use a tool like Mailtester or Hunter's verifier (free tier)
- Or send a polite email asking to confirm receipt

**Use a Paid API (for critical needs):**
- Hunter.io (50 free/month)
- ZeroBounce (100 free/month)
- NeverBounce (10 free)

### 8. Best Practices

✅ **Do:**
- Try multiple name variations (Jonathan, Jon, John)
- Check company website for email format clues
- Use LinkedIn to find contact info
- Combine first+last in different ways

❌ **Don't:**
- Assume all companies use the same pattern
- Rely solely on automated tools
- Use for spam or unsolicited emails
- Expect 100% accuracy from pattern guessing

## How the Tool Works

1. **Finds company domain** (e.g., acme.com)
2. **Generates common patterns** (john.doe@acme.com, etc.)
3. **Checks DNS** (does domain accept email?)
4. **Returns most likely pattern**

## Accuracy Statistics

| Method | Accuracy | What It Checks |
|--------|----------|----------------|
| DNS Only | 60-70% | Domain exists + has mail servers |
| SMTP | 80-90% | Can verify mailbox (but Railway blocks) |
| Paid API | 90-95% | Full verification + catch-all detection |

## Recommendations

For **personal use** (finding a few emails):
- DNS method is sufficient
- Check multiple patterns manually

For **business use** (many emails):
- Consider adding a paid API
- Implement user feedback to improve patterns
- Add manual verification step for critical emails

For **development/testing:**
- Current method works well
- No API keys needed
- Fast and reliable on Railway
