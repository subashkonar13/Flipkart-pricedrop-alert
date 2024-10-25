# 📉 Flipkart Price Drop Tracker

A Python tool to track price changes on a Flipkart product page, log the price history to a CSV file, and send an email notification when the price drops. This tool can be scheduled to check the product price at regular intervals.

## ✨ Features

- 🔍 **Real-time Price Scraping**: Automatically fetches the current price of a specified Flipkart product.
- 📊 **CSV Price History Logging**: Logs price history in a CSV file to track price trends.
- 📧 **Email Alerts**: Sends an email when a price drop is detected.
- ⏰ **Configurable Scheduling**: Schedule the price check intervals (e.g., every hour).

### 1.🛠️ Prerequisites

- Python 3.x
- Flipkart product URL
- A Gmail account (for email notifications)


### 2. 📦 Install Dependencies
To install the required Python packages, run:

```bash
pip install -r requirements.txt
```

This command installs all dependencies, including:
- **requests**: For sending HTTP requests to Flipkart's website.
- **BeautifulSoup4**: For parsing and extracting price details from the page HTML.
- **smtplib** and **email**: For sending email notifications when price changes are detected.
- **schedule**: To automate running the script at specified intervals.

### 3. ⚙️ Configure Settings
Open `main.py` and configure the following:

- `product_url`: The Flipkart product URL you want to track.
- `sender_email`, `receiver_email`, and `email_password`: Your Gmail credentials and the recipient's email for notifications.
- `price_history_file`: Path to the CSV file where price history will be logged.

---

## 🚀 Usage

### 📝 Step 1: Configure Settings
- **Flipkart Product URL**: Set the `product_url` to the link of the Flipkart product you want to track.
- **Email Credentials**: Update `sender_email`, `receiver_email`, and `email_password` for Gmail notifications.

### 🏃 Step 2: Run the Tracker
Run the tracker by executing:

```bash
python main.py
```

The **PriceTracker** class will:
1. Fetch the current product price.
2. Log the price to the specified CSV file (`price_history.csv`).
3. Send an email alert if a price drop is detected (when the current price is lower than the last logged price).

### ⏲️ Step 3: Scheduling
The tracker can be set to run at regular intervals using the **Scheduler** class. By default, it checks every 1 hour. To change the interval, adjust the `interval_hours` parameter in `scheduler.py`.

### 🔄 Run in Background
To keep the tracker running continuously in the background, you can use:

- **nohup** on Unix/Linux systems:
  ```bash
  nohup python main.py &
  ```
- **cron jobs** on Linux/Mac or **Task Scheduler** on Windows.

---

## 📂 File Structure
- **price_scraper.py**: Fetches the product price from Flipkart.
- **price_logger.py**: Logs and retrieves the last logged price.
- **email_notifier.py**: Sends an email alert on price drop.
- **scheduler.py**: Manages regular scheduling of price checks.
- **main.py**: Orchestrates tracking, logging, and notifying.

## 📈 CSV File Example
The `price_history.csv` logs each price check with a timestamp and price:

```csv
timestamp,price
2024-10-24 14:15:00,1199.00
2024-10-24 15:15:00,1099.00
...
```

---

## 🔧 Troubleshooting

- **403 Forbidden Error**: Ensure you include browser headers in `price_scraper.py`.
- **Email Sending Issues**: Enable "Allow less secure app access" in your Gmail settings.
- **Scheduling**: If it doesn’t run on schedule, verify Python and scheduling tool configurations.

---

## 📜 License
This project is licensed under the MIT License.
