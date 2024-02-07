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

# Problems I encountered while developing the script:
I will be talking about problems I encountered while developing the script and how I solved these problems. I hope that by doing so, it would be helpful to you in case you come across these problems.

# Problem 1: Choosing the Right Libraries for the Python Automation:
Selecting the appropriate libraries is a crucial step that can significantly impact the success of a project on Python and I found myself facing a common dilemma: which libraries should I use?. 

The first challenge was identifying the key functionalities needed for my script. In my case, I required tools to monitor the price of a product on website A quick search on google revealed multiple options, leaving me pondering over the trade-offs between various libraries. I needed something very simple but versatile and efficient because I'm not a very advanced python user yet. 

I decided to divide my searches into various categories to make it easier to find something simple and efficient as that was my target. My first search was regarding the **web scrapping**. I needed a library that could provide real-time information about the price range of a particular product. After some research and consideration, I opted for **Beautifulsoup**. This versatile library proved to be a go-to choice for extracting the product title and product price. It was also the first result on google. 

Before I came to a conclusion on the libraries, just for good measure, I quickly went to my very good friend Chatgpt for reassurance and validation of my choice. 

To sum up, working with ChatGPT gave me confidence and confirmation for my library selections. It underlined how crucial it is to take into account elements like dependability, community support, and usability when making such choices. I now recognize the value of a well-researched library selection. It provides the groundwork for a reliable and effective automation solution in addition to streamlining development.



## [Blog2](blog2.md)

