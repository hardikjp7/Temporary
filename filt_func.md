Here's an **EXHAUSTIVE** guide to **ALL Informatica Expression Transformation Functions** with practical examples:

---

## 1. STRING FUNCTIONS

### **SUBSTR** - Extract substring
```
SUBSTR(string, start_position, length)
```
**Examples:**
- `SUBSTR('John Doe', 1, 4)` → 'John'
- `SUBSTR(Email, 1, INSTR(Email, '@') - 1)` → Extract username from email
- `SUBSTR(Phone, -4)` → Last 4 digits (negative indexing)

### **INSTR** - Find position of substring
```
INSTR(string, search_string, [start_position], [occurrence])
```
**Examples:**
- `INSTR('john@gmail.com', '@')` → 5
- `INSTR(Full_Name, ' ', 1, 2)` → Position of 2nd space
- `INSTR(Description, 'ERROR', 1, 1)` → First occurrence of ERROR

### **LENGTH** - Get string length
```
LENGTH(string)
```
**Examples:**
- `LENGTH('Hello')` → 5
- `IIF(LENGTH(SSN) != 9, 'Invalid', 'Valid')` → Validate SSN length
- `LENGTH(REPLACE(Text, ' ', ''))` → Length without spaces

### **LENGTHB** - Get byte length
```
LENGTHB(string)
```
**Examples:**
- `LENGTHB('Hello')` → Byte length (useful for multi-byte characters)
- `LENGTHB(Chinese_Name)` → Byte size for Chinese characters

### **UPPER / LOWER** - Change case
```
UPPER(string) / LOWER(string)
```
**Examples:**
- `UPPER('john')` → 'JOHN'
- `LOWER(Email)` → Standardize email to lowercase
- `UPPER(Country_Code)` → 'US', 'UK', 'IN'

### **INITCAP** - Capitalize first letter of each word
```
INITCAP(string)
```
**Examples:**
- `INITCAP('john doe')` → 'John Doe'
- `INITCAP(City_Name)` → 'New York', 'Los Angeles'
- `INITCAP(LOWER(Full_Name))` → Proper case names

### **LTRIM / RTRIM** - Remove leading/trailing characters
```
LTRIM(string, [trim_set])
RTRIM(string, [trim_set])
```
**Examples:**
- `LTRIM('  Hello')` → 'Hello'
- `RTRIM(Name)` → Remove trailing spaces
- `LTRIM(Phone, '0')` → Remove leading zeros
- `RTRIM(LTRIM(Address))` → Trim both sides

### **LPAD / RPAD** - Pad strings
```
LPAD(string, length, pad_string)
RPAD(string, length, pad_string)
```
**Examples:**
- `LPAD(Employee_ID, 6, '0')` → '000123'
- `RPAD(Name, 20, ' ')` → Pad to 20 characters
- `LPAD(TO_CHAR(Invoice_No), 10, '0')` → '0000045678'

### **CONCAT** - Concatenate (rarely used, || is preferred)
```
CONCAT(string1, string2)
```
**Examples:**
- `CONCAT(First_Name, Last_Name)` → 'JohnDoe'
- Use `||` instead: `First_Name || ' ' || Last_Name` → 'John Doe'

### **|| (Concatenation Operator)** - Join strings
```
string1 || string2 || string3
```
**Examples:**
- `First_Name || ' ' || Last_Name` → 'John Doe'
- `'EMP' || LPAD(TO_CHAR(ID), 5, '0')` → 'EMP00123'
- `Street || ', ' || City || ', ' || State || ' ' || Zip`

### **REPLACE** - Replace substring
```
REPLACE(string, old_string, [new_string])
```
**Examples:**
- `REPLACE(Phone, '-', '')` → Remove hyphens
- `REPLACE(SSN, '-', '')` → '123456789'
- `REPLACE(Text, 'NULL', '')` → Remove NULL text
- `REPLACE(Description, CHR(10), ' ')` → Replace newlines with space

### **REPLACESTR** - Replace multiple occurrences
```
REPLACESTR(CaseSensitive, InputString, OldString1, NewString1, OldString2, NewString2,...)
```
**Examples:**
- `REPLACESTR(0, Phone, '-', '', '(', '', ')', '')` → Remove all phone formatting
- `REPLACESTR(1, Status, 'A', 'Active', 'I', 'Inactive')` → Multiple replacements

