# def subset_sum(prices, target):
#     dp = [set() for _ in range(target + 1)]
#     dp[0].add(())

#     for price in prices:
#         for i in range(target, price - 1, -1):
#             for prev in dp[i - price]:
#                 dp[i].add(prev) #dp[i].add(prev + (item,))

#     return dp[target]

def subset_sum(items, target):
    dp = {0: []}

    for price in items:
        new_dp = dp.copy()
        for total_price, combination in dp.items():
            new_total_price = total_price + price
            if new_total_price <= target:
                new_combination = combination + [price]
                if new_total_price not in dp or len(new_combination) > len(dp[new_total_price]):
                    new_dp[new_total_price] = new_combination
        dp.update(new_dp)

    return dp.get(target, [])


prices = [21.99, 44.99, 29.99, 65.99, 54.99, 23.99, 10.99, 59.99, 26.99, 49.99, 34.99, 24.99, 69.99, 39.99, 37.99, 19.99, 64.99,
          11.99, 6.99, 12.99, 13.99, 15.99]
prices.sort()
# print(prices)
target_total = 121
result = subset_sum(prices, target_total)
print(result)

if result:
    print("Items that sum up to $100:")
    for item in result:
        print("${:.2f}".format(item))
else:
    print("No combination of items sums up to $100.")


# Example usage
# items = [("item1", 10), ("item2", 20), ("item3", 30), ("item4", 40), ("item5", 50)]
# target_total = 100
# result = subset_sum(items, target_total)


# if result:
#     print("Items that sum up to $100:")
#     for item in result:
#         print(item)
# else:
#     print("No combination of items sums up to $100.")


# Scrap the website using beautiful soup
# import requests
# from bs4 import BeautifulSoup

# store_url = "https://merchandise-eu.cisco.com/catalog/category/view/s/view-all/id/61/"

# store_url_apparel = "https://merchandise-eu.cisco.com/apparel"

# store_url_apparel_women = "https://merchandise-eu.cisco.com/apparel/women?price=0-100"

# page = requests.get(store_url_apparel_women) # Getting page HTML through request
# soup = BeautifulSoup(page.content, 'html.parser') # Parsing content using beautifulsoup

# #print(soup)

# elements = soup.find_all('li', class_="product-item")
# print(elements[0])

# elements = soup.find_all('ol.products.list.items.product_items')
# print(elements)

# Find the flex element
# flex_element = soup.find_all('span', class_="price")
# #flex_element = soup.find('div', class_='product_item-details')

# print(flex_element)

# Get the event attribute of the flex element
# event_attribute = flex_element.get('event')

# # Print the event attribute
# print(event_attribute)

# Find all event elements
# event_elements = soup.find_all('div', class_='event')

# # Loop through the event elements and print their contents
# for event_element in event_elements:
#     print(event_element.text)

# links = soup.select("table tbody tr td.titleColumn a") # Selecting all of the anchors with titles
# first10 = links[:10] # Keep only the first 10 anchors
# for anchor in first10:
#     print(anchor.text) # Display the innerText of each anchor
