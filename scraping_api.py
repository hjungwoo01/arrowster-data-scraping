import requests
import pandas as pd
import time
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

def get_top_universities():
    universities = []
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    session.mount('http://', HTTPAdapter(max_retries=retries))
    session.mount('https://', HTTPAdapter(max_retries=retries))
    
    for page in range(0, 102):  # Total 102 pages
        url = f"https://www.topuniversities.com/rankings/endpoint?nid=3990755&page={page}&items_per_page=15"
        try:
            response = session.get(url)
            response.raise_for_status()
            data = response.json()
            for item in data['score_nodes']:
                university = {
                    'Rank': item.get('rank_display', ''),
                    'Name': item.get('title', ''),
                    'Location': f"{item.get('city', '')}, {item.get('country', '')}",
                    'Score': item.get('overall_score', '')
                }
                universities.append(university)
            time.sleep(1)
        except requests.exceptions.RequestException as e:
            print(f"Request failed for page {page}: {e}")
            break
    
    return universities

def get_usnews_universities():
    universities = []
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504, 429])
    session.mount('http://', HTTPAdapter(max_retries=retries))
    session.mount('https://', HTTPAdapter(max_retries=retries))

    for page in range(1, 45):  # Total 44 pages
        print(f"Retrieving data for page {page}")
        url = f"https://www.usnews.com/best-colleges/api/search?format=json&schoolType=national-universities&_sort=rank&_sortDirection=asc&_page={page}"
        try:
            response = session.get(url)
            response.raise_for_status()
            data = response.json()
            schools = data.get('data', {}).get('items', [])

            for school in schools:
                print(school)
                institution = school.get('institution', {})
                searchData = school.get('searchData', {})
                university = {
                    'Name': institution.get('displayName', ''),
                    'Location': f"{institution.get('city', '')}, {institution.get('state', '')}",
                    'Ranking': school.get('ranking', {}).get('displayRank', ''),
                    'Acceptance Rate': searchData.get('acceptanceRate', {}).get('displayValue', ''),
                    'Net Price': searchData.get('costAfterAid', {}).get('displayValue', ''),
                    'SAT Range': searchData.get('satAvg', {}).get('displayValue', ''),
                    'ACT Range': searchData.get('actAvg', {}).get('displayValue', ''),
                    'Review': school.get('blurb', '')
                }
                universities.append(university)
            time.sleep(1)
        except requests.exceptions.RequestException as e:
            print(f"Request failed for page {page}: {e}")
            break

    return universities

def get_niche_universities():
    universities = []
    session = requests.Session()
    retries = Retry(total=5, backoff_factor=1, status_forcelist=[502, 503, 504])
    session.mount('http://', HTTPAdapter(max_retries=retries))
    session.mount('https://', HTTPAdapter(max_retries=retries))

    for page in range(1, 2681):  # Total 2680 pages
        print(f"Retrieving data for page {page}")
        url = f"https://www.niche.com/api/renaissance/results/?type=private&type=public&listURL=best-colleges&page={page}&searchType=college"
        try:
            response = session.get(url)
            response.raise_for_status()
            data = response.json()
            entities = data.get('entities', [])

            for entity in entities:
                content = entity.get('content', {})
                facts = {fact['label']: fact['value'] for fact in content.get('facts', [])}
                university = {
                    'Name': content.get('name', ''),
                    'Location': content.get('location', ''),
                    'Acceptance Rate': facts.get('Acceptance Rate', ''),
                    'Net Price': facts.get('Net Price', ''),
                    'SAT Range': facts.get('SAT Range', ''),
                    'Review': entity.get('featuredReview', {}).get('body', ''),
                    'Rating': entity.get('featuredReview', {}).get('rating', '')
                }
                universities.append(university)
            time.sleep(1)
        except requests.exceptions.RequestException as e:
            print(f"Request failed for page {page}: {e}")
            break

    return universities

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    top_universities_rankings = get_top_universities()
    # usnews_rankings = get_usnews_universities()
    # niche_rankings = get_niche_universities()
    
    save_to_csv(top_universities_rankings, 'topuniversities_rankings.csv')
    # save_to_csv(usnews_rankings, 'usnews_rankings.csv')
    # save_to_csv(niche_rankings, 'niche_rankings.csv')

    print("Data saved to CSV files")
