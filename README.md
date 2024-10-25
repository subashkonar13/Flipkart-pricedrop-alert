# 📉 Flipkart Price Drop Tracker

A Python tool to track price changes on a Flipkart product page, log the price history to a CSV file, and send an email notification when the price drops. This tool can be scheduled to check the product price at regular intervals.

## ✨ Features

- 🔍 **Real-time Price Scraping**: Automatically fetches the current price of a specified Flipkart product.
- 📊 **CSV Price History Logging**: Logs price history in a CSV file to track price trends.
- 📧 **Email Alerts**: Sends an email when a price drop is detected.
- ⏰ **Configurable Scheduling**: Schedule the price check intervals (e.g., every hour).

## 🛠️ Prerequisites

- Python 3.x
- Flipkart product URL
- A Gmail account (for email notifications)

## ⚙️ Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/subashkonar13/flipkart-pricedrop-alert.git
   cd flipkart-pricedrop-alert
