Here's a comprehensive guide to **Informatica Expression Transformation Functions** with practical examples:

## 1. STRING FUNCTIONS

### **SUBSTR** - Extract substring
```
SUBSTR(string, start_position, length)
```
**Examples:**
- `SUBSTR('John Doe', 1, 4)` → 'John'
- `SUBSTR(Email, 1, INSTR(Email, '@') - 1)` → Extract username from email
- `SUBSTR(Phone, 7, 4)` → Extract last 4 digits

### **INSTR** - Find position of substring
```
INSTR(string, search_string, [start_position], [occurrence])
```
**Examples:**
- `INSTR('john@gmail.com', '@')` → 5
- `INSTR(Address, 'Street')` → Find if 'Street' exists
- `INSTR(Full_Name, ' ', 1, 2)` → Position of 2nd space

### **LENGTH** - Get string length
```
LENGTH(string)
```
**Examples:**
- `LENGTH('Hello')` → 5
- `IIF(LENGTH(Phone) = 10, 'Valid', 'Invalid')` → Validate phone length
- `LENGTH(LTRIM(RTRIM(Name)))` → Length after trimming spaces

### **UPPER / LOWER** - Change case
```
UPPER(string) / LOWER(string)
```
**Examples:**
- `UPPER('john')` → 'JOHN'
- `LOWER(Email)` → Standardize email to lowercase
- `UPPER(SUBSTR(First_Name, 1, 1)) || LOWER(SUBSTR(First_Name, 2))` → Capitalize first letter

### **LTRIM / RTRIM / TRIM** - Remove spaces
```
LTRIM(string, [trim_characters])
RTRIM(string, [trim_characters])
```
**Examples:**
- `LTRIM('  Hello')` → 'Hello'
- `RTRIM(Name)` → Remove trailing spaces
- `LTRIM(RTRIM(Address))` → Remove both leading and trailing spaces

### **LPAD / RPAD** - Pad strings
```
LPAD(string, length, pad_string)
RPAD(string, length, pad_string)
```
**Examples:**
- `LPAD(Employee_ID, 6, '0')` → '000123' (6 digits with leading zeros)
- `RPAD(Name, 20, ' ')` → Pad name to 20 characters
- `LPAD(Invoice_No, 10, '0')` → '0000045678'

### **CONCAT / ||** - Concatenate strings
```
string1 || string2 || string3
CONCAT(string1, string2)
```
**Examples:**
- `First_Name || ' ' || Last_Name` → 'John Doe'
- `'EMP' || LPAD(TO_CHAR(Emp_ID), 5, '0')` → 'EMP00123'
- `City || ', ' || State || ' ' || Zip` → 'New York, NY 10001'

### **REPLACE** - Replace substring
```
REPLACE(string, old_string, new_string)
```
**Examples:**
- `REPLACE(Phone, '-', '')` → Remove hyphens from phone
- `REPLACE(SSN, '-', '')` → '123456789'
- `REPLACE(Description, 'NULL', '')` → Remove NULL text

### **REG_EXTRACT** - Extract using regex
```
REG_EXTRACT(string, pattern, position)
```
**Examples:**
- `REG_EXTRACT(Email, '([^@]+)@', 1)` → Extract username
- `REG_EXTRACT(Phone, '[0-9]{3}', 1)` → Extract area code
- `REG_EXTRACT(URL, 'https?://([^/]+)', 1)` → Extract domain

### **REG_REPLACE** - Replace using regex
```
REG_REPLACE(string, pattern, replace_string)
```
**Examples:**
- `REG_REPLACE(Phone, '[^0-9]', '')` → Keep only digits
- `REG_REPLACE(Text, '[^A-Za-z0-9 ]', '')` → Remove special characters

### **REG_MATCH** - Check pattern match
```
REG_MATCH(string, pattern)
```
**Examples:**
- `REG_MATCH(Email, '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$')` → Validate email
- `REG_MATCH(Phone, '^[0-9]{10}$')` → Validate 10-digit phone

---

## 2. NUMERIC FUNCTIONS

### **ROUND** - Round numbers
```
ROUND(number, [precision])
```
**Examples:**
- `ROUND(123.456, 2)` → 123.46
- `ROUND(Salary, 0)` → Round to nearest integer
- `ROUND(Price * 1.15, 2)` → Add 15% tax and round

### **TRUNC** - Truncate numbers
```
TRUNC(number, [precision])
```
**Examples:**
- `TRUNC(123.456, 2)` → 123.45
- `TRUNC(Sales_Amount, 0)` → Remove decimal part
- `TRUNC(Price)` → Integer part only

### **CEIL / FLOOR** - Round up/down
```
CEIL(number) / FLOOR(number)
```
**Examples:**
- `CEIL(4.3)` → 5
- `FLOOR(4.9)` → 4
- `CEIL(Total_Items / 12)` → Calculate number of dozens needed

