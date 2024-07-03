import time
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def setup_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

def scrape_topuniversities(driver):
    url = "https://www.topuniversities.com/world-university-rankings"
    driver.get(url)
    time.sleep(10)  # Wait for the page to load completely

    rankings = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    for row in soup.select('div._qs-ranking-data-row'):
        rank = row.select_one('div._univ-rank').text.strip()
        name = row.select_one('a.uni-link').text.strip()
        location = row.select_one('div.location').text.strip()
        score = row.select_one('span.overall-score-span').text.strip()
        rankings.append({'Rank': rank, 'Name': name, 'Location': location, 'Score': score})
    
    return rankings

def scrape_usnews_universities(driver):
    url = "https://www.usnews.com/best-colleges/rankings/national-universities"
    driver.get(url)
    time.sleep(10)

    universities = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    cards = soup.select('div.Card__CardOverview-sc-1ra20i5-9')

    for card in cards:
        try:
            name = card.select_one('h3.Heading-sc-1w5xk2o-0').text.strip()
            location = card.select_one('p.Paragraph-sc-1iyax29-0').text.strip()
            ranking = card.select_one('div.RankList__Rank-sc-2xewen-2 strong').text.strip() if card.select_one('div.RankList__Rank-sc-2xewen-2 strong') else ''
            rating_element = card.select_one('div.Rating__Container-sc-1naeqqj-0 span.ReviewSnapshot__StyledSpan-sc-702mfw-0')
            rating = rating_element.text.split()[0] if rating_element else ''
            num_reviews = rating_element.text.split()[-2] if rating_element else ''
            description = card.select_one('div.MultilineEllipsis__Container-sc-1hoyc1r-5').text.strip() if card.select_one('div.MultilineEllipsis__Container-sc-1hoyc1r-5') else ''

            universities.append({
                'Name': name,
                'Location': location,
                'Ranking': ranking,
                'Rating': rating,
                'Number of Reviews': num_reviews,
                'Description': description
            })
        except AttributeError as e:
            print(f"Error parsing card: {e}")
            continue
    
    return universities

def scrape_niche_universities(driver):
    url = "https://www.niche.com/colleges/search/best-colleges/"
    driver.get(url)
    time.sleep(10)

    universities = []
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    cards = soup.select('a.search-result__link')

    for card in cards:
        try:
            name = card.select_one('h2.MuiTypography-root').text.strip()
            ranking = card.select_one('div.search-result-badge').text.strip() if card.select_one('div.search-result-badge') else ''
            location = card.select('li.search-result-tagline__item span.MuiTypography-root')[0].text.strip() if card.select('li.search-result-tagline__item span.MuiTypography-root') else ''
            rating_reviews = card.select_one('div.review__stars').text.strip() if card.select_one('div.review__stars') else ''
            rating = rating_reviews.split(' ')[2] if rating_reviews else ''
            num_reviews = rating_reviews.split(' ')[-2] if rating_reviews else ''
            acceptance_rate = card.find('span', text='Acceptance rate').find_next('span').text.strip() if card.find('span', text='Acceptance rate') else ''
            net_price = card.find('span', text='Net price').find_next('span').text.strip() if card.find('span', text='Net price') else ''
            sat_range = card.find('span', text='SAT range').find_next('span').text.strip() if card.find('span', text='SAT range') else ''
            description = card.select_one('div.search-result-feature').text.strip() if card.select_one('div.search-result-feature') else ''

            universities.append({
                'Name': name,
                'Ranking': ranking,
                'Location': location,
                'Rating': rating,
                'Number of Reviews': num_reviews,
                'Acceptance Rate': acceptance_rate,
                'Net Price': net_price,
                'SAT Range': sat_range,
                'Description': description
            })
        except AttributeError as e:
            print(f"Error parsing card: {e}")
            continue
    
    return universities