### **REVERSE** - Reverse string
```
REVERSE(string)
```
**Examples:**
- `REVERSE('Hello')` → 'olleH'
- `REVERSE(Account_No)` → Reverse account number
- Useful for pattern matching from end of string

### **SOUNDEX** - Phonetic representation
```
SOUNDEX(string)
```
**Examples:**
- `SOUNDEX('Smith')` → 'S530'
- `SOUNDEX('Smythe')` → 'S530' (same sound)
- Useful for fuzzy name matching
- `IIF(SOUNDEX(Name1) = SOUNDEX(Name2), 'Match', 'No Match')`

### **METAPHONE** - Phonetic algorithm
```
METAPHONE(string, length)
```
**Examples:**
- `METAPHONE('Catherine', 10)` → 'K0RN'
- `METAPHONE('Kathryn', 10)` → 'K0RN' (same sound)
- Better than SOUNDEX for English names

### **ASCII** - Get ASCII code
```
ASCII(character)
```
**Examples:**
- `ASCII('A')` → 65
- `ASCII('a')` → 97
- `ASCII(SUBSTR(Name, 1, 1))` → First character code

### **CHR** - Get character from ASCII
```
CHR(ascii_code)
```
**Examples:**
- `CHR(65)` → 'A'
- `CHR(10)` → Line feed (newline)
- `CHR(13)` → Carriage return
- `REPLACE(Text, CHR(10), ' ')` → Replace newlines

### **IS_NUMBER** - Check if string is numeric
```
IS_NUMBER(string)
```
**Examples:**
- `IS_NUMBER('123')` → 1 (TRUE)
- `IS_NUMBER('12.34')` → 1 (TRUE)
- `IS_NUMBER('ABC')` → 0 (FALSE)
- `IIF(IS_NUMBER(Input_Value), TO_DECIMAL(Input_Value), 0)`

### **IS_SPACES** - Check if string contains only spaces
```
IS_SPACES(string)
```
**Examples:**
- `IS_SPACES('   ')` → 1 (TRUE)
- `IS_SPACES('Hello')` → 0 (FALSE)
- `IIF(IS_SPACES(Name), 'Empty', Name)` → Handle blank names

---

## 2. REGULAR EXPRESSION FUNCTIONS

### **REG_EXTRACT** - Extract using regex
```
REG_EXTRACT(subject, pattern, [position])
```
**Examples:**
- `REG_EXTRACT(Email, '([^@]+)@', 1)` → Extract username
- `REG_EXTRACT(Phone, '[0-9]{3}', 1)` → Extract area code
- `REG_EXTRACT(URL, 'https?://([^/]+)', 1)` → Extract domain
- `REG_EXTRACT(Text, '[A-Z]{2}[0-9]{6}', 0)` → Extract pattern like 'AB123456'

### **REG_MATCH** - Check pattern match
```
REG_MATCH(subject, pattern)
```
**Examples:**
- `REG_MATCH(Email, '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$')` → Validate email
- `REG_MATCH(Phone, '^[0-9]{10}$')` → Validate 10-digit phone
- `REG_MATCH(SSN, '^\d{3}-\d{2}-\d{4}$')` → Validate SSN format
- `REG_MATCH(Zip, '^[0-9]{5}(-[0-9]{4})?$')` → Validate US zip code

### **REG_REPLACE** - Replace using regex
```
REG_REPLACE(subject, pattern, replace_string, [flag])
```
**Examples:**
- `REG_REPLACE(Phone, '[^0-9]', '', 1)` → Keep only digits
- `REG_REPLACE(Text, '[^A-Za-z0-9 ]', '', 1)` → Remove special characters
- `REG_REPLACE(HTML, '<[^>]+>', '', 1)` → Remove HTML tags
- `REG_REPLACE(Email, '.*@', 'xxx@', 1)` → Mask email username

---

## 3. NUMERIC FUNCTIONS

### **ABS** - Absolute value
```
ABS(number)
```
**Examples:**
- `ABS(-50)` → 50
- `ABS(Actual - Budget)` → Variance (always positive)
- `ABS(Account_Balance)` → Absolute balance

### **CEIL** - Round up to nearest integer
```
CEIL(number)
```
**Examples:**
- `CEIL(4.3)` → 5
- `CEIL(4.9)` → 5
- `CEIL(Total_Items / 12)` → Number of dozens needed
- `CEIL(Pages / 100)` → Number of 100-page batches

