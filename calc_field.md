Here's a **COMPREHENSIVE** guide to **ALL Tableau Calculated Field Functions** with practical examples:

---

## 1. STRING FUNCTIONS

### **LEFT** - Extract from left
```
LEFT(string, num_chars)
```
**Examples:**
- `LEFT([Product Name], 3)` → First 3 characters
- `LEFT([Phone], 3)` → Area code
- `LEFT([SKU], 2)` → Category code

### **RIGHT** - Extract from right
```
RIGHT(string, num_chars)
```
**Examples:**
- `RIGHT([Order ID], 4)` → Last 4 digits
- `RIGHT([Account Number], 4)` → Last 4 of account
- `RIGHT([Email], 10)` → Domain portion

### **MID** - Extract from middle
```
MID(string, start, [length])
```
**Examples:**
- `MID([SSN], 4, 2)` → Middle 2 digits
- `MID([Date String], 6, 2)` → Extract month
- `MID([Product Code], 3, 5)` → Extract middle portion

### **LEN** - String length
```
LEN(string)
```
**Examples:**
- `LEN([Description])` → Character count
- `IF LEN([Phone]) = 10 THEN "Valid" ELSE "Invalid" END`
- `LEN(TRIM([Name]))` → Length without spaces

### **TRIM** - Remove spaces from both ends
```
TRIM(string)
```
**Examples:**
- `TRIM([Customer Name])` → Remove leading/trailing spaces
- `LEN(TRIM([Address]))` → Clean length
- `TRIM([Email])` → Clean email

### **LTRIM** - Remove left spaces
```
LTRIM(string)
```
**Examples:**
- `LTRIM([Name])` → Remove leading spaces
- `LTRIM([Product ID])` → Clean leading whitespace

### **RTRIM** - Remove right spaces
```
RTRIM(string)
```
**Examples:**
- `RTRIM([Description])` → Remove trailing spaces
- `RTRIM([Address])` → Clean trailing whitespace

### **UPPER** - Convert to uppercase
```
UPPER(string)
```
**Examples:**
- `UPPER([Country])` → 'USA', 'UK', 'INDIA'
- `UPPER([State Code])` → Standardize state codes
- `UPPER(LEFT([Name], 1))` → First letter caps

### **LOWER** - Convert to lowercase
```
LOWER(string)
```
**Examples:**
- `LOWER([Email])` → Standardize emails
- `LOWER([Username])` → username format
- `LOWER([Product Name])` → lowercase names

### **PROPER** - Capitalize first letter of each word
```
PROPER(string)
```
**Examples:**
- `PROPER([Customer Name])` → 'John Doe'
- `PROPER([City])` → 'New York'
- `PROPER(LOWER([FULL NAME]))` → Proper case from all caps

### **CONTAINS** - Check if string contains substring
```
CONTAINS(string, substring)
```
**Examples:**
- `CONTAINS([Product Name], "iPhone")` → TRUE/FALSE
- `IF CONTAINS([Description], "urgent") THEN "Priority" END`
- `CONTAINS(LOWER([Email]), "@gmail.com")` → Check domain
- `SUM(IF CONTAINS([Category], "Electronics") THEN [Sales] END)` → Filtered sum

### **STARTSWITH** - Check if starts with
```
STARTSWITH(string, substring)
```
**Examples:**
- `STARTSWITH([Order ID], "ORD")` → TRUE/FALSE
- `IF STARTSWITH([Product Code], "IT") THEN "Tech" ELSE "Non-Tech" END`
- `STARTSWITH([Phone], "+1")` → US phone numbers

### **ENDSWITH** - Check if ends with
```
ENDSWITH(string, substring)
```
**Examples:**
- `ENDSWITH([Email], ".com")` → TRUE/FALSE
- `IF ENDSWITH([File Name], ".pdf") THEN "PDF" END`
- `ENDSWITH([Domain], ".edu")` → Educational domains

### **FIND** - Find position of substring
```
FIND(string, substring, [start])
```
**Examples:**
- `FIND([Email], "@")` → Position of @ symbol (returns 0 if not found)
- `FIND([Full Name], " ")` → Position of first space
- `MID([Email], 1, FIND([Email], "@")-1)` → Extract username
- `IF FIND([Description], "discontinued") > 0 THEN "Yes" END`

### **FINDNTH** - Find nth occurrence
```
FINDNTH(string, substring, occurrence)
```
**Examples:**
- `FINDNTH([Text], " ", 2)` → Position of 2nd space
- `FINDNTH([Path], "/", 3)` → Position of 3rd slash
- `MID([Name], FINDNTH([Name], " ", 1)+1)` → Extract last name

### **REPLACE** - Replace substring
```
REPLACE(string, substring, replacement)
```
**Examples:**
- `REPLACE([Phone], "-", "")` → Remove hyphens
- `REPLACE([SSN], "-", "")` → '123456789'
- `REPLACE([Description], "NULL", "N/A")` → Replace NULL text
- `REPLACE([URL], "http://", "https://")` → Update protocol

### **SUBSTITUTE** - Replace all occurrences
```
SUBSTITUTE(string, old_text, new_text)
```
**Examples:**
- `SUBSTITUTE([Text], " ", "_")` → Replace all spaces with underscores
- `SUBSTITUTE([Path], "\", "/")` → Convert Windows to Unix paths
- Similar to REPLACE but more explicit

