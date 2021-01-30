from googleapiclient import discovery

API_KEY='AIzaSyClYMRcU7puoRD61T4ddvTU5SDjy7M-5EY'

# Generates API client object dynamically based on service name and version


def get_score(text):
    
   service = discovery.build('commentanalyzer', 'v1alpha1', developerKey=API_KEY)
   
   analyze_request = {'comment': { 'text': text },'requestedAttributes': {'TOXICITY': {}}}

   response = service.comments().analyze(body=analyze_request).execute()
   #response.get('attributeScores').get('TOXICITY').get('summaryScore').get('value')
   return response.get('attributeScores').get('TOXICITY').get('summaryScore').get('value')


#text = ''

#print(get_score(text))