### **FLOOR** - Round down to nearest integer
```
FLOOR(number)
```
**Examples:**
- `FLOOR(4.9)` → 4
- `FLOOR(4.1)` → 4
- `FLOOR(Age)` → Integer age
- `FLOOR(Salary / 1000) * 1000` → Round down to nearest thousand

### **ROUND** - Round to specified precision
```
ROUND(number, [precision])
```
**Examples:**
- `ROUND(123.456, 2)` → 123.46
- `ROUND(123.456, 0)` → 123
- `ROUND(123.456, -1)` → 120 (round to nearest 10)
- `ROUND(Salary * 1.15, 2)` → Apply 15% increase and round

### **TRUNC** - Truncate to specified precision
```
TRUNC(number, [precision])
```
**Examples:**
- `TRUNC(123.456, 2)` → 123.45
- `TRUNC(123.456, 0)` → 123
- `TRUNC(123.456, -1)` → 120 (truncate to nearest 10)
- `TRUNC(Price)` → Remove decimal part

### **POWER** - Exponentiation
```
POWER(base, exponent)
```
**Examples:**
- `POWER(2, 3)` → 8
- `POWER(1.05, Years)` → Compound growth factor
- `POWER(10, 6)` → 1000000
- `Principal * POWER(1 + Rate, Time)` → Compound interest

### **SQRT** - Square root
```
SQRT(number)
```
**Examples:**
- `SQRT(16)` → 4
- `SQRT(Area)` → Side of square
- `SQRT(POWER(X2 - X1, 2) + POWER(Y2 - Y1, 2))` → Distance formula

### **EXP** - Exponential (e^x)
```
EXP(exponent)
```
**Examples:**
- `EXP(1)` → 2.71828 (e)
- `EXP(2)` → 7.389
- Used in statistical calculations

### **LN** - Natural logarithm
```
LN(number)
```
**Examples:**
- `LN(10)` → 2.302585
- `LN(EXP(5))` → 5
- Used in growth rate calculations

### **LOG** - Logarithm base 10
```
LOG(number)
```
**Examples:**
- `LOG(100)` → 2
- `LOG(1000)` → 3
- `LOG(Sales)` → Log scale transformation

### **MOD** - Modulus (remainder)
```
MOD(dividend, divisor)
```
**Examples:**
- `MOD(10, 3)` → 1
- `IIF(MOD(Employee_ID, 2) = 0, 'Even', 'Odd')` → Check even/odd
- `MOD(Row_Count, 1000)` → Reset counter every 1000 rows
- `MOD(Day_Number, 7)` → Day of week (0-6)

### **SIGN** - Sign of number
```
SIGN(number)
```
**Examples:**
- `SIGN(10)` → 1
- `SIGN(-10)` → -1
- `SIGN(0)` → 0
- `SIGN(Profit)` → Determine profit/loss direction

### **COS / SIN / TAN** - Trigonometric functions
```
COS(angle_in_radians)
SIN(angle_in_radians)
TAN(angle_in_radians)
```
**Examples:**
- `COS(0)` → 1
- `SIN(3.14159/2)` → 1
- `TAN(0.785398)` → 1 (45 degrees)
- Used in geometric calculations

### **COSH / SINH / TANH** - Hyperbolic functions
```
COSH(number)
SINH(number)
TANH(number)
```
**Examples:**
- `COSH(0)` → 1
- `SINH(0)` → 0
- Used in advanced mathematical models

### **ACOS / ASIN / ATAN / ATAN2** - Inverse trigonometric
```
ACOS(number)
ASIN(number)
ATAN(number)
ATAN2(y, x)
```
**Examples:**
- `ACOS(1)` → 0
- `ASIN(0)` → 0
- `ATAN2(Y, X)` → Angle in radians
- Used in coordinate transformations

---

## 4. DATE FUNCTIONS

### **SYSDATE** - Current system date/time
```
SYSDATE
```
**Examples:**
- `SYSDATE` → Current timestamp
- `TRUNC(SYSDATE)` → Today's date (no time)
- `TO_CHAR(SYSDATE, 'YYYY-MM-DD HH24:MI:SS')` → Formatted current time

### **SYSTIMESTAMP** - Current timestamp with microseconds
```
SYSTIMESTAMP
```
**Examples:**
- `SYSTIMESTAMP` → High-precision timestamp
- Used for precise time logging