### **SPLIT** - Split string by delimiter
```
SPLIT(string, delimiter, token_number)
```
**Examples:**
- `SPLIT([Full Name], " ", 1)` → First name
- `SPLIT([Full Name], " ", 2)` → Last name
- `SPLIT([Email], "@", 1)` → Username
- `SPLIT([Email], "@", 2)` → Domain
- `SPLIT([CSV Data], ",", 3)` → Third value in CSV
- `SPLIT([Date], "-", 1)` → Year from YYYY-MM-DD

### **SPACE** - Generate spaces
```
SPACE(number)
```
**Examples:**
- `[First Name] + SPACE(1) + [Last Name]` → Full name with space
- `SPACE(10)` → 10 spaces
- Used for formatting

### **CHAR** - Get character from ASCII code
```
CHAR(code)
```
**Examples:**
- `CHAR(65)` → 'A'
- `CHAR(10)` → Line break
- `[Line1] + CHAR(10) + [Line2]` → Multi-line text

### **ASCII** - Get ASCII code from character
```
ASCII(string)
```
**Examples:**
- `ASCII('A')` → 65
- `ASCII(LEFT([Name], 1))` → ASCII of first character
- Used for custom sorting

### **+ (Concatenation)** - Join strings
```
string1 + string2
```
**Examples:**
- `[First Name] + " " + [Last Name]` → 'John Doe'
- `"Order: " + [Order ID]` → 'Order: 12345'
- `[City] + ", " + [State]` → 'Boston, MA'
- `"$" + STR([Sales])` → '$1000'

### **ISDATE** - Check if valid date string
```
ISDATE(string)
```
**Examples:**
- `ISDATE("2024-01-15")` → TRUE
- `ISDATE("NotADate")` → FALSE
- `IF ISDATE([Date String]) THEN DATE([Date String]) END`

---

## 2. NUMBER FUNCTIONS

### **ABS** - Absolute value
```
ABS(number)
```
**Examples:**
- `ABS([Profit])` → Always positive
- `ABS([Actual] - [Budget])` → Variance magnitude
- `ABS([Temperature Change])` → Absolute change

### **ROUND** - Round to specified decimals
```
ROUND(number, [decimals])
```
**Examples:**
- `ROUND([Sales], 2)` → 1234.56
- `ROUND([Price])` → Round to integer
- `ROUND([Percentage], 1)` → One decimal place
- `ROUND([Sales]/1000, 1)` → Sales in thousands

### **CEILING** - Round up to integer
```
CEILING(number)
```
**Examples:**
- `CEILING([Units Needed]/12)` → Boxes needed (round up)
- `CEILING([Price])` → Next integer
- `CEILING([Days]/7)` → Weeks needed

### **FLOOR** - Round down to integer
```
FLOOR(number)
```
**Examples:**
- `FLOOR([Total Items]/12)` → Complete dozens
- `FLOOR([Age])` → Integer age
- `FLOOR([Revenue]/1000)` → Thousands of revenue

### **INT** - Integer part (truncate)
```
INT(number)
```
**Examples:**
- `INT([Decimal Value])` → Remove decimals
- `INT([Price])` → Dollar amount only
- `INT([Months]/12)` → Complete years

### **POWER** - Exponentiation
```
POWER(number, exponent)
```
**Examples:**
- `POWER(2, 3)` → 8
- `POWER(1.05, [Years])` → Compound growth
- `[Principal] * POWER(1 + [Rate], [Time])` → Compound interest

### **SQUARE** - Square of number
```
SQUARE(number)
```
**Examples:**
- `SQUARE(5)` → 25
- `SQUARE([Side Length])` → Area of square
- Used in statistical calculations

### **SQRT** - Square root
```
SQRT(number)
```
**Examples:**
- `SQRT(16)` → 4
- `SQRT([Area])` → Side of square
- `SQRT(SQUARE([X2]-[X1]) + SQUARE([Y2]-[Y1]))` → Distance

### **EXP** - Exponential (e^x)
```
EXP(number)
```
**Examples:**
- `EXP(1)` → 2.71828 (e)
- `EXP([Growth Rate])` → Exponential growth
- Used in predictive models

### **LOG** - Natural logarithm (base e)
```
LOG(number)
```
**Examples:**
- `LOG([Value])` → Natural log
- `LOG([Sales])` → Log transformation for analysis
- Used to normalize skewed data

### **LOG10** - Logarithm base 10
```
LOG10(number)
```
**Examples:**
- `LOG10(1000)` → 3
- `LOG10([Population])` → Log scale for large numbers

### **DIV** - Integer division
```
DIV(integer1, integer2)
```
**Examples:**
- `DIV([Total Items], 12)` → Complete dozens
- `DIV([Minutes], 60)` → Complete hours
- `DIV([Seconds], 3600)` → Complete hours from seconds

### **MOD** - Modulus (remainder)
```
number1 % number2
or
MOD(number, divisor)
```
**Examples:**
- `[Order ID] % 2` → Even/odd check (0 = even, 1 = odd)
- `IF [ID] % 2 = 0 THEN "Even" ELSE "Odd" END`
- `[Days] % 7` → Day of week offset
- `[Row Number] % 100` → Cycle 0-99

### **SIGN** - Sign of number
```
SIGN(number)
```
**Examples:**
- `SIGN([Profit])` → 1 (positive), -1 (negative), 0 (zero)
- `IF SIGN([Change]) = 1 THEN "Up" ELSE "Down" END`
- `SIGN([Balance])` → Account direction

