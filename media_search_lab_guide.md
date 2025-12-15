# Media Search & Recommendations Challenge Lab - Complete Solution

## Lab Overview
This guide provides complete solutions for building AI-powered media search and recommendation applications using Google Cloud's AI Applications (formerly Discovery Engine).

## Prerequisites
- Access to Google Cloud Console
- Basic understanding of BigQuery, SQL, and REST APIs
- Lab credentials from Qwiklabs

---

## Task 1: Prepare Movie Data and User Event Data

### Step 1: Create BigQuery Dataset
```bash
# In Cloud Shell or using gcloud CLI
bq mk --dataset --location=US ${GOOGLE_CLOUD_PROJECT}:cymbal_media
```

**Or via Console:**
1. Navigate to BigQuery in Google Cloud Console
2. Click your project name
3. Click "CREATE DATASET"
4. Dataset ID: `cymbal_media`
5. Location: `US (multiple regions in United States)`
6. Click "CREATE DATASET"

### Step 2: Create Movies Table
```bash
# Using bq command
bq load \
  --source_format=CSV \
  --autodetect \
  cymbal_media.movies \
  gs://${GOOGLE_CLOUD_PROJECT}/movies.csv
```

**Or via Console:**
1. In BigQuery, expand your project and `cymbal_media` dataset
2. Click "CREATE TABLE"
3. Source: Google Cloud Storage
4. Select file: `gs://[YOUR_PROJECT_ID]/movies.csv`
5. File format: CSV
6. Table name: `movies`
7. Schema: Auto detect
8. Click "CREATE TABLE"

**Verify:** Should show 86,537 rows

### Step 3: Create User Events Table
```bash
# Define schema in a file first
cat > user_events_schema.json << 'EOF'
[
  {"name": "userPseudoId", "type": "STRING", "mode": "REQUIRED"},
  {"name": "eventType", "type": "STRING", "mode": "REQUIRED"},
  {"name": "eventTime", "type": "STRING", "mode": "REQUIRED"},
  {
    "name": "documents",
    "type": "RECORD",
    "mode": "REPEATED",
    "fields": [
      {"name": "id", "type": "INTEGER", "mode": "NULLABLE"},
      {"name": "name", "type": "INTEGER", "mode": "NULLABLE"}
    ]
  }
]
EOF

# Load the table
bq load \
  --source_format=NEWLINE_DELIMITED_JSON \
  cymbal_media.user_events \
  gs://${GOOGLE_CLOUD_PROJECT}/user_events.json \
  user_events_schema.json
```

**Or via Console:**
1. Click "CREATE TABLE"
2. Source: Google Cloud Storage
3. Select file: `gs://[YOUR_PROJECT_ID]/user_events.json`
4. File format: JSONL (newline delimited JSON)
5. Table name: `user_events`
6. Schema: Edit as text and paste the schema above
7. Click "CREATE TABLE"

**Verify:** Should show 16,916,912 rows

### Step 4: Create BigQuery View
Run this SQL in BigQuery:

```sql
CREATE OR REPLACE VIEW
  cymbal_media.movies_view AS (
  WITH
    t AS (
    SELECT
      CAST(movieId AS string) AS id,
      title AS title,
      SPLIT(genres, "|") AS categories,
      homepage,
      IFNULL(homepage, CONCAT('https://www.google.com/search?q=', 
        REGEXP_REPLACE(LOWER(title), r'\s+', '+')) ) AS uri,
      "2023-01-01T00:00:00Z" AS available_time,
      EXTRACT(YEAR FROM release_date) AS production_year,
      runtime AS media_duration,
      "movie" AS media_type,
      poster_path as poster_uri
    FROM
      `cymbal_media.movies`)
  SELECT
    id,
    "default_schema" AS schemaId,
    NULL AS parentDocumentId,
    TO_JSON_STRING( 
      STRUCT( 
        title AS title,
        categories AS categories,
        uri AS uri,
        production_year AS production_year,
        available_time AS available_time,
        media_duration AS media_duration,
        poster_uri as poster_uri,
        media_type AS media_type 
      ) 
    ) AS jsonData
  FROM t
)
```

### Quiz Answers for Task 1:
**What is this view doing?**
- ✅ Building a JSON string that includes all the movie metadata
- ✅ Converting the categories column to an array of strings
- ✅ Changing column names to match the media application default schema
- ✅ Replacing null homepage values with a Google search URL

