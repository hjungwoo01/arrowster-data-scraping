import requests
import pandas as pd

def get_social_science_rankings():
    universities = []
    for page in range(0, 37):
        url = f"https://www.topuniversities.com/rankings/endpoint?nid=3948170&page={page}&items_per_page=15&tab=indicators&region=&countries=&cities=&search=&star=&sort_by=rank&order_by=asc&program_type=&loggedincache="
        # print(f"Requesting page {page}")
        try:
            response = requests.get(url, timeout=20)
            response.raise_for_status()
            data = response.json()
            
            for item in data['score_nodes']:
                university = {
                    'Rank': item.get('rank_display', ''),
                    'Name': item.get('title', ''),
                    'Location': f"{item.get('city', '')}, {item.get('country', '')}",
                    'Overall Score': item.get('overall_score', ''),
                    'Academic Reputation Score': '',
                    'Employer Reputation Score': '',
                    'Citations per Paper Score': '',
                    'H-index Citations Score': '',
                    'International Research Network Score': ''
                }
                
                for score in item.get('scores', []):
                    if score['indicator_name'] == 'Academic Reputation':
                        university['Academic Reputation Score'] = score['score']
                    elif score['indicator_name'] == 'Employer Reputation':
                        university['Employer Reputation Score'] = score['score']
                    elif score['indicator_name'] == 'Citations per Paper':
                        university['Citations per Paper Score'] = score['score']
                    elif score['indicator_name'] == 'H-index Citations':
                        university['H-index Citations Score'] = score['score']
                    elif score['indicator_name'] == 'International Research Network':
                        university['International Research Network Score'] = score['score']
                
                universities.append(university)
            
            # print(f"Processed page {page}, current total universities: {len(universities)}")
        except requests.exceptions.RequestException as e:
            # print(f"Request failed for page {page}: {e}")
            break
    
    return universities

def get_natural_science_rankings():
    universities = []
    base_url = "https://www.topuniversities.com/rankings/endpoint?nid=3948169&page={page}&items_per_page=15&tab=indicators&region=&countries=&cities=&search=&star=&sort_by=rank&order_by=asc&program_type=&loggedincache="
    
    for page in range(0, 37):  # Total 37 pages
        url = base_url.format(page=page)
        # print(f"Requesting page {page}")
        try:
            response = requests.get(url, timeout=20)
            response.raise_for_status()
            data = response.json()
            
            for item in data['score_nodes']:
                university = {
                    'Rank': item.get('rank_display', ''),
                    'Name': item.get('title', ''),
                    'Location': f"{item.get('city', '')}, {item.get('country', '')}",
                    'Overall Score': item.get('overall_score', ''),
                    'Academic Reputation Score': '',
                    'Employer Reputation Score': '',
                    'Citations per Paper Score': '',
                    'H-index Citations Score': '',
                    'International Research Network Score': ''
                }
                
                for score in item.get('scores', []):
                    if score['indicator_name'] == 'Academic Reputation':
                        university['Academic Reputation Score'] = score['score']
                    elif score['indicator_name'] == 'Employer Reputation':
                        university['Employer Reputation Score'] = score['score']
                    elif score['indicator_name'] == 'Citations per Paper':
                        university['Citations per Paper Score'] = score['score']
                    elif score['indicator_name'] == 'H-index Citations':
                        university['H-index Citations Score'] = score['score']
                    elif score['indicator_name'] == 'International Research Network':
                        university['International Research Network Score'] = score['score']
                
                universities.append(university)
            
            # print(f"Processed page {page}, current total universities: {len(universities)}")
        except requests.exceptions.RequestException as e:
            # print(f"Request failed for page {page}: {e}")
            break
    
    return universities

def get_life_sciences_and_medicine_rankings():
    universities = []
    base_url = "https://www.topuniversities.com/rankings/endpoint?nid=3948168&page={page}&items_per_page=15&tab=indicators&region=&countries=&cities=&search=&star=&sort_by=rank&order_by=asc&program_type=&loggedincache="
    
    for page in range(0, 37):  # Total 37 pages
        url = base_url.format(page=page)
        # print(f"Requesting page {page}")
        try:
            response = requests.get(url, timeout=20)
            response.raise_for_status()
            data = response.json()
            
            for item in data['score_nodes']:
                university = {
                    'Rank': item.get('rank_display', ''),
                    'Name': item.get('title', ''),
                    'Location': f"{item.get('city', '')}, {item.get('country', '')}",
                    'Overall Score': item.get('overall_score', ''),
                    'Academic Reputation Score': '',
                    'Employer Reputation Score': '',
                    'Citations per Paper Score': '',
                    'H-index Citations Score': '',
                    'International Research Network Score': ''
                }
                
                for score in item.get('scores', []):
                    if score['indicator_name'] == 'Academic Reputation':
                        university['Academic Reputation Score'] = score['score']
                    elif score['indicator_name'] == 'Employer Reputation':
                        university['Employer Reputation Score'] = score['score']
                    elif score['indicator_name'] == 'Citations per Paper':
                        university['Citations per Paper Score'] = score['score']
                    elif score['indicator_name'] == 'H-index Citations':
                        university['H-index Citations Score'] = score['score']
                    elif score['indicator_name'] == 'International Research Network':
                        university['International Research Network Score'] = score['score']
                
                universities.append(university)
            
            # print(f"Processed page {page}, current total universities: {len(universities)}")
        except requests.exceptions.RequestException as e:
            # print(f"Request failed for page {page}: {e}")
            break
    
    return universities