### **ZN** - Replace NULL with zero
```
ZN(expression)
```
**Examples:**
- `ZN([Bonus])` → Convert NULL to 0
- `[Salary] * ZN([Bonus %])` → Handle NULL in calculation
- `ZN([Discount Amount])` → Default discount to 0
- **Most commonly used NULL handler in Tableau**

### **RANDOM** - Random number 0 to 1
```
RANDOM()
```
**Examples:**
- `RANDOM()` → Random decimal between 0 and 1
- `INT(RANDOM() * 100)` → Random integer 0-99
- `IF RANDOM() < 0.1 THEN "Sample" END` → 10% sample

### **HEXBINX / HEXBINY** - Hexagonal binning coordinates
```
HEXBINX(x, y, size)
HEXBINY(x, y, size)
```
**Examples:**
- `HEXBINX([Longitude], [Latitude], 0.5)` → Hex X coordinate
- `HEXBINY([Longitude], [Latitude], 0.5)` → Hex Y coordinate
- Used for spatial hex binning visualizations

---

## 3. DATE FUNCTIONS

### **TODAY** - Current date (no time)
```
TODAY()
```
**Examples:**
- `TODAY()` → Current date
- `DATEDIFF('day', [Order Date], TODAY())` → Days since order
- `IF [Due Date] < TODAY() THEN "Overdue" END`

### **NOW** - Current date and time
```
NOW()
```
**Examples:**
- `NOW()` → Current timestamp
- `DATEDIFF('minute', [Start Time], NOW())` → Minutes elapsed
- Used for timestamp logging

### **DATE** - Convert to date or create date
```
DATE(expression)
DATE(year, month, day)
```
**Examples:**
- `DATE([Date String])` → Convert string to date
- `DATE("2024-01-15")` → Create date
- `DATE(2024, 1, 15)` → Create date from parts
- `DATE(#2024-01-15#)` → Date literal

### **DATETIME** - Convert to datetime
```
DATETIME(expression)
```
**Examples:**
- `DATETIME([Timestamp String])` → Convert to datetime
- `DATETIME("2024-01-15 14:30:00")` → Create datetime
- Used for timestamp conversions

### **MAKEDATE** - Create date from parts
```
MAKEDATE(year, month, day)
```
**Examples:**
- `MAKEDATE(2024, 1, 15)` → January 15, 2024
- `MAKEDATE([Year], [Month], [Day])` → Construct date from fields
- `MAKEDATE(YEAR([Date]), 1, 1)` → First day of year

### **MAKETIME** - Create time from parts
```
MAKETIME(hour, minute, second)
```
**Examples:**
- `MAKETIME(14, 30, 0)` → 2:30:00 PM
- `MAKETIME([Hour], [Minute], [Second])` → Construct time

### **MAKEDATETIME** - Create datetime from parts
```
MAKEDATETIME(date, time)
MAKEDATETIME(year, month, day, hour, minute, second)
```
**Examples:**
- `MAKEDATETIME([Order Date], [Order Time])` → Combine date and time
- `MAKEDATETIME(2024, 1, 15, 14, 30, 0)` → Full datetime

### **DATEPARSE** - Parse date from string with format
```
DATEPARSE(format, string)
```
**Examples:**
- `DATEPARSE("MM/dd/yyyy", [Date String])` → Parse US date
- `DATEPARSE("dd-MMM-yyyy", "15-Jan-2024")` → Parse with month name
- `DATEPARSE("yyyy-MM-dd HH:mm:ss", [Timestamp])` → Parse datetime

### **DATEADD** - Add interval to date
```
DATEADD(date_part, interval, date)
```
**Examples:**
- `DATEADD('day', 7, [Order Date])` → Add 7 days
- `DATEADD('month', 6, [Start Date])` → Add 6 months
- `DATEADD('year', 1, [Hire Date])` → Add 1 year
- `DATEADD('hour', 24, NOW())` → 24 hours from now
- `DATEADD('quarter', -1, TODAY())` → Last quarter

**Date parts:** 'year', 'quarter', 'month', 'week', 'day', 'hour', 'minute', 'second'

### **DATEDIFF** - Difference between dates
```
DATEDIFF(date_part, start_date, end_date, [start_of_week])
```
**Examples:**
- `DATEDIFF('day', [Order Date], [Ship Date])` → Days to ship
- `DATEDIFF('month', [Hire Date], TODAY())` → Tenure in months
- `DATEDIFF('year', [Birth Date], TODAY())` → Age
- `DATEDIFF('hour', [Start Time], [End Time])` → Hours between
- `DATEDIFF('week', [Start], [End], 'monday')` → Weeks (Monday start)

### **DATENAME** - Get date part name
```
DATENAME(date_part, date, [start_of_week])
```
**Examples:**
- `DATENAME('month', [Order Date])` → 'January'
- `DATENAME('weekday', [Date])` → 'Monday'
- `DATENAME('year', [Date])` → '2024'
- `DATENAME('quarter', [Date])` → 'Q1'

### **DATEPART** - Get date part number
```
DATEPART(date_part, date, [start_of_week])
```
**Examples:**
- `DATEPART('year', [Order Date])` → 2024
- `DATEPART('month', [Date])` → 1-12
- `DATEPART('day', [Date])` → 1-31
- `DATEPART('weekday', [Date])` → 1-7
- `DATEPART('quarter', [Date])` → 1-4
- `DATEPART('week', [Date])` → 1-52