### **GET_DATE_PART** - Extract date component
```
GET_DATE_PART(date, format)
```
**Examples:**
- `GET_DATE_PART(Order_Date, 'YYYY')` → 2024 (year)
- `GET_DATE_PART(Order_Date, 'MM')` → 3 (month)
- `GET_DATE_PART(Order_Date, 'DD')` → 15 (day)
- `GET_DATE_PART(Order_Date, 'HH')` → Hour
- `GET_DATE_PART(Order_Date, 'MI')` → Minute
- `GET_DATE_PART(Order_Date, 'SS')` → Second
- `GET_DATE_PART(Order_Date, 'DW')` → Day of week (1-7)
- `GET_DATE_PART(Order_Date, 'WW')` → Week of year

### **SET_DATE_PART** - Set date component
```
SET_DATE_PART(date, format, value)
```
**Examples:**
- `SET_DATE_PART(Order_Date, 'YYYY', 2025)` → Change year to 2025
- `SET_DATE_PART(Date_Field, 'MM', 1)` → Set month to January
- `SET_DATE_PART(Date_Field, 'DD', 1)` → Set day to 1st
- `SET_DATE_PART(Timestamp, 'HH', 0)` → Set hour to midnight

### **TO_DATE** - Convert string to date
```
TO_DATE(string, [format])
```
**Examples:**
- `TO_DATE('2024-01-15', 'YYYY-MM-DD')` → Date value
- `TO_DATE(Date_String, 'MM/DD/YYYY')` → US format
- `TO_DATE('15-JAN-2024', 'DD-MON-YYYY')` → With month name
- `TO_DATE('20240115', 'YYYYMMDD')` → Without separators

### **TO_CHAR** - Convert date to string
```
TO_CHAR(date, [format])
```
**Examples:**
- `TO_CHAR(Order_Date, 'YYYY-MM-DD')` → '2024-01-15'
- `TO_CHAR(SYSDATE, 'Month DD, YYYY')` → 'January 15, 2024'
- `TO_CHAR(Hire_Date, 'Day')` → 'Monday'
- `TO_CHAR(Date_Field, 'HH24:MI:SS')` → '14:30:45'
- `TO_CHAR(Date_Field, 'Q')` → Quarter (1-4)

### **ADD_TO_DATE** - Add interval to date
```
ADD_TO_DATE(date, format, value)
```
**Examples:**
- `ADD_TO_DATE(Order_Date, 'DD', 30)` → Add 30 days
- `ADD_TO_DATE(Start_Date, 'MM', 6)` → Add 6 months
- `ADD_TO_DATE(Date_Field, 'YYYY', 1)` → Add 1 year
- `ADD_TO_DATE(Timestamp, 'HH', 24)` → Add 24 hours
- `ADD_TO_DATE(Date_Field, 'MI', 30)` → Add 30 minutes
- `ADD_TO_DATE(Date_Field, 'SS', 60)` → Add 60 seconds

### **DATE_DIFF** - Difference between dates
```
DATE_DIFF(date1, date2, format)
```
**Examples:**
- `DATE_DIFF(End_Date, Start_Date, 'DD')` → Days between
- `DATE_DIFF(SYSDATE, Birth_Date, 'YYYY')` → Age in years
- `DATE_DIFF(Due_Date, Payment_Date, 'DD')` → Days overdue
- `DATE_DIFF(End_Time, Start_Time, 'HH')` → Hours between
- `DATE_DIFF(Date2, Date1, 'MM')` → Months between
- `DATE_DIFF(Date2, Date1, 'SS')` → Seconds between

### **DATE_COMPARE** - Compare dates
```
DATE_COMPARE(date1, date2, format)
```
**Examples:**
- `DATE_COMPARE(Date1, Date2, 'DD')` → Returns -1, 0, or 1
- `IIF(DATE_COMPARE(Order_Date, Ship_Date, 'DD') < 0, 'Late', 'On Time')`

### **TRUNC (for dates)** - Truncate date to specified part
```
TRUNC(date, [format])
```
**Examples:**
- `TRUNC(Order_DateTime)` → Remove time, keep date only
- `TRUNC(SYSDATE, 'MM')` → First day of current month
- `TRUNC(Date_Field, 'YYYY')` → First day of year
- `TRUNC(Date_Field, 'Q')` → First day of quarter
- `TRUNC(Timestamp, 'HH')` → Top of the hour

### **LAST_DAY** - Last day of month
```
LAST_DAY(date)
```
**Examples:**
- `LAST_DAY(Order_Date)` → Last day of order month
- `LAST_DAY(SYSDATE)` → Last day of current month
- `LAST_DAY(TO_DATE('2024-02-15', 'YYYY-MM-DD'))` → '2024-02-29'

