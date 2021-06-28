from discord.ext import commands
from discord import Embed
import requests
client = commands.Bot(command_prefix='$')
template={'faculty':'','days':[],'times':[],'section':'','seats':'','location':''}
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def cl(ctx,course):
    url='https://selfservice.bergen.edu/Student/Courses/SearchAsync'
    json={"searchParameters":"{\"keyword\":\"placeholder\"}"}
    json['searchParameters']=json['searchParameters'].replace('placeholder',course)
    headers = {
    'Host': 'selfservice.bergen.edu',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/json, charset=utf-8',
    '__RequestVerificationToken': '' ## Removed for security Reasons,
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '750',
    'Connection': 'keep-alive',
    'Cookie': '', ## Removed for security Reasons
    'Cache-Control': 'max-age=0',
    'TE':'Trailers'
    }
    sample=requests.post(url=url,json=json ,headers=headers)
    json={"courseId":sample.json()['Courses'][0]['Id'],"sectionIds":sample.json()['Courses'][0]['MatchingSectionIds']}
    url='https://selfservice.bergen.edu/Student/Courses/SectionsAsync'
    listing=requests.post(url=url,json=json,headers=headers).json()
    embed=Embed(title=listing['Course']['SubjectCode']+' '+ listing['Course']['Number'] ,description=listing['Course']['Title']+'\n'+listing['Course']['Description'])
    await ctx.send(embed=embed)
    for i in range(len(listing['TermsAndSections'])):
        embed=Embed(title=listing['TermsAndSections'][i]['Term']['Description'],description='',colour=discord.Colour.dark_purple())
        for j in range(len(listing['TermsAndSections'][i]['Sections'])):
            message='**Times:**\n'
            template['faculty']=listing['TermsAndSections'][i]['Sections'][j]['FacultyDisplay']
            template['section']=listing['TermsAndSections'][i]['Sections'][j]['Section']['SectionNameDisplay']
            template['seats']=listing['TermsAndSections'][i]['Sections'][j]['Section']['Available']
            template['location']=listing['TermsAndSections'][i]['Sections'][j]['Section']['LocationDisplay']
            temp=listing['TermsAndSections'][i]['Sections'][j]['Section']['FormattedMeetingTimes']
            for k in range(len(temp)):
                message=message+' '+temp[k]['DaysOfWeekDisplay']+' '+temp[k]['StartTimeDisplay']+'-'+temp[k]['EndTimeDisplay'] +'\n'
            embed.add_field(name=template['section'],value='**Professor:** '+template['faculty']+'\n'+
            '**Seats Left: **'+str(template['seats'])+'\n'+'**Location: **'+template['location']+'\n'+message)
        await ctx.send(embed=embed)
# Consider adding ['BuildingDisplay'] and ['RoomDisplay'] (same path as previous comment)

client.run('Token') ## Removed for security Reasons just replace with your own token to get it working