def scrape_times_higher_education():
    html_content = """<table><tbody><tr height="19" style="height: 14.4pt;"><td height="19" width="64" style="height: 14.4pt; width: 48pt;">US rank 2024</td><td class="xl66" width="64" style="width: 48pt;">World University Rank 2024<span>&nbsp;</span></td><td class="xl66" width="64" style="width: 48pt;">World University Rank 2023<span>&nbsp;</span></td><td class="xl65" width="275" style="width: 206pt;">University</td><td class="xl65" width="103" style="width: 77pt;">City</td><td width="64" style="width: 48pt;">State</td></tr><tr height="19" style="height: 14.4pt;"><td align="right" height="19" style="height: 14.4pt;">1</td><td class="xl68" style="border-top: none;">2<span>&nbsp;</span></td><td class="xl68" style="border-top: none;">=3<span>&nbsp;</span></td><td class="xl67" style="border-top: none;"><a href="/world-university-rankings/stanford-university">Stanford University</a></td><td class="xl67" style="border-top: none;">Stanford</td><td>California</td></tr><tr height="19" style="height: 14.4pt;"><td align="right" height="19" style="height: 14.4pt;">2</td><td class="xl70" style="border-top: none;">3<span>&nbsp;</span></td><td class="xl70" style="border-top: none;">5<span>&nbsp;</span></td><td class="xl69" style="border-top: none;"><a href="/world-university-rankings/massachusetts-institute-technology">Massachusetts Institute of Technology</a></td><td class="xl69" style="border-top: none;">Cambridge</td><td>Massachusetts</td></tr><tr height="19" style="height: 14.4pt;"><td align="right" height="19" style="height: 14.4pt;">3</td><td class="xl68" style="border-top: none;">4<span>&nbsp;</span></td><td class="xl68" style="border-top: none;">2<span>&nbsp;</span></td><td class="xl67" style="border-top: none;"><a href="/world-university-rankings/harvard-university">Harvard University</a></td><td class="xl67" style="border-top: none;">Cambridge</td><td>Massachusetts</td></tr><tr height="19" style="height: 14.4pt;"><td align="right" height="19" style="height: 14.4pt;">4</td><td class="xl70" style="border-top: none;">6<span>&nbsp;</span></td><td class="xl70" style="border-top: none;">7<span>&nbsp;</span></td><td class="xl69" style="border-top: none;"><a href="/world-university-rankings/princeton-university">Princeton University</a></td><td class="xl69" style="border-top: none;">Princeton</td><td>New Jersey</td></tr><tr height="19" style="height: 14.4pt;"><td align="right" height="19" style="height: 14.4pt;">5</td><td class="xl68" style="border-top: none;">7<span>&nbsp;</span></td><td class="xl68" style="border-top: none;">6<span>&nbsp;</span></td><td class="xl67" style="border-top: none;"><a href="/world-university-rankings/california-institute-technology">California Institute of Technology</a></td><td class="xl67" style="border-top: none;">Pasadena</td><td>California</td></tr></tbody></table>"""  # Replace this with the actual HTML content


    soup = BeautifulSoup(html_content, 'html.parser')
    table = soup.find('table')
    rows = table.find_all('tr')[1:]  # Skip the header row

    universities = []
    for row in rows:
        cells = row.find_all('td')
        try:
            us_rank_2024 = cells[0].get_text(strip=True)
            world_rank_2024 = cells[1].get_text(strip=True)
            world_rank_2023 = cells[2].get_text(strip=True)
            university = cells[3].get_text(strip=True)
            city = cells[4].get_text(strip=True)
            state = cells[5].get_text(strip=True)

            universities.append({
                'US Rank 2024': us_rank_2024,
                'World University Rank 2024': world_rank_2024,
                'World University Rank 2023': world_rank_2023,
                'University': university,
                'City': city,
                'State': state
            })
        except AttributeError as e:
            print(f"Error parsing row: {e}")
            continue

    return universities

# Initialize WebDriver
driver = setup_driver()

# Run the scraping functions
# topuniversities_rankings = scrape_topuniversities(driver)
# usnews_rankings = scrape_usnews_universities(driver)
# niche_rankings = scrape_niche_universities(driver)
timeshighereducation_rankings = scrape_times_higher_education()

# Convert to a DataFrame
# topuniversities_rankings_df = pd.DataFrame(topuniversities_rankings)
# usnews_rankings_df = pd.DataFrame(usnews_rankings)
# niche_rankings_df = pd.DataFrame(niche_rankings)
timeshighereducation_rankings_df = pd.DataFrame(timeshighereducation_rankings)

# Save to CSV
# topuniversities_rankings_df.to_csv('topuniversities_rankings.csv', index=False)
# usnews_rankings_df.to_csv('usnews_rankings.csv', index=False)
# niche_rankings_df.to_csv('niche_rankings.csv', index=False)
timeshighereducation_rankings_df.to_csv('timeshighereducation_rankings.csv', index=False)

print("Data saved to CSV files")

driver.quit()