### **ROUND (for dates)** - Round date to specified part
```
ROUND(date, format)
```
**Examples:**
- `ROUND(SYSDATE, 'DD')` → Round to nearest day
- `ROUND(Date_Field, 'MM')` → Round to nearest month
- `ROUND(Date_Field, 'YYYY')` → Round to nearest year

### **MONTHS_BETWEEN** - Months between dates
```
MONTHS_BETWEEN(date1, date2)
```
**Examples:**
- `MONTHS_BETWEEN(End_Date, Start_Date)` → 6.5 months
- `TRUNC(MONTHS_BETWEEN(SYSDATE, Hire_Date))` → Tenure in months

### **IS_DATE** - Check if valid date string
```
IS_DATE(string, format)
```
**Examples:**
- `IS_DATE('2024-01-15', 'YYYY-MM-DD')` → 1 (TRUE)
- `IS_DATE('2024-02-30', 'YYYY-MM-DD')` → 0 (FALSE - invalid date)
- `IS_DATE('NotADate', 'YYYY-MM-DD')` → 0 (FALSE)

---

## 5. CONVERSION FUNCTIONS

### **TO_INTEGER** - Convert to integer
```
TO_INTEGER(value)
```
**Examples:**
- `TO_INTEGER('123')` → 123
- `TO_INTEGER('123.99')` → 123 (truncates decimal)
- `TO_INTEGER(Price)` → Convert decimal to integer
- `IIF(IS_NUMBER(Input), TO_INTEGER(Input), 0)` → Safe conversion

### **TO_DECIMAL** - Convert to decimal
```
TO_DECIMAL(value, [precision], [scale])
```
**Examples:**
- `TO_DECIMAL('123.45')` → 123.45
- `TO_DECIMAL('123.456', 10, 2)` → 123.46 (rounded)
- `TO_DECIMAL(String_Amount, 18, 2)` → Convert to currency format

### **TO_FLOAT** - Convert to float
```
TO_FLOAT(value)
```
**Examples:**
- `TO_FLOAT('123.456')` → 123.456
- `TO_FLOAT(Integer_Value)` → Convert integer to float
- Used for scientific calculations

### **TO_BIGINT** - Convert to big integer
```
TO_BIGINT(value)
```
**Examples:**
- `TO_BIGINT('9223372036854775807')` → Large integer
- Used for very large numbers

### **TO_CHAR (for numbers)** - Convert number to string
```
TO_CHAR(number, [format])
```
**Examples:**
- `TO_CHAR(Employee_ID)` → '123'
- `TO_CHAR(Salary, '999,999.99')` → '75,000.00'
- `TO_CHAR(Amount, '$999,999.99')` → '$1,234.56'
- `'EMP' || TO_CHAR(ID)` → 'EMP123'

### **CAST** - Generic type conversion
```
CAST(value AS datatype)
```
**Examples:**
- `CAST(String_Value AS INTEGER)`
- `CAST(Int_Value AS VARCHAR(20))`
- `CAST(Date_String AS DATE)`

---

## 6. NULL HANDLING FUNCTIONS

### **ISNULL** - Check if value is NULL
```
ISNULL(value)
```
**Examples:**
- `ISNULL(Middle_Name)` → 1 (TRUE) if NULL
- `IIF(ISNULL(Phone), 'No Phone', Phone)`
- `IIF(ISNULL(Email), 0, 1)` → Email present flag

### **IIF with NULL** - NULL replacement
```
IIF(ISNULL(field), default, field)
```
**Examples:**
- `IIF(ISNULL(Discount), 0, Discount)` → Default to 0
- `IIF(ISNULL(Manager_ID), 'No Manager', Manager_ID)`
- `Salary * IIF(ISNULL(Bonus_Pct), 0, Bonus_Pct)` → Handle NULL in calc

### **NULL (keyword)** - Return NULL value
```
NULL
```
**Examples:**
- `IIF(Status = 'Unknown', NULL, Status)` → Return NULL explicitly
- `IIF(Amount = 0, NULL, Amount)` → NULL for zero amounts

---

## 7. CONDITIONAL FUNCTIONS

