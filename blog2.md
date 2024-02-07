# FULL AUTOMATION SCRIPT AND EXPLANATION:

To automate the task of monitoring the price of a product on eBay and notifying the user if the price falls below a certain threshold,
I followed these steps and outline possible solutions:


```
import requests
from bs4 import BeautifulSoup

```
These lines import the necessary libraries needed to ensure the code runs properly. 

 The **requests** library is used for making HTTP requests to fetch web pages or interact with web services, 
 while **BeautifulSoup** is used for parsing and navigating the HTML/XML content fetched using requests, making it easier to extract and manipulate data from web pages. 
 These two libraries are commonly used together in web scraping and web automation tasks.
 

### 1. Fetching HTML Content:

Use the `requests` library to send a GET request to the eBay product page and retrieve the HTML content.
I have implemented this in my code with
```
requests.get(URL, headers=headers)
```

### 2. Parsing HTML:

Utilize a HTML parser like BeautifulSoup to extract relevant information such as product title and price from the HTML content.
I have used BeautifulSoup to extract the product title and price in the code.
```
soup = BeautifulSoup(page.content, 'html.parser')
```

### 3. Extracting Product Information:

Identify the HTML elements (classes or IDs) that contain the product title and price, and then extract their text content.
I have used soup.find() and soup.select() methods to locate and extract the product title and price. 

```
product_title = soup.find(class_='ux-textspans ux-textspans--BOLD').get_text()
print(product_title)

product_price = soup.select('#mainContent > div > div.vim.x-price-section.mar-t-20 > div > div > div > span')

```
### 4.

The product_price is a span html text scraped from the website. Then using a loop, the value of the line is taken as p.text. The value p.text contains US $ at the beginning. To format this value without "US $" the substring is taken starting from the index 4 and upto 7. The the final value is of text of 3 digit. So it is converted to integer using int(). Later, the product_price_value is printed as integer.

```

for p in product_price:
    print(p.text)
    product_price_value = int(p.text[4:7])
    print(product_price_value)

```

### 5. Comparing Prices:

Compare the extracted price against a predefined threshold (e.g., $400) to determine if it has fallen below the threshold.
I have implemented a `check_price()` function to compare the product price against $400 and print a notification accordingly.

```
def check_price():
    if (product_price_value < 400):
        print('Congrats! The price has fallen to : $' , product_price_value)
    else:
        print('Sorry, The price is still $400')
```

### 6. Notification Mechanism:
 Implement a notification mechanism to inform the user when the price falls below the threshold. This involves sending a Telegram message to the user.
```
import requests

def send_to_telegram(message):

    apiToken = '6490356169:AAGpU9ojduVolrj6U3gi0dvUmMgAuCp_2wg'
    chatID = '6847742875'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

send_to_telegram('Sorry, The price is still $400')

```
### 7. 
```
if __name__ == '__main__':
    check_price()
```

This block ensures that the **check_price** function is executed only if the script is run as the main program (not imported as a module).

## [Blog3](blog3.md)