### **DATETRUNC** - Truncate date to specified part
```
DATETRUNC(date_part, date, [start_of_week])
```
**Examples:**
- `DATETRUNC('month', [Order Date])` → First day of month
- `DATETRUNC('year', [Date])` → January 1st of year
- `DATETRUNC('quarter', [Date])` → First day of quarter
- `DATETRUNC('week', [Date])` → Monday of week (default)
- `DATETRUNC('day', NOW())` → Today at midnight
- `DATETRUNC('hour', NOW())` → Current hour (00 minutes)

### **YEAR / QUARTER / MONTH / DAY** - Extract date parts
```
YEAR(date)
QUARTER(date)
MONTH(date)
DAY(date)
```
**Examples:**
- `YEAR([Order Date])` → 2024
- `QUARTER([Order Date])` → 1, 2, 3, or 4
- `MONTH([Order Date])` → 1-12
- `DAY([Order Date])` → 1-31

### **WEEK** - Week number
```
WEEK(date, [start_of_week])
```
**Examples:**
- `WEEK([Order Date])` → 1-52
- `WEEK([Date], 'monday')` → Week with Monday start

### **ISOQUARTER / ISOWEEK / ISOWEEKDAY / ISOYEAR** - ISO date parts
```
ISOQUARTER(date)
ISOWEEK(date)
ISOWEEKDAY(date)
ISOYEAR(date)
```
**Examples:**
- `ISOWEEK([Date])` → ISO week number
- `ISOWEEKDAY([Date])` → 1=Monday, 7=Sunday
- `ISOYEAR([Date])` → ISO year (can differ from calendar year)

---

## 4. LOGICAL FUNCTIONS

### **IF THEN ELSE** - Conditional logic
```
IF condition THEN value1
ELSEIF condition2 THEN value2
ELSE value3
END
```
**Examples:**
- `IF [Sales] > 10000 THEN "High" ELSE "Low" END`
- `IF [Score] >= 90 THEN "A" ELSEIF [Score] >= 80 THEN "B" ELSE "C" END`
- `IF [Status] = "Active" THEN [Sales] ELSE 0 END`

### **IIF** - Inline IF (simpler syntax)
```
IIF(test, then, else, [unknown])
```
**Examples:**
- `IIF([Sales] > 5000, "High", "Low")` → Quick IF
- `IIF([Quantity] > 0, [Sales]/[Quantity], 0)` → Avoid divide by zero
- `IIF(ISNULL([Bonus]), 0, [Bonus])` → NULL handling
- `IIF([Category] = "Tech", [Sales], 0)` → Conditional aggregation

### **CASE** - Multiple conditions
```
CASE expression
WHEN value1 THEN result1
WHEN value2 THEN result2
ELSE default
END
```
**Examples:**
- `CASE [Grade] WHEN "A" THEN 4.0 WHEN "B" THEN 3.0 WHEN "C" THEN 2.0 ELSE 0 END`
- `CASE [Region] WHEN "East" THEN "E" WHEN "West" THEN "W" ELSE "O" END`
- `CASE [Status Code] WHEN 1 THEN "Active" WHEN 2 THEN "Inactive" ELSE "Unknown" END`

### **CASE with conditions**
```
CASE
WHEN condition1 THEN result1
WHEN condition2 THEN result2
ELSE default
END
```
**Examples:**
- `CASE WHEN [Sales] < 1000 THEN "Low" WHEN [Sales] < 5000 THEN "Med" ELSE "High" END`
- `CASE WHEN [Profit] > 0 THEN "Profit" WHEN [Profit] < 0 THEN "Loss" ELSE "Break Even" END`

### **AND** - Logical AND
```
condition1 AND condition2
```
**Examples:**
- `IF [Sales] > 5000 AND [Quantity] > 100 THEN "Large Order" END`
- `[Category] = "Furniture" AND [Region] = "West"`
- `[Active] = TRUE AND [Balance] > 0`

### **OR** - Logical OR
```
condition1 OR condition2
```
**Examples:**
- `IF [Status] = "Pending" OR [Status] = "Processing" THEN "Active" END`
- `[Category] = "Tech" OR [Category] = "Electronics"`
- `[Overdue] = TRUE OR [Balance] > 10000`

### **NOT** - Logical NOT
```
NOT condition
```
**Examples:**
- `NOT [Shipped]` → Not shipped orders
- `NOT CONTAINS([Name], "Test")` → Exclude test records
- `IF NOT ISNULL([Email]) THEN "Has Email" END`

### **IN** - Value in list
```
value IN (value1, value2, ...)
```
**Examples:**
- `[Category] IN ("Electronics", "Computers", "Phones")`
- `[State] IN ("CA", "NY", "TX")`
- `IF [Status] IN ("Active", "Pending") THEN [Sales] END`

### **BETWEEN** - Value in range
```
value >= lower AND value <= upper
```
**Examples:**
- `[Age] >= 18 AND [Age] <= 65`
- `[Date] >= #2024-01-01# AND [Date] <= #2024-12-31#`
- `IF [Score] >= 70 AND [Score] <= 79 THEN "C" END`

---

## 5. AGGREGATE FUNCTIONS

### **SUM** - Total sum
```
SUM(expression)
```
**Examples:**
- `SUM([Sales])` → Total sales
- `SUM([Quantity] * [Price])` → Total revenue
- `SUM(IF [Region] = "East" THEN [Sales] END)` → Conditional sum