### **IIF** - If-Then-Else (Simple)
```
IIF(condition, value_if_true, value_if_false)
```
**Examples:**
- `IIF(Salary > 50000, 'High', 'Low')` → Simple categorization
- `IIF(Status = 'A', 'Active', 'Inactive')` → Status mapping
- `IIF(Age >= 18, 'Adult', 'Minor')` → Age check

### **Nested IIF** - Multiple conditions
```
IIF(cond1, result1, IIF(cond2, result2, IIF(cond3, result3, default)))
```
**Examples:**
- `IIF(Score >= 90, 'A', IIF(Score >= 80, 'B', IIF(Score >= 70, 'C', 'F')))`
- `IIF(Amount > 10000, 'Platinum', IIF(Amount > 5000, 'Gold', IIF(Amount > 1000, 'Silver', 'Bronze')))`

### **DECODE** - Multiple value matching
```
DECODE(expression, value1, result1, value2, result2, ..., default)
```
**Examples:**
- `DECODE(Grade, 'A', 90, 'B', 80, 'C', 70, 'D', 60, 0)` → Grade to score
- `DECODE(Country_Code, 'US', 'United States', 'UK', 'United Kingdom', 'IN', 'India', Country_Code)`
- `DECODE(Status_Code, 1, 'Active', 2, 'Inactive', 3, 'Suspended', 'Unknown')`
- `DECODE(Month_No, 1, 'Jan', 2, 'Feb', 3, 'Mar', 4, 'Apr', 'Other')`

### **DECODE with TRUE** - Condition-based (like CASE)
```
DECODE(TRUE, condition1, result1, condition2, result2, ..., default)
```
**Examples:**
- `DECODE(TRUE, Salary < 30000, 'Low', Salary < 60000, 'Medium', 'High')`
- `DECODE(TRUE, Age < 18, 'Minor', Age < 65, 'Adult', 'Senior')`
- `DECODE(TRUE, Score >= 90, 'A', Score >= 80, 'B', Score >= 70, 'C', 'F')`

---

## 8. AGGREGATE/ANALYTICAL FUNCTIONS (Using Variable Ports)

### **Running Total**
```
-- Variable Port: v_Running_Total
v_Running_Total = v_Running_Total + Amount

-- Output Port: Running_Total
Running_Total = v_Running_Total
```

### **Running Count / Row Number**
```
-- Variable: v_Row_Count
v_Row_Count = v_Row_Count + 1

-- Output: Row_Number
Row_Number = v_Row_Count
```

### **Running Maximum**
```
-- Variable: v_Max_Value
v_Max_Value = IIF(Amount > v_Max_Value, Amount, v_Max_Value)

-- Output: Max_So_Far
Max_So_Far = v_Max_Value
```

### **Running Minimum**
```
-- Variable: v_Min_Value
v_Min_Value = IIF(ISNULL(v_Min_Value) OR Amount < v_Min_Value, Amount, v_Min_Value)

-- Output: Min_So_Far
Min_So_Far = v_Min_Value
```

### **Previous Row Value (LAG)**
```
-- Variable: v_Prev_Amount
v_Prev_Amount = Amount

-- Output: Previous_Amount
Previous_Amount = v_Prev_Amount
```

### **Change from Previous Row**
```
-- Variable: v_Prev_Value
v_Prev_Value = Current_Value

-- Output: Change
Change = Current_Value - v_Prev_Value
```

### **Group Change Detection**
```
-- Variable: v_Prev_Dept
v_Prev_Dept = Department

-- Output: Is_New_Dept
Is_New_Dept = IIF(v_Prev_Dept = Department, 'N', 'Y')
```

### **Running Average (Cumulative)**
```
-- Variable: v_Sum
v_Sum = v_Sum + Amount

-- Variable: v_Count
v_Count = v_Count + 1

-- Output: Running_Avg
Running_Avg = v_Sum / v_Count
```

---

## 9. SPECIAL FUNCTIONS

### **MD5** - Generate MD5 hash
```
MD5(string)
```
**Examples:**
- `MD5('password')` → MD5 hash
- `MD5(SSN)` → Hash sensitive data
- `MD5(Email || TO_CHAR(SYSDATE))` → Unique token generation

### **ENCRYPT / DECRYPT** - Data encryption (if configured)
```
ENCRYPT(string, key)
DECRYPT(string, key)
```
**Examples:**
- `ENCRYPT(SSN, 'MySecretKey')` → Encrypted SSN
- `DECRYPT(Encrypted_Field, 'MySecretKey')` → Decrypted value

