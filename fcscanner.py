import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sys

url='https://booknow.appointment-plus.com/b6l56ers/'
executable_path = {'executable_path':'chromedriver.exe'}
browser = Browser('chrome',**executable_path, headless=False)

browser.visit(url)

#log into page and open up the pages that are going to be scraped.
input_element = browser.find_by_name('loginname')   
input_element.fill('jmedias')

input_element = browser.find_by_name('password')   
input_element.fill('3ggR0ll$')

button_element = browser.find_by_value('Log In').click()

browser.find_by_name('e_id').click()
browser.find_by_value('4807').click()

browser.find_by_name('service_id').click()
browser.find_by_value('6453').click()

# check to see if the table tag with the class 'appointment-list-style' exists.
# if no = True, switch courts and see if the table class exists. 
# if no = True, close browser and exit program. 
# if no = False, check to see if table tag exist. 
# if yes = True, click on the link. 
# then create an empty list called date_list
# get all the text that is in between the <td></td> tags
# and enter it ino the date_list list. 

if browser.is_element_not_present_by_id('cv-leftnav-item-calendar-available-id'):
    browser.find_by_name('e_id').click()
    browser.find_by_value('5311').click()
    
    if browser.is_element_not_present_by_id('cv-leftnav-item-calendar-available-id'):
        browser.quit
        sys.exit()
            
    if browser.find_by_id('cv-leftnav-item-calendar-available-id'):
        browser.find_by_id('cv-leftnav-item-calendar-available-id').click()   
else:
    browser.find_by_id('cv-leftnav-item-calendar-available-id').click()

html = browser.html
soup = bs(html, "html.parser")

date_scheduled = soup.find_all('table', class_='appointment-list-style')

date_list =[]
for TDs in date_scheduled:
    innerDivs= TDs.find_all("td")
    for idiv in innerDivs:
            date_list.append(idiv.get_text(strip=True))

# if the next button is available, 
# click it and grab all the text that is in between <td>,/td> 
# and add it to the date_list list. 

if browser.is_element_present_by_name('next'):
        browser.find_by_name('next').click()
        
        html = browser.html
        soup = bs(html, "html.parser")
        date_scheduled = soup.find_all('table', class_='appointment-list-style')
        
        for TDs in date_scheduled:
                innerDivs= TDs.find_all("td")
                for idiv in innerDivs:
                        date_list.append(idiv.get_text(strip=True))

if browser.is_element_present_by_name('next'):
        browser.find_by_name('next').click()
        
        html = browser.html
        soup = bs(html, "html.parser")
        date_scheduled = soup.find_all('table', class_='appointment-list-style')
        
        for TDs in date_scheduled:
                innerDivs= TDs.find_all("td")
                for idiv in innerDivs:
                        date_list.append(idiv.get_text(strip=True))


df = pd.DataFrame(date_list)

# extract all the rows that contain a ',' from the df and save to the day_date df.Date
# reset the index and rename the column from 0 to Date.

day_date=df[df[0].str.contains(',', na=False)]
day_date = day_date.reset_index(drop=True)
day_date.rename(columns = {0:'Date'}, inplace=True)

# extract all the rows that contain ':' and save it to the time_slot df.  
# reset the index and rename the column from 0 to Time. 

time_slot=df[df[0].str.contains(':', na=False)]
time_slot = time_slot.reset_index(drop=True)
time_slot.rename(columns= {0:'Time'}, inplace=True)

# create court1df by joining the day_date and time_slot together as two separate columns
# create a new column called Court Name. This will be used for the text message.
# create a new column called Court ID. This will be used by splinter when booking in the 
#  other program. 

court1df = day_date.join(time_slot)
court1df['Court Name'] = 'Court 1'
court1df['Court ID'] = '4807' 
court1df = court1df[['Court Name', 'Date', 'Time','Court ID']]

browser.find_by_name('e_id').click()
browser.find_by_value('5311').click()

html = browser.html
soup = bs(html, "html.parser")

# find the table tag with the class 'appointment-list-style'
# then create an empty list called date_list
# get all the text that is in between the <td></td> tags
# and enter it ino the date_list list. 

date_scheduled = soup.find_all('table', class_='appointment-list-style')

date_list =[]
for TDs in date_scheduled:
    innerDivs= TDs.find_all("td")
    for idiv in innerDivs:
            date_list.append(idiv.get_text(strip=True))

# if the next button is available, 
# click it and grab all the text that is in between <td>,/td> 
# and add it to the date_list list. 

