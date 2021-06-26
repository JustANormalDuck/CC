# Do a post request to get section IDs for the course (https://selfservice.bergen.edu/Student/Courses/Search?keyword=cis165)
# Do a post request to sectionsAsync with their JSON format to get the course times/etc
# format the JSON response and display on discord
import requests
url='https://selfservice.bergen.edu/Student/Courses/SearchAsync'
coursename='cis165'
json={"searchParameters":"{\"keyword\":\"placeholder\"}"}
json['searchParameters']=json['searchParameters'].replace('placeholder',coursename)
headers = {
    'Host': 'selfservice.bergen.edu',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json, charset=utf-8',
    '__RequestVerificationToken': 'u5ZIERO6awkVrwKT0RLDuKvi5OKEYmCNl7jnO1WAbL6k2tU0MlAh1LAMHa26RCHdzWzE8XH3PR-E5a0dPELJB3ogm6yS476fZI9Ic8Eu_pc1',
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '750',
    'Connection': 'keep-alive',
    'Cookie': 'AMCV_4D6368F454EC41940A4C98A6%40AdobeOrg=870038026%7CMCIDTS%7C18687%7CMCMID%7C90344209994971932212038851338118089713%7CMCAID%7CNONE%7CMCOPTOUT-1614529868s%7CNONE%7CvVersion%7C5.0.0; amplitude_id_9f6c0bb8b82021496164c672a7dc98d6_edmbergen.edu=eyJkZXZpY2VJZCI6Ijg3ODAxNGI4LTIyMGItNGMyZC04YzE1LTFmNmY0ODI2OWY0OVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU5ODgyOTI5NjE4MSwibGFzdEV2ZW50VGltZSI6MTU5ODgyOTk5NzkwOCwiZXZlbnRJZCI6MCwiaWRlbnRpZnlJZCI6MzUsInNlcXVlbmNlTnVtYmVyIjozNX0=; studentselfservice_production_Sso=s8LmHk76Uh4eGwibqN94B/8OHbHRS4c+KH/lOcMhsx1b/5CJRUZelKUnYygMOzkCfT3Y/383QUVI64liGHTJ2YSDGQZD8dhGkbmQ9Lh5WRtVYh7AXoDKW7pJ1djl+RRR; __RequestVerificationToken_L1N0dWRlbnQ1=EzkRXWognkpclON7dY1mfmE-GW2n2ci-WFlGf94Q_VFYLQ6xrcvxjJgKAXNWiyXDUos3tZjxfQrJy0MbPIl72StMFfV55ouq5pMLRzNbj7M1',
    'Cache-Control': 'max-age=0',
    'TE':'Trailers'
}
sample=requests.post(url=url,json=json ,headers=headers)
json={"courseId":sample.json()['Courses'][0]['Id'],"sectionIds":sample.json()['Courses'][0]['MatchingSectionIds']}
url='https://selfservice.bergen.edu/Student/Courses/SectionsAsync'
sample=requests.post(url=url,json=json,headers=headers)
for i in range(len(sample.json()['TermsAndSections'])):
    for j in range(len(sample.json()['TermsAndSections'][i]['Sections'])):
        print(sample.json()['TermsAndSections'][i]['Sections'][j]['FacultyDisplay'])


#To Extract from JSON:
# Faculty Name: sample.json()['TermsAndSections'][i]['Sections'][j]['FacultyDisplay']
# Course Time: sample.json()['TermsAndSections'][i]['Sections'][j]['Section']['FormattedMeetingTimes'][k] after that you need ['DaysOfWeekDisplay'][j] and ['StartTimeDisplay'] and ['EndTimeDisplay']
# Consider adding ['BuildingDisplay'] and ['RoomDisplay'] (same path as previous comment)
# Seats Left: sample.json()['TermsAndSections'][i]['Sections'][j]['Section']['Available']
# Section Name: sample.json()['TermsAndSections'][i]['Sections'][j]['Section']['SectionNameDisplay'])