### **ABS** - Absolute value
```
ABS(number)
```
**Examples:**
- `ABS(-50)` → 50
- `ABS(Actual - Budget)` → Variance (always positive)
- `ABS(Balance)` → Absolute balance

### **POWER** - Exponentiation
```
POWER(base, exponent)
```
**Examples:**
- `POWER(2, 3)` → 8
- `POWER(1 + Interest_Rate, Years)` → Compound interest factor
- `POWER(10, 6)` → 1000000

### **SQRT** - Square root
```
SQRT(number)
```
**Examples:**
- `SQRT(16)` → 4
- `SQRT(Area)` → Side of square

### **MOD** - Modulus/Remainder
```
MOD(dividend, divisor)
```
**Examples:**
- `MOD(10, 3)` → 1
- `IIF(MOD(Employee_ID, 2) = 0, 'Even', 'Odd')` → Check even/odd
- `MOD(Row_Number, 100)` → Cycle through 0-99

---

## 3. DATE FUNCTIONS

### **SYSDATE** - Current system date
```
SYSDATE
```
**Examples:**
- `SYSDATE` → Current date and time
- `TRUNC(SYSDATE)` → Today's date (no time)
- `SYSDATE + 7` → Date 7 days from now

### **TO_DATE** - Convert string to date
```
TO_DATE(string, format)
```
**Examples:**
- `TO_DATE('2024-01-15', 'YYYY-MM-DD')` → Date value
- `TO_DATE(Date_String, 'MM/DD/YYYY')` → Convert US format
- `TO_DATE('15-JAN-2024', 'DD-MON-YYYY')` → Convert with month name

### **TO_CHAR** - Convert date to string
```
TO_CHAR(date, format)
```
**Examples:**
- `TO_CHAR(Order_Date, 'YYYY-MM-DD')` → '2024-01-15'
- `TO_CHAR(SYSDATE, 'Month DD, YYYY')` → 'January 15, 2024'
- `TO_CHAR(Hire_Date, 'Day')` → 'Monday'

### **ADD_TO_DATE** - Add to date
```
ADD_TO_DATE(date, format, value)
```
**Examples:**
- `ADD_TO_DATE(Order_Date, 'DD', 30)` → Add 30 days
- `ADD_TO_DATE(Start_Date, 'MM', 6)` → Add 6 months
- `ADD_TO_DATE(Date_Field, 'YYYY', 1)` → Add 1 year

### **DATE_DIFF** - Difference between dates
```
DATE_DIFF(date1, date2, format)
```
**Examples:**
- `DATE_DIFF(End_Date, Start_Date, 'DD')` → Days between
- `DATE_DIFF(SYSDATE, Birth_Date, 'YYYY')` → Age in years
- `DATE_DIFF(Due_Date, Payment_Date, 'DD')` → Days overdue

### **TRUNC (for dates)** - Truncate time portion
```
TRUNC(date, format)
```
**Examples:**
- `TRUNC(Order_DateTime)` → Remove time, keep only date
- `TRUNC(SYSDATE, 'MM')` → First day of current month
- `TRUNC(Date_Field, 'YYYY')` → First day of year

### **LAST_DAY** - Last day of month
```
LAST_DAY(date)
```
**Examples:**
- `LAST_DAY(Order_Date)` → Last day of order month
- `LAST_DAY(SYSDATE)` → Last day of current month

---

## 4. CONDITIONAL FUNCTIONS

### **IIF** - If-Then-Else
```
IIF(condition, value_if_true, value_if_false)
```
**Examples:**
- `IIF(Salary > 50000, 'High', 'Low')` → Salary category
- `IIF(ISNULL(Bonus), 0, Bonus)` → Replace NULL with 0
- `IIF(Status = 'A', 'Active', 'Inactive')` → Status description

### **DECODE** - Multiple condition check
```
DECODE(expression, value1, result1, value2, result2, ..., default)
```
**Examples:**
- `DECODE(Grade, 'A', 90, 'B', 80, 'C', 70, 0)` → Grade to marks
- `DECODE(Country, 'US', 'United States', 'UK', 'United Kingdom', Country)` → Country expansion
- `DECODE(Status, 1, 'Active', 2, 'Inactive', 3, 'Suspended', 'Unknown')` → Status mapping

### Nested IIF (Multiple conditions)
```
IIF(condition1, result1, IIF(condition2, result2, result3))
```
**Examples:**
- `IIF(Score >= 90, 'A', IIF(Score >= 80, 'B', IIF(Score >= 70, 'C', 'F')))` → Grade assignment
- `IIF(Age < 18, 'Minor', IIF(Age < 65, 'Adult', 'Senior'))` → Age group

---

## 5. NULL HANDLING FUNCTIONS

### **ISNULL** - Check if NULL
```
ISNULL(value)
```
**Examples:**
- `ISNULL(Middle_Name)` → Returns TRUE if NULL
- `IIF(ISNULL(Phone), 'No Phone', Phone)` → Handle NULL
- `IIF(ISNULL(Email), 'MISSING', 'PRESENT')` → Email presence check