if browser.is_element_present_by_name('next'):
        browser.find_by_name('next').click()
        
        html = browser.html
        soup = bs(html, "html.parser")
        date_scheduled = soup.find_all('table', class_='appointment-list-style')
        
        for TDs in date_scheduled:
                innerDivs= TDs.find_all("td")
                for idiv in innerDivs:
                        date_list.append(idiv.get_text(strip=True))

if browser.is_element_present_by_name('next'):
        browser.find_by_name('next').click()
        
        html = browser.html
        soup = bs(html, "html.parser")
        date_scheduled = soup.find_all('table', class_='appointment-list-style')
        
        for TDs in date_scheduled:
                innerDivs= TDs.find_all("td")
                for idiv in innerDivs:
                        date_list.append(idiv.get_text(strip=True))


df = pd.DataFrame(date_list)

# extract all the rows that contain a ',' from the df and save to the day_date df.Date
# reset the index and rename the column from 0 to Date. 

day_date = df[df[0].str.contains(',', na=False)]
day_date = day_date.reset_index(drop=True)
day_date.rename(columns = {0:'Date'}, inplace=True)

# extract all the rows that contain ':' and save it to the time_slot df.  
# reset the index and rename the column from 0 to Time. 

time_slot = df[df[0].str.contains(':', na=False)]
time_slot = time_slot.reset_index(drop=True)
time_slot.rename(columns= {0:'Time'}, inplace=True)

# create court2df by joining the day_date and time_slot together as two separate columns
# create a new column called Court Name. This will be used for the text message.
# create a new column called Court ID. This will be used by splinter when booking in the 
#  other program. 

court2df = day_date.join(time_slot)
court2df['Court Name'] = 'Court 2' 
court2df['Court ID'] = '5311'
court2df = court2df[['Court Name', 'Date', 'Time','Court ID']]


# add the court2df to the bottom of court1df. 
# then create a new column in the datetime object format using the Time column
# then drop the date from the time_obj column
# sort the rows based on time_obj

courtsdf = pd.concat([court1df,court2df])
courtsdf = courtsdf.reset_index(drop=True)
courtsdf['time_obj'] = pd.to_datetime(courtsdf['Time'])
courtsdf['time_obj'] = pd.to_datetime(courtsdf['time_obj'],format='%H:%M').dt.time
courtsdf.sort_values(by='time_obj', inplace=True)

# Select only the rows containing the word, Sunday or Thursday from the dataframe
# and save it to filtered_dates.

filtered_dates = courtsdf[courtsdf['Date'].str.contains('Sunday', case=False, regex=True)]
filtered_dates = filtered_dates.reset_index(drop=True)
filtered_dates = filtered_dates.drop('Date', axis=1)
print(filtered_dates)
browser.quit

if filtered_dates['Time'].str.contains('4:00pm|4:30pm|5:00pm|5:30pm|6:00pm|6:30pm|7:00pm|7:30pm|8:00pm', case=False, regex=True).any():

        SMSdf = filtered_dates[filtered_dates['Time'].str.contains('4:00pm|4:30pm|5:00pm|5:30pm|6:00pm|6:30pm|7:00pm|7:30pm|8:00pm', case=False, regex=True)]
        SMSdf = SMSdf.reset_index(drop=True).drop('time_obj',axis=1).drop('Court ID', axis=1)
        message_body = ':\n'
        for x in SMSdf.index:
                message_body += '\n' + SMSdf['Court Name'][x] + ': ' + SMSdf['Time'][x] +'\n'
        print(message_body)   

        email = "picklebot@zohomail.com"
        pas = "cupN00dles"

        contact_List = ['8327154545@txt.att.net','2817321638@vtext.com','7133981968@tmomail.net']
        
        for telnum in contact_List:

                sms_gateway = telnum
                # The server we use to send emails in our case it will be gmail but every email provider has a different smtp 
                # and port is also provided by the email provider.
                smtp = "smtp.zoho.com" 
                port = 587
                # This will start our email server
                server = smtplib.SMTP(smtp,port)
                # Starting the server
                server.ehlo()
                server.starttls()
                # Now we need to login
                server.login(email,pas)

                # Now we use the MIME module to structure our message.
                msg = MIMEMultipart()
                msg['From'] = email
                msg['To'] = sms_gateway
                # Make sure you add a new line in the subject
                msg['Subject'] = "Available Time Slots\n"
                # Make sure you also add new lines to your body
                body = message_body
                # and then attach that body furthermore you can also send html content.
                msg.attach(MIMEText(body, 'plain'))

                sms = msg.as_string()

                server.sendmail(email,sms_gateway,sms)



        # lastly quit the server
        server.quit()