**What columns are being projected?**
- ✅ id, schemaId, parentDocumentId, jsonData

---

## Task 2: Create Media Search Application and Data Store

### Step 1: Enable Required APIs
```bash
gcloud services enable discoveryengine.googleapis.com
```

**Or via Console:**
1. Navigate to "APIs & Services" > "Library"
2. Search for "Discovery Engine API"
3. Click "ENABLE"

### Step 2: Create Media Search Application
1. Navigate to **AI Applications** (search for "Discovery Engine" or "AI Applications")
2. Click "CREATE APP"
3. Select "Search" as app type
4. Select "Generic" content type
5. App name: `media_search_app`
6. Company name: `Cymbal Shops` (optional)
7. Click "CONTINUE"

### Step 3: Create Data Store
1. On the "Create data store" page:
   - Data store name: `movie_data_store`
   - Data store type: Keep default (unstructured)
   - Industry: Media
2. Click "CREATE"

### Step 4: Import Document Data
1. In your data store, go to "DATA" tab
2. Click "IMPORT" > "BigQuery"
3. Configure import:
   - Project: Your current project
   - Dataset: `cymbal_media`
   - Table: `movies_view`
4. Click "IMPORT"
5. Wait for import to complete (several minutes)

### Step 5: Import User Events
1. In data store, go to "ACTIVITY" tab
2. Click "IMPORT EVENTS"
3. Select "BigQuery"
4. Configure:
   - Project: Your current project
   - Dataset: `cymbal_media`
   - Table: `user_events`
5. Click "IMPORT"

### Step 6: Test Search
1. Go to your app's "PREVIEW" section
2. Enter search query: "Interstellar"
3. Verify results appear

---

## Task 3: Update Application Configuration

### Step 1: Enable User Event Collection
1. Go to your app's "CONFIGURATIONS" page
2. Under "User event collection", ensure toggle is **ON**
3. Save changes

**Quiz Answer:** 
- ✅ Automatically records events whenever a user searches using this application

### Step 2: Enable Search-As-You-Type
1. In "CONFIGURATIONS" > "Search features"
2. Toggle on "Enable search-as-you-type"
3. Click "SAVE AND PUBLISH"
4. Test by typing slowly in preview pane

**Quiz Answer:**
- ✅ Shows results and dynamically filters as you type your query

### Step 3: Configure Data Display
1. In "CONFIGURATIONS" > "Display data"
2. Map fields:
   - **Title** → `title`
   - **Thumbnail** → `poster_uri`
   - **URL** → `uri`
   - **Text 1** → `categories`
3. Click "SAVE AND PUBLISH"

**Quiz Answer:**
- ✅ False (It doesn't limit data, it just controls how it's displayed)

---

## Task 4: Access Media Search Application Using API

### Step 1: Navigate to Integration Page
1. Go to your app > "INTEGRATIONS" > "API"
2. Find the sample CURL request

### Step 2: Construct CURL Request
```bash
# Replace PROJECT_NUMBER and APP_ID with your values
export PROJECT_NUMBER=$(gcloud projects describe ${GOOGLE_CLOUD_PROJECT} --format="value(projectNumber)")
export APP_ID="media_search_app"  # Your app's ID (check in console)

# Basic search for "miracle"
curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  "https://discoveryengine.googleapis.com/v1beta/projects/${PROJECT_NUMBER}/locations/global/collections/default_collection/engines/${APP_ID}/servingConfigs/default_search:search" \
  -d '{
    "query": "miracle"
  }'
```

### Step 3: Set Page Size to 3
```bash
curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  "https://discoveryengine.googleapis.com/v1beta/projects/${PROJECT_NUMBER}/locations/global/collections/default_collection/engines/${APP_ID}/servingConfigs/default_search:search" \
  -d '{
    "query": "miracle",
    "pageSize": 3
  }'
```

---

## Task 5: Create Media Recommendations Application

### Quiz Answers for Recommendation Types:
**Which types are based on all user activity?**
- ✅ Most Popular
- ✅ Others You May Like

**What does Conversion rate optimization do?**
- ✅ Optimizes for movies that are clicked on when recommended
- ✅ Maximizes the likelihood a user consumes recommended content up to a threshold