### **IIF with NULL handling**
```
IIF(ISNULL(field), default_value, field)
```
**Examples:**
- `IIF(ISNULL(Discount), 0, Discount)` → Default to 0
- `IIF(ISNULL(Manager_ID), 'No Manager', Manager_ID)` → NULL replacement
- `Salary * IIF(ISNULL(Bonus_Pct), 0, Bonus_Pct)` → Handle NULL in calculation

---

## 6. CONVERSION FUNCTIONS

### **TO_INTEGER / TO_DECIMAL** - Convert to number
```
TO_INTEGER(string)
TO_DECIMAL(string, [precision], [scale])
```
**Examples:**
- `TO_INTEGER('123')` → 123
- `TO_DECIMAL('123.45', 10, 2)` → 123.45
- `TO_INTEGER(SUBSTR(Emp_ID, 4, 3))` → Extract and convert to number

### **TO_CHAR** - Convert to string
```
TO_CHAR(value)
```
**Examples:**
- `TO_CHAR(Employee_ID)` → Convert number to string
- `'EMP' || TO_CHAR(ID)` → Concatenate with number
- `TO_CHAR(Salary, '999,999.99')` → Format number

---

## 7. AGGREGATE FUNCTIONS (with Variables)

### Using Variable Ports for Running Totals
```
-- Variable port: v_RunningTotal
v_RunningTotal = v_RunningTotal + Amount

-- Output port: o_RunningTotal
o_RunningTotal = v_RunningTotal
```

### Running Count
```
-- Variable: v_Count
v_Count = v_Count + 1

-- Output: Row_Number
Row_Number = v_Count
```

---

## 8. PRACTICAL REAL-WORLD EXAMPLES

### **Example 1: Email Validation**
```
IIF(
    REG_MATCH(Email, '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'),
    'Valid',
    'Invalid'
)
```

### **Example 2: Phone Number Formatting**
```
'(' || SUBSTR(Phone, 1, 3) || ') ' || 
SUBSTR(Phone, 4, 3) || '-' || 
SUBSTR(Phone, 7, 4)
-- Result: (123) 456-7890
```

### **Example 3: Full Name Creation**
```
UPPER(SUBSTR(First_Name, 1, 1)) || 
LOWER(SUBSTR(First_Name, 2)) || ' ' ||
UPPER(SUBSTR(Last_Name, 1, 1)) || 
LOWER(SUBSTR(Last_Name, 2))
-- Result: John Smith
```

### **Example 4: Age Calculation**
```
TRUNC(DATE_DIFF(SYSDATE, Birth_Date, 'DD') / 365.25)
```

### **Example 5: Discount Calculation**
```
IIF(
    Total_Amount > 10000, Total_Amount * 0.15,
    IIF(Total_Amount > 5000, Total_Amount * 0.10,
    IIF(Total_Amount > 1000, Total_Amount * 0.05, 0))
)
```

### **Example 6: Generate Unique ID**
```
'CUS' || TO_CHAR(SYSDATE, 'YYYYMMDD') || LPAD(TO_CHAR(Sequence_ID), 6, '0')
-- Result: CUS202401150000123
```

### **Example 7: Extract Domain from Email**
```
SUBSTR(Email, INSTR(Email, '@') + 1)
-- john@gmail.com → gmail.com
```

### **Example 8: Flag Duplicate Records**
```
-- Variable: v_Prev_ID
v_Prev_ID = Customer_ID

-- Variable: v_Duplicate_Flag
v_Duplicate_Flag = IIF(v_Prev_ID = Customer_ID, 'Y', 'N')

-- Output: Duplicate_Flag
Duplicate_Flag = v_Duplicate_Flag
```

### **Example 9: Salary Range Categorization**
```
DECODE(
    TRUE,
    Salary < 30000, 'Entry Level',
    Salary < 60000, 'Mid Level',
    Salary < 100000, 'Senior Level',
    'Executive Level'
)
```

### **Example 10: Clean and Standardize Address**
```
UPPER(
    LTRIM(RTRIM(
        REPLACE(REPLACE(REPLACE(Address, '  ', ' '), 'St.', 'Street'), 'Ave.', 'Avenue')
    ))
)
```

---

## BEST PRACTICES

1. **Always handle NULL values** - Use ISNULL() or IIF() to avoid errors
2. **Use UPPER/LOWER for comparisons** - Makes matching case-insensitive
3. **Trim strings before comparison** - Remove unwanted spaces
4. **Use TO_CHAR for date formatting** - Ensures consistent date formats
5. **LPAD for ID generation** - Creates fixed-length IDs
6. **Use DECODE for multiple conditions** - Cleaner than nested IIF
7. **Test with sample data** - Verify expressions before deployment

This covers the most commonly used functions in Expression Transformation with practical, real-world scenarios!