### **GET_SESSION_VARIABLE** - Get session variable value
```
$PMSessionLogDir
$PMSourceFileDir
$PMTargetFileDir
```
**Examples:**
- `$PMSessionLogDir` → Session log directory
- Used for file paths in dynamic configurations

### **COMPRESS / DECOMPRESS** - Data compression
```
COMPRESS(string)
DECOMPRESS(string)
```
**Examples:**
- `COMPRESS(Large_Text)` → Compressed data
- `DECOMPRESS(Compressed_Data)` → Original data

### **UUID** - Generate unique identifier
```
UUID()
```
**Examples:**
- `UUID()` → 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11'
- Used for generating unique IDs

---

## 10. TEST/VALIDATION FUNCTIONS

### **IS_NUMBER** - Check if numeric
```
IS_NUMBER(string)
```
**Examples:**
- `IS_NUMBER('123')` → 1 (TRUE)
- `IS_NUMBER('12.34')` → 1 (TRUE)
- `IS_NUMBER('ABC')` → 0 (FALSE)

### **IS_DATE** - Check if valid date
```
IS_DATE(string, format)
```
**Examples:**
- `IS_DATE('2024-01-15', 'YYYY-MM-DD')` → 1
- `IS_DATE('2024-13-45', 'YYYY-MM-DD')` → 0

### **IS_SPACES** - Check if only spaces
```
IS_SPACES(string)
```
**Examples:**
- `IS_SPACES('   ')` → 1 (TRUE)
- `IS_SPACES('Hello')` → 0 (FALSE)

---

## 11. PRACTICAL REAL-WORLD COMPLEX EXAMPLES

### **Example 1: Email Masking**
```
SUBSTR(Email, 1, 2) || 
RPAD('*', LENGTH(Email) - INSTR(Email, '@') - 2, '*') || 
SUBSTR(Email, INSTR(Email, '@'))
-- john.doe@gmail.com → jo******@gmail.com
```

### **Example 2: Credit Card Masking**
```
RPAD('*', LENGTH(Card_No) - 4, '*') || SUBSTR(Card_No, -4)
-- 1234567890123456 → ************3456
```

### **Example 3: Phone Formatting**
```
IIF(LENGTH(REPLACE(Phone, '-', '')) = 10,
    '(' || SUBSTR(Phone, 1, 3) || ') ' || 
    SUBSTR(Phone, 4, 3) || '-' || 
    SUBSTR(Phone, 7, 4),
    Phone
)
-- 1234567890 → (123) 456-7890
```

### **Example 4: Age Group Calculation**
```
DECODE(TRUE,
    TRUNC(DATE_DIFF(SYSDATE, Birth_Date, 'DD') / 365.25) < 18, 'Minor',
    TRUNC(DATE_DIFF(SYSDATE, Birth_Date, 'DD') / 365.25) < 35, 'Young Adult',
    TRUNC(DATE_DIFF(SYSDATE, Birth_Date, 'DD') / 365.25) < 55, 'Middle Age',
    TRUNC(DATE_DIFF(SYSDATE, Birth_Date, 'DD') / 365.25) < 70, 'Senior',
    'Elderly'
)
```

### **Example 5: Generate Reference Number**
```
'REF' || 
TO_CHAR(SYSDATE, 'YYYYMMDD') || 
LPAD(TO_CHAR(Sequence_No), 6, '0') || 
SUBSTR(MD5(Customer_ID || TO_CHAR(SYSDATE)), 1, 4)
-- Result: REF202401150001239a8f
```

### **Example 6: Fiscal Year Calculation**
```
IIF(TO_INTEGER(TO_CHAR(Order_Date, 'MM')) >= 4,
    TO_CHAR(Order_Date, 'YYYY') || '-' || TO_CHAR(ADD_TO_DATE(Order_Date, 'YYYY', 1), 'YYYY'),
    TO_CHAR(ADD_TO_DATE(Order_Date, 'YYYY', -1), 'YYYY') || '-' || TO_CHAR(Order_Date, 'YYYY')
)
-- If order in June 2024 → FY 2024-2025
-- If order in Jan 2024 → FY 2023-2024
```

### **Example 7: Business Days Calculation**
```
DATE_DIFF(End_Date, Start_Date, 'DD') - 
(FLOOR(DATE_DIFF(End_Date, Start_Date, 'DD') / 7) * 2)
-- Approximate business days (excludes weekends)
```

