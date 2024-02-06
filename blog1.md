# Problem and Context

The problem and context of this automation script revolves around monitoring the price of a product on eBay and notifying the user if the price falls below a certain threshold.

### Monitoring eBay Product Price: 

The script fetches the HTML content of a specific eBay product page using the provided URL. It then extracts the product title and price from the page using web scraping techniques.

### Price Comparison: 

The extracted price is compared against a predefined threshold (in this case, $400). If the price is lower than the threshold, a notification is triggered to inform the user that the price has fallen.

### Automation Trigger: 

The script is designed to be run periodically or on-demand to continuously monitor the price changes of the eBay product. This automation ensures that the user stays informed about any price drops without manually checking the website.

### Notification Mechanism: 

Currently, the script notifies the user by printing a message in the console. However, in a real-world scenario, this notification mechanism is extended to send notifications via Telegram, which was the initial focus of this conversation.

### Integration Possibilities: 

This automation script can be further enhanced by integrating it with other services or platforms. For instance, it could be integrated with a Telegram bot to send notifications directly to the user's Telegram account, providing a more seamless and user-friendly experience.