### **AVG** - Average
```
AVG(expression)
```
**Examples:**
- `AVG([Sales])` → Average sales
- `AVG([Score])` → Average score
- `AVG(IF [Status] = "Complete" THEN [Duration] END)` → Conditional avg

### **MIN / MAX** - Minimum / Maximum
```
MIN(expression)
MAX(expression)
```
**Examples:**
- `MIN([Order Date])` → Earliest order
- `MAX([Sales])` → Highest sales
- `MAX([Price]) - MIN([Price])` → Price range

### **COUNT** - Count records
```
COUNT(expression)
```
**Examples:**
- `COUNT([Order ID])` → Number of orders
- `COUNT([Customer ID])` → Count customers (includes duplicates)
- `COUNT(IF [Status] = "Active" THEN 1 END)` → Conditional count

### **COUNTD** - Count distinct
```
COUNTD(expression)
```
**Examples:**
- `COUNTD([Customer ID])` → Unique customers
- `COUNTD([Product])` → Number of unique products
- `COUNTD(IF [Sales] > 1000 THEN [Customer ID] END)` → High-value customers

### **MEDIAN** - Median value
```
MEDIAN(expression)
```
**Examples:**
- `MEDIAN([Sales])` → Middle value
- `MEDIAN([Age])` → Median age
- Less affected by outliers than AVG

### **PERCENTILE** - Percentile value
```
PERCENTILE(expression, percentile)
```
**Examples:**
- `PERCENTILE([Sales], 0.75)` → 75th percentile
- `PERCENTILE([Score], 0.5)` → Same as MEDIAN
- `PERCENTILE([Income], 0.95)` → 95th percentile

### **STDEV / STDEVP** - Standard deviation
```
STDEV(expression)    // Sample
STDEVP(expression)   // Population
```
**Examples:**
- `STDEV([Sales])` → Sales standard deviation
- `STDEVP([Test Scores])` → Population std dev
- Used for variability analysis

### **VAR / VARP** - Variance
```
VAR(expression)      // Sample
VARP(expression)     // Population
```
**Examples:**
- `VAR([Sales])` → Sales variance
- `VARP([Returns])` → Population variance
- `SQRT(VAR([Values]))` → Standard deviation

### **ATTR** - Attribute (single value or *)
```
ATTR(expression)
```
**Examples:**
- `ATTR([Customer Name])` → Customer name (if only one)
- Returns * if multiple values
- Used in LOD expressions

---

## 6. TABLE CALCULATION FUNCTIONS

### **RUNNING_SUM** - Running total
```
RUNNING_SUM(SUM([Sales]))
```
**Examples:**
- `RUNNING_SUM(SUM([Sales]))` → Cumulative sales
- `RUNNING_SUM(SUM([Profit]))` → Year-to-date profit
- Shows accumulation over time

### **RUNNING_AVG** - Running average
```
RUNNING_AVG(SUM([Sales]))
```
**Examples:**
- `RUNNING_AVG(AVG([Price]))` → Moving average
- `RUNNING_AVG(SUM([Orders]))` → Cumulative avg orders

### **RUNNING_MIN / RUNNING_MAX** - Running min/max
```
RUNNING_MIN(MIN([Price]))
RUNNING_MAX(MAX([Sales]))
```
**Examples:**
- `RUNNING_MIN(MIN([Price]))` → Lowest price so far
- `RUNNING_MAX(MAX([Sales]))` → Peak sales to date

### **RUNNING_COUNT** - Running count
```
RUNNING_COUNT(COUNT([Orders]))
```
**Examples:**
- `RUNNING_COUNT(COUNTD([Customer]))` → Cumulative unique customers

### **WINDOW_SUM** - Sum over window
```
WINDOW_SUM(SUM([Sales]), [start], [end])
```
**Examples:**
- `WINDOW_SUM(SUM([Sales]), -2, 0)` → 3-period moving sum (current + 2 previous)
- `WINDOW_SUM(SUM([Sales]), 0, 2)` → Current + 2 forward
- `WINDOW_SUM(SUM([Sales]))` → Total of entire partition

### **WINDOW_AVG** - Average over window
```
WINDOW_AVG(AVG([Sales]), [start], [end])
```
**Examples:**
- `WINDOW_AVG(SUM([Sales]), -6, 0)` → 7-day moving average
- `WINDOW_AVG(AVG([Price]), -2, 2)` → 5-period centered average

### **WINDOW_MIN / WINDOW_MAX** - Min/Max over window
```
WINDOW_MIN(MIN([Price]), [start], [end])
WINDOW_MAX(MAX([Sales]), [start], [end])
```
**Examples:**
- `WINDOW_MIN(SUM([Sales]), 0, 0)` → Current value
- `WINDOW_MAX(SUM([Sales]))` → Maximum in partition

### **WINDOW_COUNT** - Count over window
```
WINDOW_COUNT(COUNT([Orders]), [start], [end])
```
**Examples:**
- `WINDOW_COUNT(COUNTD([Customer]), -3, 0)` → 4-period rolling count

### **WINDOW_MEDIAN / WINDOW_PERCENTILE** - Statistical window functions
```
WINDOW_MEDIAN(MEDIAN([Sales]), [start], [end])
WINDOW_PERCENTILE(PERCENTILE([Sales], 0.75), [start], [end])
```
**Examples:**
- `WINDOW_MEDIAN(SUM([Sales]), -2, 2)` → 5-period median

