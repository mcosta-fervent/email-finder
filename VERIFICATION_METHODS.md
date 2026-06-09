# Verification Methods: DNS vs SMTP

## Overview

The Email Finder now supports **two verification methods**: DNS and SMTP. You can choose which method to use based on your needs.

## Choosing a Verification Method

In the tool interface, you'll see two radio buttons:

- ✅ **DNS** (Default) - Faster, no SMTP connections
- ⭕ **SMTP** - Slower, more accurate (but may have issues on Railway)

## DNS Verification (Recommended)

### How It Works

1. **Validates email format** using regex
2. **Checks domain existence** (A/AAAA DNS records)
3. **Verifies MX records** (mail servers exist)
4. **Confirms MX servers are reachable**

### Pros

✅ **Fast** - DNS queries complete in milliseconds
✅ **Reliable on Railway** - No outbound connection issues
✅ **No timeouts** - Works within Railway's constraints
✅ **No API keys needed** - Completely free
✅ **Works everywhere** - No port restrictions

### Cons

❌ **Cannot verify specific mailbox** - Only checks if domain accepts email
❌ **Cannot detect catch-all** - Domain might accept all emails
❌ **Less accurate** - Only confirms domain validity, not email existence

### When to Use

- ✅ **Default choice** for most users
- ✅ **Railway deployments** (avoids connection issues)
- ✅ **Quick checks** when speed matters
- ✅ **No API key available**

## SMTP Verification (Experimental)

### How It Works

1. **Finds MX records** for the domain
2. **Connects to SMTP server** (port 25)
3. **Simulates sending email** (without actually sending)
4. **Checks server response**:
   - `250` - Email accepted (verified)
   - `251/252` - Catch-all domain (likely)
   - Other codes - Email rejected (invalid)

### Pros

✅ **More accurate** - Can verify if mailbox exists
✅ **Detects catch-all** - Identifies domains that accept all emails
✅ **Standard protocol** - Works with all email servers

### Cons

❌ **Slow** - SMTP handshake takes 1-3 seconds per email
❌ **Railway may block** - Outbound SMTP often restricted
❌ **Timeouts likely** - Railway workers have connection limits
❌ **Unreliable** - Many companies block SMTP checks

### When to Use

- ⚠️ **Local development** (not on Railway)
- ⚠️ **Self-hosted deployments** with SMTP access
- ⚠️ **When you need higher accuracy**
- ⚠️ **For testing purposes**

## Comparison Table

| Feature | DNS | SMTP |
|---------|-----|------|
| **Speed** | ⚡ Very Fast (ms) | 🐢 Slow (1-3s per email) |
| **Accuracy** | ❌ Domain only | ✅ Mailbox verification |
| **Catch-all Detection** | ❌ No | ✅ Yes |
| **Works on Railway** | ✅ Yes | ❌ Often blocked |
| **Connection Issues** | ❌ None | ✅ Likely |
| **API Key Needed** | ❌ No | ❌ No |
| **Best For** | Quick checks | Accurate verification |

## Status Values

Both methods return the same status values:

### DNS Method

- **✅ Verified**: Domain has valid MX records
- **🟡 Likely**: Domain has MX records (same as verified for DNS)
- **❌ Invalid**: Domain doesn't exist or has no mail servers

### SMTP Method

- **✅ Verified**: Server explicitly accepted the email address
- **🟡 Likely**: Server is catch-all (accepts everything)
- **❌ Invalid**: Address rejected or timed out

## Technical Details

### DNS Verification Flow

```
1. Check email format regex
2. Query domain A/AAAA records
3. Query domain MX records
4. Verify MX servers exist
5. Return "likely" if all checks pass
```

### SMTP Verification Flow

```
1. Query domain MX records
2. Connect to SMTP server (port 25)
3. Send HELO command
4. Send MAIL FROM command
5. Send RCPT TO command
6. Check response code
7. Return status based on code
```

## Performance Impact

### DNS Method

- **Time per email**: 50-200ms
- **6 candidates**: ~1 second total
- **Railway timeout risk**: None

### SMTP Method

- **Time per email**: 1-3 seconds
- **6 candidates**: 6-18 seconds total
- **Railway timeout risk**: High (worker timeout = 60s)
- **Connection failures**: Common

## Recommendations

### For Railway Users

**Use DNS method** (default):
- ✅ Works reliably
- ✅ No timeouts
- ✅ Fast results
- ✅ Good enough for most use cases

### For Local Development

**Try SMTP method**:
- ✅ More accurate
- ✅ Detects catch-all
- ⚠️ May still fail (some companies block SMTP checks)

### For Self-Hosted

**Choose based on needs**:
- **Speed needed?** → DNS
- **Accuracy needed?** → SMTP
- **SMTP port open?** → SMTP
- **SMTP blocked?** → DNS

## Troubleshooting

### SMTP Issues on Railway

**Symptom**: "Network is unreachable" or timeout errors

**Solution**:
- Switch to DNS method (recommended)
- Railway blocks outbound SMTP (port 25)
- This is a platform limitation

### SMTP Connection Refused

**Symptom**: "Connection refused" for specific domains

**Solution**:
- Some companies block SMTP verification
- Try DNS method instead
- This is expected behavior

### Slow SMTP Verification

**Symptom**: Taking too long (more than 3s per email)

**Solution**:
- Switch to DNS for faster results
- SMTP requires multiple round-trips
- DNS is instantaneous

## Best Practices

### General

1. **Start with DNS** (default)
2. **Use SMTP only if needed**
3. **Check "Show all candidates"** to see all patterns
4. **Combine with confidence %** for better guesses

### For Accuracy

1. Try DNS first
2. If unsure, check company website for email format
3. Use LinkedIn to verify pattern
4. Consider sending test email

### For Speed

1. Use DNS method
2. Don't check "Show all candidates" unless needed
3. Accept first reasonable result

## Future Improvements

Potential enhancements:
- **Hybrid mode**: Try SMTP, fallback to DNS
- **Caching**: Cache DNS/SMTP results
- **Bulk verification**: Verify multiple emails efficiently
- **Rate limiting**: Control verification speed

## Conclusion

| Scenario | Recommended Method |
|----------|-------------------|
| **Railway deployment** | DNS ✅ |
| **Local development** | SMTP (try it) |
| **Self-hosted** | SMTP (if works) |
| **Quick checks** | DNS ✅ |
| **Accurate verification** | SMTP (if available) |

**DNS method is recommended for most users**, especially on Railway. SMTP is provided for completeness but may not work reliably in all environments.
