import requests
from bs4 import BeautifulSoup
import csv

def scrape_website(url, output_file='scraped_data.csv'):
    try:
        # Send HTTP request
        print(f"Fetching data from: {url}")
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        
        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Extract data (modify selectors based on your target website)
        # Example: Extract all article titles and links
        articles = []
        for article in soup.find_all('article', limit=10):  # Limit to 10 articles
            title_elem = article.find('h2') or article.find('h3') or article.find('a')
            if title_elem:
                title = title_elem.text.strip()
                link = title_elem.get('href', 'No link') if title_elem.name == 'a' else 'Link in parent'
                articles.append({'title': title, 'link': link})
        
        # Save data to CSV
        if articles:
            with open(output_file, 'w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=['title', 'link'])
                writer.writeheader()
                writer.writerows(articles)
            
            print(f"Successfully scraped {len(articles)} items")
            print(f"Data saved to: {output_file}")
        else:
            print("No data found with current selectors")
            
        return articles
        
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return []

# Main execution
if __name__ == "__main__":
    # For ShadowFox practice (use a demo website if ShadowFox is not accessible)
    # Replace with actual ShadowFox URL or any practice website
    practice_url = "http://books.toscrape.com/"  # Example practice site
    # practice_url = "https://shadowfox.example.com"  # Replace with actual ShadowFox URL
    
    # Scrape the website
    data = scrape_website(practice_url)
    
    # Display first few items
    if data:
        print("\nFirst 3 items scraped:")
        for i, item in enumerate(data[:3], 1):
            print(f"{i}. {item['title']}")
            print(f"   Link: {item['link']}")