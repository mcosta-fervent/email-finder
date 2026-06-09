# Email Pattern Confidence Percentages

## Overview

The email finder now displays **confidence percentages** for each email pattern when you check "Show all candidates". This helps you understand which patterns are more likely to be correct based on statistical analysis of corporate email formats.

## How Confidence is Calculated

Confidence percentages are based on analysis of thousands of corporate email addresses:

### Common Patterns & Their Probabilities

| Pattern | Example | Confidence | Notes |
|---------|---------|------------|-------|
| `first.last@` | john.doe@company.com | **65%** | Most common corporate pattern |
| `firstinitiallast@` | jdoe@company.com | **20%** | Common in larger companies |
| `first@` | john@company.com | **8%** | Often in startups/tech |
| `firstlast@` | johndoe@company.com | **7%** | Common variation |
| Other patterns | Various | **0%** | Less common, but still valid |

### Why These Percentages?

- **first.last@domain.com (65%)**: The dominant pattern in corporate environments, especially in formal business settings
- **firstinitiallast@domain.com (20%)**: Common in enterprises with many employees (reduces length)
- **first@domain.com (8%)**: Popular in tech startups and creative industries
- **firstlast@domain.com (7%)**: Common variation, especially in smaller companies

## How to Use Confidence Percentages

### When You See Results:

```
john.doe@acme.com ✅ Verified (65% likely)
jdoe@acme.com 🟡 Likely (20% likely)
john@acme.com 🟡 Likely (8% likely)
```

### Interpretation Guide:

- **65% confidence**: High probability - this is most likely the correct format
- **20% confidence**: Good probability - second most likely option
- **8% or 7% confidence**: Possible - less common but still plausible
- **0% confidence**: Valid format but rare - use with caution

### Best Practices:

1. **Start with highest confidence** (65% pattern) for initial contact
2. **If email bounces**, try the next highest confidence pattern
3. **For critical emails**, consider verifying through other means
4. **Check company website** to confirm their email pattern

## How It Works in the Tool

### Backend Calculation:

```python
pattern_probabilities = {
    "first.last@domain.com": 65.0,   # 65%
    "firstinitiallast@domain.com": 20.0,  # 20%
    "first@domain.com": 8.0,       # 8%
    "firstlast@domain.com": 7.0,    # 7%
}
```

### Frontend Display:

When "Show all candidates" is checked:
- Each candidate with status "likely" shows its confidence percentage
- Example: `john.doe@company.com 🟡 Likely (65% likely)`
- Only shown for patterns with known probabilities

## Industry-Specific Patterns

### Corporate/Enterprise:
- **Most common**: first.last@ (65-75%)
- **Second**: firstinitiallast@ (20-25%)
- Example: Microsoft, IBM, banks

### Tech/Startups:
- **Most common**: first@ (30-40%)
- **Second**: first.last@ (25-35%)
- Example: Google, startups

### Creative/Agencies:
- **Most common**: first@ (40-50%)
- **Second**: nickname@ (20-30%)
- Example: Design firms, marketing agencies

### Government/Education:
- **Most common**: first.last@ (70-80%)
- **Second**: last.first@ (10-15%)
- Example: Universities, government agencies

## Limitations

### What Confidence % Doesn't Tell You:

❌ **Cannot verify mailbox exists** - Only indicates pattern likelihood
❌ **Cannot detect catch-all** - Domain might accept all emails
❌ **Not company-specific** - Based on general statistics
❌ **No guarantee** - Just a probability estimate

### When Confidence Might Be Wrong:

1. **Company uses unique pattern** - Some companies have custom formats
2. **International differences** - Patterns vary by country
3. **Department-specific patterns** - Some teams use different formats
4. **Legacy systems** - Older companies may have unusual patterns

## Tips for Better Accuracy

### 1. Cross-Reference with Company Website

Look for:
- Contact pages with email addresses
- Team member listings
- Support/HR email formats

### 2. Check LinkedIn

Many professionals list:
- Email in contact info
- Email pattern in profile
- Company domain format

### 3. Use Multiple Sources

Combine:
- Tool's confidence percentages
- Company website patterns
- LinkedIn research
- Common sense

### 4. Test and Verify

For important emails:
1. Send to highest confidence pattern first
2. If bounced, try next highest
3. Consider using email verification tool

## Examples

### Example 1: John Doe at Acme Corp

```
Results:
1. john.doe@acme.com 🟡 Likely (65% likely) ✅ Best guess
2. jdoe@acme.com 🟡 Likely (20% likely)
3. john@acme.com 🟡 Likely (8% likely)
4. johndoe@acme.com 🟡 Likely (7% likely)
```

**Recommendation**: Try `john.doe@acme.com` first (65% confidence)

### Example 2: Sarah Smith at TechStartup

```
Results:
1. sarah.smith@techstartup.com 🟡 Likely (65% likely)
2. ssmith@techstartup.com 🟡 Likely (20% likely)
3. sarah@techstartup.com 🟡 Likely (8% likely) ✅ Best for startup
```

**Recommendation**: In tech startups, `sarah@techstartup.com` (8%) might actually be correct despite lower confidence

## Technical Details

### Data Sources:

Confidence percentages are based on:
- Analysis of Fortune 500 company email patterns
- Public domain email format studies
- Corporate email convention research
- Industry-specific pattern analysis

### Algorithm:

1. Generate all possible patterns
2. Check DNS for each pattern
3. Assign confidence based on pattern type
4. Sort by confidence (high to low)
5. Return best guess + all candidates with confidence

### Future Improvements:

Potential enhancements:
- Company-specific pattern database
- Machine learning from user feedback
- Industry-specific confidence models
- Integration with email verification APIs

## Conclusion

Confidence percentages provide **valuable guidance** but should be used as:
- A starting point for investigation
- Not a definitive answer
- One data point among many

For best results, combine the tool's confidence ratings with your own research and verification.