### **FIRST** - First value in partition
```
FIRST()
```
**Examples:**
- `IF FIRST() = 0 THEN [Sales] END` → First row only
- `LOOKUP(SUM([Sales]), FIRST())` → Value from first row

### **LAST** - Last value in partition
```
LAST()
```
**Examples:**
- `IF LAST() = 0 THEN [Sales] END` → Last row only
- `LOOKUP(SUM([Sales]), LAST())` → Value from last row

### **INDEX** - Current row index
```
INDEX()
```
**Examples:**
- `INDEX()` → 1, 2, 3, ... (row number in partition)
- `IF INDEX() <= 10 THEN [Sales] END` → Top 10 rows
- `IF INDEX() % 2 = 0 THEN "Even" ELSE "Odd" END`

### **SIZE** - Number of rows in partition
```
SIZE()
```
**Examples:**
- `SIZE()` → Total rows in partition
- `INDEX() / SIZE()` → Percent through partition
- `IF INDEX() = SIZE() THEN "Last" END`

### **TOTAL** - Total of expression
```
TOTAL(SUM([Sales]))
```
**Examples:**
- `SUM([Sales]) / TOTAL(SUM([Sales]))` → Percent of total
- `TOTAL(COUNTD([Customer]))` → Total unique customers

### **RANK** - Rank within partition
```
RANK(SUM([Sales]), 'asc'|'desc')
```
**Examples:**
- `RANK(SUM([Sales]), 'desc')` → Sales rank (1 = highest)
- `IF RANK(SUM([Sales])) <= 5 THEN [Product] END` → Top 5 products
- **Gaps** for ties (1, 2, 2, 4...)

### **RANK_DENSE** - Dense rank (no gaps)
```
RANK_DENSE(SUM([Sales]), 'asc'|'desc')
```
**Examples:**
- `RANK_DENSE(SUM([Sales]), 'desc')` → 1, 2, 2, 3... (no gaps)
- Better for top N when ties exist

### **RANK_MODIFIED** - Modified competition rank
```
RANK_MODIFIED(SUM([Sales]), 'asc'|'desc')
```
**Examples:**
- `RANK_MODIFIED(SUM([Sales]))` → 1, 3, 3, 4... (Olympic ranking)

### **RANK_PERCENTILE** - Percentile rank
```
RANK_PERCENTILE(SUM([Sales]), 'asc'|'desc')
```
**Examples:**
- `RANK_PERCENTILE(SUM([Sales]))` → 0 to 1 (percentile rank)
- `RANK_PERCENTILE(SUM([Sales])) * 100` → Percentile (0-100)

### **RANK_UNIQUE** - Unique rank (arbitrary tie-break)
```
RANK_UNIQUE(SUM([Sales]), 'asc'|'desc')
```
**Examples:**
- `RANK_UNIQUE(SUM([Sales]))` → Always unique ranks

### **PREVIOUS_VALUE** - Previous calculation value
```
PREVIOUS_VALUE(default) + current_value
```
**Examples:**
- `PREVIOUS_VALUE(0) + SUM([Sales])` → Running sum manually
- `PREVIOUS_VALUE(100) * (1 + [Growth Rate])` → Compound growth

### **LOOKUP** - Look up value at offset
```
LOOKUP(expression, [offset])
```
**Examples:**
- `LOOKUP(SUM([Sales]), -1)` → Previous row sales
- `LOOKUP(SUM([Sales]), 1)` → Next row sales
- `SUM([Sales]) - LOOKUP(SUM([Sales]), -1)` → Change from previous
- `(SUM([Sales]) - LOOKUP(SUM([Sales]), -1)) / LOOKUP(SUM([Sales]), -1)` → % change

### **MODEL_PERCENTILE** - Percentile of current row
```
MODEL_PERCENTILE(SUM([Sales]))
```
**Examples:**
- `MODEL_PERCENTILE(SUM([Profit]))` → Where this row falls (0-1)

### **MODEL_QUANTILE** - Quantile of current row
```
MODEL_QUANTILE(quantile_number, SUM([Sales]))
```
**Examples:**
- `MODEL_QUANTILE(4, SUM([Sales]))` → Quartile (1-4)
- `MODEL_QUANTILE(10, SUM([Sales]))` → Decile (1-10)

---

## 7. LEVEL OF DETAIL (LOD) EXPRESSIONS

### **FIXED** - Fixed level aggregation
```
{ FIXED [Dimension] : AGG(expression) }
```
**Examples:**
- `{ FIXED [Customer] : SUM([Sales]) }` → Total sales per customer
- `{ FIXED : SUM([Sales]) }` → Grand total (ignore all dimensions)
- `{ FIXED [Region], [Category] : AVG([Profit]) }` → Avg profit by region & category
- Compare individual to fixed aggregate

### **INCLUDE** - Include additional dimensions
```
{ INCLUDE [Dimension] : AGG(expression) }
```
**Examples:**
- `{ INCLUDE [Product] : SUM([Sales]) }` → Add product to current view level
- Adds dimensions to the view's level of detail

### **EXCLUDE** - Exclude dimensions
```
{ EXCLUDE [Dimension] : AGG(expression) }
```
**Examples:**
- `{ EXCLUDE [Month] : AVG([Sales]) }` → Average excluding month
- `{ EXCLUDE [Product] : SUM([Sales]) }` → Category total (remove product detail)

### **LOD Practical Examples:**

**Customer Lifetime Value:**
```
{ FIXED [Customer ID] : SUM([Sales]) }
```

