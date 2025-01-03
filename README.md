# Transcript Summarizer API Documentation

This API provides functionalities for uploading, listing, and summarizing PDF transcripts of earnings calls for companies. The service allows you to extract text from PDF files and generate summaries of these transcripts by using a summarization model.

## Table of Contents

1. [Overview](#overview)
2. [Base URL](#base-url)
3. [Endpoints](#endpoints)
    - [GET /list_pdfs](#get-list_pdfs)
    - [POST /earnings_transcript_summary](#post-earnings_transcript_summary)
    - [GET /earnings_transcript_summary](#get-earnings_transcript_summary)
4. [Sample Requests](#sample-requests)
5. [Error Handling](#error-handling)
6. [Requirements](#requirements)
7. [Installation](#installation)
8. [Run the App](#run-the-app)

## Overview

The Transcript Summarizer API helps you:

- **List Available PDF Files**: Query the available PDF files that contain earnings call transcripts for various companies.
- **Summarize Earnings Transcripts**: Input a company name and retrieve a summarized version of the corresponding earnings transcript.

## Base URL

All the API endpoints listed below are relative to the following base URL:

http://<host>:<port>/
Example: `http://127.0.0.1:5000/`

## Endpoints

### GET /list_pdfs

**Description**:  
This endpoint lists all available PDF files in the `documents` directory.

**Request**:
```bash
curl -X GET http://127.0.0.1:5000/list_pdfs

**Response:**
{
  "Message": "Here are the list of available PDFs.",
  "pdf_files": [
    "file_name1": "file_path1",
    "file_name2": "file_path2"
  ]
}

### POST /earnings_transcript_summary
Description:
This endpoint accepts a JSON request body with the company_name and returns the summary of the earnings transcript.

Request:

bash
Copy code
curl -X POST http://127.0.0.1:5000/earnings_transcript_summary \
    -H "Content-Type: application/json" \
    -d '{"company_name": "Company XYZ"}'


Response:

json

{
  "financial_performance": "Company XYZ reported an increase of 12% in quarterly earnings...",
  "market_dynamics": "The company noted a shift in demand trends in North America...",
  "expansion_plans": "Plans for opening 10 new stores in the upcoming quarter...",
  "environmental_risks": "Company XYZ discussed environmental concerns regarding energy consumption...",
  "regulatory_or_policy_changes": "New government regulations are expected to impact future operations..."
}


