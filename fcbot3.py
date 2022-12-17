import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup as bs
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


url='https://booknow.appointment-plus.com/b6l56ers/'
executable_path = {'executable_path':'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

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

browser.find_by_id('cv-leftnav-item-calendar-available-id').click()

#put page into memory and parse
html = browser.html
soup = bs(html, "html.parser")

date_scheduled = soup.find_all('table', class_='appointment-list-style')

date_list =[]
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
  
day_date=df[df[0].str.contains(',', na=False)]
day_date = day_date.reset_index(drop=True)
day_date.rename(columns = {0:'Date'}, inplace=True)

time_slot=df[df[0].str.contains(':', na=False)]
time_slot = time_slot.reset_index(drop=True)
time_slot.rename(columns= {0:'Time'}, inplace=True)

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
print(courtsdf)
# Select only the rows containing the word, Sunday or Thursday from the dataframe
# and save it to filtered_dates.

filtered_dates = courtsdf[courtsdf['Date'].str.contains('Thursday|Sunday', case=False, regex=True)]
# filtered_dates = filtered_dates.reset_index(drop=True)
# filtered_dates = filtered_dates.drop('Date', axis=1)
filtered_dates["time_obj"] = filtered_dates['time_obj'].astype(str)
filtered_dates['time_obj'] = filtered_dates['time_obj'].replace(':','', regex=True)
filtered_dates["time_obj"] = filtered_dates['time_obj'].astype(int)

# if filtered_dates['Date'].str.contains('Sunday').any() == True:
#         # clear times that are earlier than below. 170000 = 5:00:00 PM
#         filtered_dates = filtered_dates[filtered_dates['time_obj'] >= 170000]
#         filtered_dates = filtered_dates.reset_index(drop=True)
#         print(filtered_dates)

# else:
#         filtered_dates = filtered_dates[filtered_dates['time_obj'] >= 190000]
#         filtered_dates = filtered_dates.reset_index(drop=True)
#         print(filtered_dates)

if filtered_dates.empty:
        print("No Times Available.")
else:
        if filtered_dates['Date'].str.contains('Sunday').any() == True:
                # clear times that are earlier than below. 170000 = 5:00:00 PM
                filtered_dates = filtered_dates[filtered_dates['time_obj'] >= 170000]
                filtered_dates = filtered_dates.reset_index(drop=True)
                print(filtered_dates)

        else:
                # for all the other days. book at 7PM
                filtered_dates = filtered_dates[filtered_dates['time_obj'] >= 190000]
                filtered_dates = filtered_dates.reset_index(drop=True)
                print(filtered_dates)
                
        court_id = filtered_dates.iloc[0]['Court ID']
        session_time = filtered_dates.iloc[0]['Time']

        browser.find_by_name('e_id').click()
        browser.find_by_value(court_id).click()

        book_it = browser.find_by_xpath("//td[. = '" + session_time + "']/following-sibling::td")
        book_it.find_by_value('Book it').click()
        browser.find_by_name('finalize_appt').click()



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
                msg['Subject'] = "The following time was booked\n"
                # Make sure you also add new lines to your body
                body = '\n' + filtered_dates.iloc[0]['Court Name'] + ': ' + filtered_dates.iloc[0]['Date'] +' - ' + filtered_dates.iloc[0]['Time']
                # and then attach that body furthermore you can also send html content.
                msg.attach(MIMEText(body, 'plain'))

                sms = msg.as_string()

                server.sendmail(email,sms_gateway,sms)



        # lastly quit the server
        server.quit()


browser.quit