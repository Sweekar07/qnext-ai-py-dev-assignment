# Transcript Summarizer API Documentation

This API provides functionalities for uploading, listing, and summarizing PDF transcripts of earnings calls for companies. The service allows you to extract text from PDF files and generate summaries of these transcripts by using a summarization model.

## Table of Contents

1. [Overview](#overview)
2. [Base URL](#base-url)
3. [Endpoints](#endpoints)
    - [GET /list_pdfs](#get-list_pdfs)
    - [GET /earnings_transcript_summary](#get-earnings_transcript_summary)
    - [POST /earnings_transcript_summary](#post-earnings_transcript_summary)

## Overview

The Transcript Summarizer API helps you:

- **List Available PDF Files**: Query the available PDF files that contain earnings call transcripts for various companies.
- **Summarize Earnings Transcripts**: Input a company name and retrieve a summarized version of the corresponding earnings transcript.

## Base URL

All the API endpoints listed below are relative to the following base URL:

Example: `https://sweekar07.pythonanywhere.com/`

## Endpoints

### GET /list_pdfs

**Description**:  
This endpoint lists all available PDF files in the `documents` directory.

**Request**:
https://sweekar07.pythonanywhere.com/list_pdfs


**Response: 200**

```json
{
    "Message": "Here are the list of available PDFs.",
    "pdf_files": {
        "Earning Call Transcript - Dr Lal Pathlabs.pdf": "src/documents/Earning Call Transcript - Dr Lal Pathlabs.pdf",
        "Earning Call Transcript - One97 (Paytm).pdf": "src/documents/Earning Call Transcript - One97 (Paytm).pdf"
    }
}
```

Note: The key is the File Name and the Value is the file path stored in a JSON format.


### GET /earnings_transcript_summary

**Request using query parameter from browser:**

https://sweekar07.pythonanywhere.com/earnings_transcript_summary?company_name=<name-of-company>

Example URL:

https://sweekar07.pythonanywhere.com/earnings_transcript_summary?company_name=Earning Call Transcript - One97 (Paytm).pdf


### POST /earnings_transcript_summary

Description:
This endpoint accepts a JSON request body with the company_name and returns the summary of the earnings transcript.

**Request using payload from Postman:**

https://sweekar07.pythonanywhere.com/earnings_transcript_summary

JSON body:

```json
{
    "company_name": "Earning Call Transcript - Dr Lal Pathlabs.pdf",
    "ttranscript_text": ""
}
```

**Response: 200**:

```json
{
    "company_name": "Earning Call Transcript - One97 (Paytm).pdf",
    "environmental_risks": "No mentions of sustainability, ESG, or environmental issues were found in the provided transcript.",
    "expansion_plans": "Paytm plans to increase monetization from its devices, primarily through subscription revenues and reactivations, refurbishments, and redeployments of devices.  The company is open to doing DLG with more lending partners to scale up its lending business.  Paytm is focused on adding more lending partners and scaling existing partnerships for personal loan distribution.  There are plans to explore new loan products like home loans and mortgages in the future, but this is not the primary focus currently.",
    "financial_performance": "Paytm reported strong Q2 FY25 earnings.  The overall take rate, net of Direct Loan Guarantee (DLG) cost, for merchant loans is expected to be north of 5%.  Net payment margin improved due to better monetization of merchants and control over payment gateway costs.  The company expects to maintain these levels going forward, with some quarterly volatility due to festive seasons.  Contribution margins returned to near 55% without UPI incentives.  Significant profitability is expected this year, with a focus on becoming a consistently free cash flow positive business.",
    "market_dynamics": "The lending industry is moving towards a DLG-based structure. There is significant demand for merchant loans and personal loans, with a large market opportunity.  The company is seeing improving asset quality and collection performance in its merchant loan business.",
    "regulatory_or_policy_changes": "The company is aligning its business model with evolving regulatory guidelines and market practices, particularly in relation to Direct Loan Guarantees (DLG) for merchant loans. The company is awaiting clear direction from regulatory bodies regarding the operation of the Paytm wallet and new user onboarding through the UPI system."
}
```