**Percent of Customer Total:**
```
SUM([Sales]) / { FIXED [Customer] : SUM([Sales]) }
```

**New vs Repeat Customers:**
```
IF [Order Date] = { FIXED [Customer] : MIN([Order Date]) }
THEN "New" ELSE "Repeat" END
```

**Cohort Analysis:**
```
DATEDIFF('month', 
    { FIXED [Customer] : MIN([Order Date]) },
    [Order Date]
)
```

**Top Products per Category:**
```
IF RANK(SUM([Sales])) <= 5
AND SUM([Sales]) / { FIXED [Category] : SUM([Sales]) } > 0.05
THEN [Product] END
```

---

## 8. NULL HANDLING FUNCTIONS

### **ISNULL** - Check if NULL
```
ISNULL(expression)
```
**Examples:**
- `ISNULL([Middle Name])` → TRUE/FALSE
- `IF ISNULL([Email]) THEN "No Email" ELSE [Email] END`
- `SUM(IF NOT ISNULL([Bonus]) THEN [Bonus] END)`

### **ZN** - Zero if NULL (most common)
```
ZN(expression)
```
**Examples:**
- `ZN([Bonus])` → Convert NULL to 0
- `[Salary] * ZN([Bonus %])` → Multiply with NULL protection
- `ZN([Discount])` → Default to 0
- **Use this for most NULL handling in calculations**

### **IFNULL** - Replace NULL with value
```
IFNULL(expression, replacement)
```
**Examples:**
- `IFNULL([Middle Name], "")` → Empty string if NULL
- `IFNULL([Discount], 0)` → Default to 0
- `IFNULL([Manager], "No Manager")` → Text replacement

### **COALESCE** - First non-NULL value
```
COALESCE(expression1, expression2, ...)
```
**Examples:**
- `COALESCE([Phone Mobile], [Phone Work], [Phone Home], "No Phone")`
- `COALESCE([Email], [Backup Email], "No Email")`
- Returns first non-NULL from list

---

## 9. TYPE CONVERSION FUNCTIONS

### **STR** - Convert to string
```
STR(expression)
```
**Examples:**
- `STR([Order ID])` → Convert number to string
- `"Order: " + STR([Order Number])`
- `STR([Sales])` → Number as string

### **INT** - Convert to integer
```
INT(expression)
```
**Examples:**
- `INT("123")` → 123
- `INT([Decimal Value])` → Truncate to integer
- `INT([Sales])` → Remove decimals

### **FLOAT** - Convert to float
```
FLOAT(expression)
```
**Examples:**
- `FLOAT("123.45")` → 123.45
- `FLOAT([String Value])` → Convert to decimal

### **DATE / DATETIME** - Convert to date/datetime
```
DATE(expression)
DATETIME(expression)
```
**Examples:**
- `DATE("2024-01-15")` → Convert string to date
- `DATETIME([Timestamp String])` → Convert to datetime

---

## 10. USER FUNCTIONS

### **USERNAME** - Current Tableau username
```
USERNAME()
```
**Examples:**
- `IF USERNAME() = "admin" THEN [Sensitive Data] ELSE "Hidden" END`
- `[User] = USERNAME()` → Filter to user's own data
- Row-level security

### **FULLNAME** - Current user's full name
```
FULLNAME()
```
**Examples:**
- `"Report generated by: " + FULLNAME()`
- Used in custom welcome messages

### **ISFULLNAME** - Check if full name matches
```
ISFULLNAME("Name")
```
**Examples:**
- `ISFULLNAME("John Doe")` → TRUE/FALSE
- User-specific filtering

### **ISUSERNAME** - Check if username matches
```
ISUSERNAME("username")
```
**Examples:**
- `ISUSERNAME("jdoe")` → TRUE/FALSE
- Security filters

### **USERDOMAIN** - User's domain
```
USERDOMAIN()
```
**Examples:**
- `USERDOMAIN()` → Returns user's network domain
- Multi-tenant scenarios

---

## 11. SPATIAL FUNCTIONS

### **DISTANCE** - Distance between two points
```
DISTANCE([Lat1], [Lon1], [Lat2], [Lon2], 'km'|'miles')
```
**Examples:**
- `DISTANCE([Store Lat], [Store Lon], [Customer Lat], [Customer Lon], 'miles')`
- Calculate proximity

### **MAKELINE** - Create line between points
```
MAKELINE(MAKEPOINT([Lat1], [Lon1]), MAKEPOINT([Lat2], [Lon2]))
```
**Examples:**
- `MAKELINE(MAKEPOINT([Origin Lat], [Origin Lon]), MAKEPOINT([Dest Lat], [Dest Lon]))`
- Connect geographic points

### **MAKEPOINT** - Create spatial point
```
MAKEPOINT([Latitude], [Longitude])
```
**Examples:**
- `MAKEPOINT([Store Latitude], [Store Longitude])`
- Plot locations on map

### **AREA** - Calculate area of polygon
```
AREA([Spatial Polygon], 'km'|'miles')
```
**Examples:**
- `AREA([Territory Boundary], 'miles')` → Territory size

### **BUFFER** - Create buffer around geometry
```
BUFFER([Spatial Object], distance, 'km'|'miles')
```
**Examples:**
- `BUFFER(MAKEPOINT([Lat], [Lon]), 5, 'miles')` → 5-mile radius

---

## 12. PRACTICAL REAL-WORLD EXAMPLES