def get_engineering_and_technology_rankings():
    universities = []
    base_url = "https://www.topuniversities.com/rankings/endpoint?nid=3948167&page={page}&items_per_page=15&tab=indicators&region=&countries=&cities=&search=&star=&sort_by=rank&order_by=asc&program_type=&loggedincache="
    
    for page in range(0, 37):  # Total 37 pages
        url = base_url.format(page=page)
        # print(f"Requesting page {page}")
        try:
            response = requests.get(url, timeout=20)
            response.raise_for_status()
            data = response.json()
            
            for item in data['score_nodes']:
                university = {
                    'Rank': item.get('rank_display', ''),
                    'Name': item.get('title', ''),
                    'Location': f"{item.get('city', '')}, {item.get('country', '')}",
                    'Overall Score': item.get('overall_score', ''),
                    'Academic Reputation Score': '',
                    'Employer Reputation Score': '',
                    'Citations per Paper Score': '',
                    'H-index Citations Score': '',
                    'International Research Network Score': ''
                }
                
                for score in item.get('scores', []):
                    if score['indicator_name'] == 'Academic Reputation':
                        university['Academic Reputation Score'] = score['score']
                    elif score['indicator_name'] == 'Employer Reputation':
                        university['Employer Reputation Score'] = score['score']
                    elif score['indicator_name'] == 'Citations per Paper':
                        university['Citations per Paper Score'] = score['score']
                    elif score['indicator_name'] == 'H-index Citations':
                        university['H-index Citations Score'] = score['score']
                    elif score['indicator_name'] == 'International Research Network':
                        university['International Research Network Score'] = score['score']
                
                universities.append(university)
            
            # print(f"Processed page {page}, current total universities: {len(universities)}")
        except requests.exceptions.RequestException as e:
            # print(f"Request failed for page {page}: {e}")
            break
    
    return universities

def get_arts_and_humanities_rankings():
    universities = []
    base_url = "https://www.topuniversities.com/rankings/endpoint?nid=3948166&page={page}&items_per_page=15&tab=indicators&region=&countries=&cities=&search=&star=&sort_by=rank&order_by=asc&program_type=&loggedincache="
    
    for page in range(0, 37):  # Total 37 pages
        url = base_url.format(page=page)
        # print(f"Requesting page {page}")
        try:
            response = requests.get(url, timeout=20)
            response.raise_for_status()
            data = response.json()
            
            for item in data['score_nodes']:
                university = {
                    'Rank': item.get('rank_display', ''),
                    'Name': item.get('title', ''),
                    'Location': f"{item.get('city', '')}, {item.get('country', '')}",
                    'Overall Score': item.get('overall_score', ''),
                    'Academic Reputation Score': '',
                    'Employer Reputation Score': '',
                    'Citations per Paper Score': '',
                    'H-index Citations Score': '',
                    'International Research Network Score': ''
                }
                
                for score in item.get('scores', []):
                    if score['indicator_name'] == 'Academic Reputation':
                        university['Academic Reputation Score'] = score['score']
                    elif score['indicator_name'] == 'Employer Reputation':
                        university['Employer Reputation Score'] = score['score']
                    elif score['indicator_name'] == 'Citations per Paper':
                        university['Citations per Paper Score'] = score['score']
                    elif score['indicator_name'] == 'H-index Citations':
                        university['H-index Citations Score'] = score['score']
                    elif score['indicator_name'] == 'International Research Network':
                        university['International Research Network Score'] = score['score']
                
                universities.append(university)
            
            # print(f"Processed page {page}, current total universities: {len(universities)}")
        except requests.exceptions.RequestException as e:
            # print(f"Request failed for page {page}: {e}")
            break
    
    return universities

def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)

if __name__ == "__main__":
    # Data Retrieval
    # social_science_rankings = get_social_science_rankings()
    # natural_science_rankings = get_natural_science_rankings()
    # life_sciences_and_medicine_rankings = get_life_sciences_and_medicine_rankings()
    # engineering_and_technology_rankings = get_engineering_and_technology_rankings()
    arts_and_humanities_rankings = get_arts_and_humanities_rankings()
    
    print("Saving data to CSV...")
    # save_to_csv(social_science_rankings, 'social_science_rankings.csv')
    # save_to_csv(natural_science_rankings, 'natural_science_rankings.csv')
    # save_to_csv(life_sciences_and_medicine_rankings, 'life_sciences_and_medicine_rankings.csv')
    # save_to_csv(engineering_and_technology_rankings, 'engineering_and_technology_rankings.csv')
    save_to_csv(arts_and_humanities_rankings, 'arts_and_humanities_rankings.csv')
    
    print("Data saved to CSV files")