### Step 1: Create Recommendations Application
1. In AI Applications, click "CREATE APP"
2. Select "Recommendations"
3. Configure:
   - App name: `media_rec_app`
   - Recommendation type: **Others you may like**
   - Business objective: **Click-through rate (CTR)**
   - Data store: Select `movie_data_store`
4. Click "CREATE"

### Step 2: Check Data Quality
1. Go to app > "DATA QUALITY"
2. Review conditions

**Quiz Answers:**
- Documents requirement (≥100): ✅ True (You have 86,537)
- Event data conditions: ✅ False (Events need 12-24 hours to assimilate)

### Step 3: Check Training Settings
1. Go to "CONFIGURATIONS" > "Training"
2. Review schedule

**Quiz Answer:**
- ✅ Daily

### Step 4: Configure Serving - Media Progress Filter
1. Go to "CONFIGURATIONS" > "Serving"
2. Under "Media progress filter":
   - Enable the filter
   - Set minimum watch time: **30 seconds**
3. Save changes

### Step 5: Configure Diversification
1. In "Serving" settings
2. Under "Diversification":
   - Diversification type: **Rules based**
   - Level: **Low**
3. Click "SAVE"

**Quiz Answer:**
- ✅ Show results with different categories, with a maximum of 3 per category

### Step 6: Review Integration
1. Go to "INTEGRATIONS" > "API"
2. Select a document to see recommendation request

**Quiz Answer:**
- ✅ servingConfig

---

## Example Recommendation API Call

```bash
# Get recommendations based on viewing "Toy Story" (document ID: 1)
export PROJECT_NUMBER=$(gcloud projects describe ${GOOGLE_CLOUD_PROJECT} --format="value(projectNumber)")

curl -X POST \
  -H "Authorization: Bearer $(gcloud auth print-access-token)" \
  -H "Content-Type: application/json" \
  "https://discoveryengine.googleapis.com/v1beta/projects/${PROJECT_NUMBER}/locations/global/collections/default_collection/engines/media_rec_app/servingConfigs/default_serving_config:recommend" \
  -d '{
    "userEvent": {
      "eventType": "view-item",
      "userPseudoId": "user123",
      "documents": [{"id": "1"}]
    }
  }'
```

---

## Key Concepts Summary

### Media Search Application:
- **Purpose:** Find specific content based on queries
- **Features:** Search-as-you-type, user event tracking, customizable display
- **Use Case:** "Find movies about space exploration"

### Media Recommendations Application:
- **Purpose:** Suggest related content based on user behavior
- **Types:** 
  - Others You May Like (collaborative filtering)
  - Recommended For You (personalized)
  - More Like This (content-based)
  - Most Popular (popularity-based)
- **Business Objectives:** CTR, Watch-time, Conversion rate
- **Use Case:** "Users who watched Toy Story also enjoyed..."

### User Events:
- Critical for personalization and recommendations
- Types: view-item, media-play, media-progress
- Require 12-24 hours to fully assimilate for training

---

## Troubleshooting Tips

1. **Import Fails:** Check BigQuery table schemas match expected format
2. **No Search Results:** Verify documents imported successfully (check Activity page)
3. **Recommendation Model Not Training:** Events need time to assimilate (12-24 hours)
4. **API Errors:** Ensure Discovery Engine API is enabled and you're using correct project number
5. **Preview Not Working:** Clear browser cache, try incognito window

---

## Additional Resources

- [AI Applications Documentation](https://cloud.google.com/generative-ai-app-builder/docs)
- [Media Search Guide](https://cloud.google.com/generative-ai-app-builder/docs/create-engine-media)
- [Media Recommendations Guide](https://cloud.google.com/generative-ai-app-builder/docs/create-recommendations-media)
- [User Events Schema](https://cloud.google.com/generative-ai-app-builder/docs/user-event-schema)

---

## Completion Checklist

- ✅ BigQuery dataset and tables created
- ✅ Movies view created with proper transformations
- ✅ Media Search app created with data imported
- ✅ Search-as-you-type enabled
- ✅ Data display fields configured
- ✅ API tested with miracle query (page size 3)
- ✅ Media Recommendations app created
- ✅ Serving configurations set (progress filter, diversification)
- ✅ All quiz questions answered correctly

**Expected Score:** 80%+ to pass

Good luck with your lab!