### **Example 8: Salary Band Classification**
```
DECODE(TRUE,
    Salary < 30000, '1-Entry',
    Salary < 50000, '2-Junior',
    Salary < 80000, '3-Mid',
    Salary < 120000, '4-Senior',
    Salary < 200000, '5-Lead',
    '6-Executive'
) || ' (' || TO_CHAR(Salary, '$999,999') || ')'
-- Result: 3-Mid ($65,000)
```

### **Example 9: Data Quality Score**
```
(IIF(ISNULL(First_Name), 0, 1) +
 IIF(ISNULL(Last_Name), 0, 1) +
 IIF(ISNULL(Email) OR NOT REG_MATCH(Email, '^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}$'), 0, 1) +
 IIF(ISNULL(Phone) OR LENGTH(REPLACE(Phone, '-', '')) != 10, 0, 1) +
 IIF(ISNULL(Address), 0, 1)) * 20
-- Result: 0-100 score based on completeness
```

### **Example 10: Currency Conversion with Formatting**
```
TO_CHAR(
    ROUND(Amount * Exchange_Rate, 2),
    'L999,999,999.99'
) || ' ' || Target_Currency
-- Result: $1,234.56 USD
```

### **Example 11: Extract Initials**
```
UPPER(SUBSTR(First_Name, 1, 1)) || 
IIF(ISNULL(Middle_Name), '', UPPER(SUBSTR(Middle_Name, 1, 1))) || 
UPPER(SUBSTR(Last_Name, 1, 1))
-- John Michael Doe → JMD
```

### **Example 12: Time Since Event**
```
DECODE(TRUE,
    DATE_DIFF(SYSDATE, Event_Date, 'DD') < 1, 
        TO_CHAR(DATE_DIFF(SYSDATE, Event_Date, 'HH')) || ' hours ago',
    DATE_DIFF(SYSDATE, Event_Date, 'DD') < 7,
        TO_CHAR(DATE_DIFF(SYSDATE, Event_Date, 'DD')) || ' days ago',
    DATE_DIFF(SYSDATE, Event_Date, 'DD') < 30,
        TO_CHAR(FLOOR(DATE_DIFF(SYSDATE, Event_Date, 'DD') / 7)) || ' weeks ago',
    DATE_DIFF(SYSDATE, Event_Date, 'DD') < 365,
        TO_CHAR(FLOOR(DATE_DIFF(SYSDATE, Event_Date, 'DD') / 30)) || ' months ago',
    TO_CHAR(FLOOR(DATE_DIFF(SYSDATE, Event_Date, 'DD') / 365)) || ' years ago'
)
-- Result: "3 days ago", "2 weeks ago", etc.
```

---

## 12. BEST PRACTICES & TIPS

### **Performance Tips**
1. **Avoid nested functions** when simple logic works
2. **Use DECODE over nested IIF** for multiple conditions
3. **Pre-calculate** reusable expressions in variable ports
4. **Use TO_CHAR(date)** instead of multiple GET_DATE_PART calls
5. **Minimize string concatenation** in loops/large datasets

### **Data Quality Tips**
1. **Always handle NULLs** - Use ISNULL or IIF
2. **Validate before conversion** - Use IS_NUMBER, IS_DATE
3. **Trim strings** before comparison - LTRIM(RTRIM())
4. **Use UPPER/LOWER** for case-insensitive matching
5. **Validate formats** with REG_MATCH before processing

### **Debugging Tips**
1. **Use multiple output ports** to see intermediate results
2. **Add validation flags** to identify bad data
3. **Create audit columns** (Created_Date, Modified_Date)
4. **Use DECODE(TRUE, ...)** for complex conditional logic
5. **Test with edge cases** (NULL, empty, special characters)

### **Common Patterns**
```
-- NULL handling pattern
IIF(ISNULL(Field), Default_Value, Field)

-- Empty string check
IIF(IS_SPACES(Field) OR ISNULL(Field), 'EMPTY', Field)

-- Safe numeric conversion
IIF(IS_NUMBER(Field), TO_DECIMAL(Field), 0)

-- Safe date conversion
IIF(IS_DATE(Field, 'YYYY-MM-DD'), TO_DATE(Field, 'YYYY-MM-DD'), SYSDATE)

-- String cleaning
LTRIM(RTRIM(UPPER(REPLACE(Field, '  ', ' '))))
```

---

This is the **COMPLETE** collection of Informatica Expression Transformation functions with practical, real-world examples! 🎯