### **Example 1: YoY Growth %**
```
(SUM([Sales]) - LOOKUP(SUM([Sales]), -1)) / ABS(LOOKUP(SUM([Sales]), -1))
```

### **Example 2: Percent of Total**
```
SUM([Sales]) / TOTAL(SUM([Sales]))
```

### **Example 3: Moving Average (7-day)**
```
WINDOW_AVG(SUM([Sales]), -6, 0)
```

### **Example 4: Customer Segmentation (RFM)**
```
// Recency Score
CASE
WHEN DATEDIFF('day', { FIXED [Customer] : MAX([Order Date]) }, TODAY()) <= 30 THEN 5
WHEN DATEDIFF('day', { FIXED [Customer] : MAX([Order Date]) }, TODAY()) <= 90 THEN 4
WHEN DATEDIFF('day', { FIXED [Customer] : MAX([Order Date]) }, TODAY()) <= 180 THEN 3
WHEN DATEDIFF('day', { FIXED [Customer] : MAX([Order Date]) }, TODAY()) <= 365 THEN 2
ELSE 1
END
```

### **Example 5: Top N with Others**
```
IF RANK(SUM([Sales])) <= 10 THEN [Product]
ELSE "Other"
END
```

### **Example 6: Same Period Last Year**
```
LOOKUP(SUM([Sales]), -12)  // Assuming monthly data
```

### **Example 7: Days in Stock**
```
DATEDIFF('day', [Receipt Date], IFNULL([Sold Date], TODAY()))
```

### **Example 8: Email Validation**
```
IF CONTAINS([Email], "@") AND CONTAINS([Email], ".") 
AND LEN([Email]) > 5
THEN "Valid" ELSE "Invalid" END
```

### **Example 9: Age Groups**
```
CASE
WHEN DATEDIFF('year', [Birth Date], TODAY()) < 18 THEN "Under 18"
WHEN DATEDIFF('year', [Birth Date], TODAY()) < 35 THEN "18-34"
WHEN DATEDIFF('year', [Birth Date], TODAY()) < 50 THEN "35-49"
WHEN DATEDIFF('year', [Birth Date], TODAY()) < 65 THEN "50-64"
ELSE "65+"
END
```

### **Example 10: Profit Margin Category**
```
CASE
WHEN SUM([Profit])/SUM([Sales]) >= 0.20 THEN "Excellent (20%+)"
WHEN SUM([Profit])/SUM([Sales]) >= 0.10 THEN "Good (10-20%)"
WHEN SUM([Profit])/SUM([Sales]) >= 0 THEN "Low (0-10%)"
ELSE "Loss"
END
```

### **Example 11: Quarter over Quarter Growth**
```
(SUM([Sales]) - LOOKUP(SUM([Sales]), -1)) / ABS(LOOKUP(SUM([Sales]), -1))
// Use with DATETRUNC('quarter', [Date]) in view
```

### **Example 12: Cohort Retention**
```
COUNTD(IF [Order Date] >= DATEADD('month', [Months Since First], { FIXED [Customer] : MIN([Order Date]) })
AND [Order Date] < DATEADD('month', [Months Since First]+1, { FIXED [Customer] : MIN([Order Date]) })
THEN [Customer] END)
/
{ FIXED [Cohort Month] : COUNTD([Customer]) }
```

### **Example 13: Dynamic Date Filter**
```
CASE [Parameter]
WHEN "Last 7 Days" THEN [Date] >= TODAY()-7
WHEN "Last 30 Days" THEN [Date] >= TODAY()-30
WHEN "Last Quarter" THEN [Date] >= DATETRUNC('quarter', DATEADD('quarter', -1, TODAY()))
WHEN "YTD" THEN YEAR([Date]) = YEAR(TODAY())
END
```

### **Example 14: Running Total Reset by Group**
```
IF FIRST() = 0 OR [Category] != LOOKUP([Category], -1)
THEN SUM([Sales])
ELSE PREVIOUS_VALUE(0) + SUM([Sales])
END
```

### **Example 15: Anomaly Detection (Simple)**
```
IF ABS(SUM([Sales]) - WINDOW_AVG(SUM([Sales]), -6, 0)) > 
2 * WINDOW_STDEV(SUM([Sales]), -6, 0)
THEN "Anomaly" ELSE "Normal" END
```

---

## 13. BEST PRACTICES

### **Performance Tips:**
1. **Use FIXED LOD** for reusable calculations
2. **Avoid nested LODs** when possible
3. **Use ZN()** instead of IF ISNULL checks
4. **Pre-aggregate** in data source when possible
5. **Use ATTR()** for single-value dimensions in aggregations

### **Common Patterns:**
```
// Safe division
ZN(SUM([Profit]) / SUM([Sales]))

// Conditional aggregation
SUM(IF [Condition] THEN [Value] END)

// Rank filtering
IF RANK(SUM([Sales])) <= 10 THEN [Product] END

// Percent change
(Current - Previous) / ABS(Previous)

// NULL-safe concatenation
IFNULL([First], "") + " " + IFNULL([Last], "")
```

### **Debugging Tips:**
1. **Build incrementally** - test each part
2. **Use tooltips** to display intermediate values
3. **Create separate calc fields** for complex logic steps
4. **Check NULL handling** at each step
5. **Verify aggregation level** with LOD expressions

---

This is the **COMPLETE** collection of Tableau calculated field functions with practical examples! 🎯