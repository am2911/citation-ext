import requests
import json

response=requests.get("https://devapi.beyondchats.com/api/get_message_with_sources")
data_ext=response.json()

#print(data_ext['data']['data'][1]['source'][7]['link'])

# Function to extract citations
def extract_citations(data):
    results = []
    for item in data['data']['data']:
        response = item['response']
        sources = item['source']
        citations = []
        
        for source in sources:
            context = source['context']
            link = source['link']
            if link and any(phrase in context for phrase in response.split()):
                citations.append({
                    'id': source['id'],
                    'link': link
                })

        results.append({
            'id':item['id'],
            'citations': citations
        })
    
    return results


# Running the function with the provided data
citations = extract_citations(data_ext)
print(json.dumps(citations, indent=2))
