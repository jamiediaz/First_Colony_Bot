from splinter import Browser

# from bs4 import BeautifulSoup


url='https://booknow.appointment-plus.com/b6l56ers/'
executable_path = {'executable_path':'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

browser.visit(url)

input_element = browser.find_by_name('loginname')   
input_element.fill('jmedias')

input_element = browser.find_by_name('password')   
input_element.fill('3ggR0ll$')

browser.find_by_value('Log In').click()

browser.find_by_name('e_id').click()
browser.find_by_value('4807').click()

browser.find_by_name('service_id').click()
browser.find_by_value('6453').click()

browser.find_by_id('cv-leftnav-item-calendar-available-id').click()
# if browser.is_element_present_by_text('5:00pm'):
#     book_it = browser.find_by_xpath("//td[. = '5:00pm']/following-sibling::td")
#     book_it.find_by_value('Book it').click()
#     browser.find_by_name('finalize_appt').click()

# if browser.is_element_present_by_text('5:00pm') == False:
#     browser.find_by_name('e_id').click()
#     browser.find_by_value('5311').click()
#     if browser.is_element_present_by_text('5:00pm'):
#         book_it = browser.find_by_xpath("//td[. = '5:00pm']/following-sibling::td")
#         book_it.find_by_value('Book it').click()
#         browser.find_by_name('finalize_appt').click()
#     else:
#         browser.find_by_name('e_id').click()
#         browser.find_by_value('4807').click()

# if browser.is_element_present_by_text('5:30pm'):
#     book_it = browser.find_by_xpath("//td[. = '5:30pm']/following-sibling::td")
#     book_it.find_by_value('Book it').click()
#     browser.find_by_name('finalize_appt').click()

# if browser.is_element_present_by_text('5:30pm') == False:
#     browser.find_by_name('e_id').click()
#     browser.find_by_value('5311').click()
#     if browser.is_element_present_by_text('5:30pm'):
#         book_it = browser.find_by_xpath("//td[. = '5:30pm']/following-sibling::td")
#         book_it.find_by_value('Book it').click()
#         browser.find_by_name('finalize_appt').click()
#     else:
#         browser.find_by_name('e_id').click()
#         browser.find_by_value('4807').click()

# if browser.is_element_present_by_text('6:00pm'):
#     book_it = browser.find_by_xpath("//td[. = '6:00pm']/following-sibling::td")
#     book_it.find_by_value('Book it').click()
#     browser.find_by_name('finalize_appt').click()
    
# if browser.is_element_present_by_text('6:00pm') == False:
#     browser.find_by_name('e_id').click()
#     browser.find_by_value('5311').click()
#     if browser.is_element_present_by_text('6:00pm'):
#         book_it = browser.find_by_xpath("//td[. = '6:00pm']/following-sibling::td")
#         book_it.find_by_value('Book it').click()
#         browser.find_by_name('finalize_appt').click()
#     else:
#         browser.find_by_name('e_id').click()
#         browser.find_by_value('4807').click()    

# if browser.is_element_present_by_text('6:30pm'):
#     book_it = browser.find_by_xpath("//td[. = '6:30pm']/following-sibling::td")
#     book_it.find_by_value('Book it').click()
#     browser.find_by_name('finalize_appt').click()

# if browser.is_element_present_by_text('6:30pm') == False:
#     browser.find_by_name('e_id').click()
#     browser.find_by_value('5311').click()
#     if browser.is_element_present_by_text('6:30pm'):
#         book_it = browser.find_by_xpath("//td[. = '6:30pm']/following-sibling::td")
#         book_it.find_by_value('Book it').click()
#         browser.find_by_name('finalize_appt').click()
#     else:
#         browser.find_by_name('e_id').click()
#         browser.find_by_value('4807').click() 

if browser.is_element_present_by_text('7:00pm'):
    book_it = browser.find_by_xpath("//td[. = '7:00pm']/following-sibling::td")
    book_it.find_by_value('Book it').click()
    browser.find_by_name('finalize_appt').click()

if browser.is_element_present_by_text('7:00pm') == False:
    browser.find_by_name('e_id').click()
    browser.find_by_value('5311').click()
    if browser.is_element_present_by_text('7:00pm'):
        book_it = browser.find_by_xpath("//td[. = '7:00pm']/following-sibling::td")
        book_it.find_by_value('Book it').click()
        browser.find_by_name('finalize_appt').click()
    else:
        browser.find_by_name('e_id').click()
        browser.find_by_value('4807').click() 

if browser.is_element_present_by_text('7:30pm'):
    book_it = browser.find_by_xpath("//td[. = '7:30pm']/following-sibling::td")
    book_it.find_by_value('Book it').click()
    browser.find_by_name('finalize_appt').click()

if browser.is_element_present_by_text('7:30pm') == False:
    browser.find_by_name('e_id').click()
    browser.find_by_value('5311').click()
    if browser.is_element_present_by_text('7:30pm'):
        book_it = browser.find_by_xpath("//td[. = '7:30pm']/following-sibling::td")
        book_it.find_by_value('Book it').click()
        browser.find_by_name('finalize_appt').click()
    else:
        browser.find_by_name('e_id').click()
        browser.find_by_value('4807').click() 

if browser.is_element_present_by_text('8:00pm'):
    book_it = browser.find_by_xpath("//td[. = '8:00pm']/following-sibling::td")
    book_it.find_by_value('Book it').click()
    browser.find_by_name('finalize_appt').click()

if browser.is_element_present_by_text('8:00pm') == False:
    browser.find_by_name('e_id').click()
    browser.find_by_value('5311').click()
    if browser.is_element_present_by_text('8:00pm'):
        book_it = browser.find_by_xpath("//td[. = '8:00pm']/following-sibling::td")
        book_it.find_by_value('Book it').click()
        browser.find_by_name('finalize_appt').click()
 
else:
    if browser.is_element_present_by_name('next'):
        browser.find_by_name('next').click()
    else: print("no time available")

# if browser.is_element_present_by_text('5:00pm'):
#     book_it = browser.find_by_xpath("//td[. = '5:00pm']/following-sibling::td")
#     book_it.find_by_value('Book it').click()
#     browser.find_by_name('finalize_appt').click()

# if browser.is_element_present_by_text('5:00pm') == False:
#     browser.find_by_name('e_id').click()
#     browser.find_by_value('5311').click()
#     if browser.is_element_present_by_text('5:00pm'):
#         book_it = browser.find_by_xpath("//td[. = '5:00pm']/following-sibling::td")
#         book_it.find_by_value('Book it').click()
#         browser.find_by_name('finalize_appt').click()
#     else:
#         browser.find_by_name('e_id').click()
#         browser.find_by_value('4807').click()

# if browser.is_element_present_by_text('5:30pm'):
#     book_it = browser.find_by_xpath("//td[. = '5:30pm']/following-sibling::td")
#     book_it.find_by_value('Book it').click()
#     browser.find_by_name('finalize_appt').click()

# if browser.is_element_present_by_text('5:30pm') == False:
#     browser.find_by_name('e_id').click()
#     browser.find_by_value('5311').click()
#     if browser.is_element_present_by_text('5:30pm'):
#         book_it = browser.find_by_xpath("//td[. = '5:30pm']/following-sibling::td")
#         book_it.find_by_value('Book it').click()
#         browser.find_by_name('finalize_appt').click()
#     else:
#         browser.find_by_name('e_id').click()
#         browser.find_by_value('4807').click()

# if browser.is_element_present_by_text('6:00pm'):
#     book_it = browser.find_by_xpath("//td[. = '6:00pm']/following-sibling::td")
#     book_it.find_by_value('Book it').click()
#     browser.find_by_name('finalize_appt').click()
    
# if browser.is_element_present_by_text('6:00pm') == False:
#     browser.find_by_name('e_id').click()
#     browser.find_by_value('5311').click()
#     if browser.is_element_present_by_text('6:00pm'):
#         book_it = browser.find_by_xpath("//td[. = '6:00pm']/following-sibling::td")
#         book_it.find_by_value('Book it').click()
#         browser.find_by_name('finalize_appt').click()
#     else:
#         browser.find_by_name('e_id').click()
#         browser.find_by_value('4807').click()    

# if browser.is_element_present_by_text('6:30pm'):
#     book_it = browser.find_by_xpath("//td[. = '6:30pm']/following-sibling::td")
#     book_it.find_by_value('Book it').click()
#     browser.find_by_name('finalize_appt').click()

# if browser.is_element_present_by_text('6:30pm') == False:
#     browser.find_by_name('e_id').click()
#     browser.find_by_value('5311').click()
#     if browser.is_element_present_by_text('6:30pm'):
#         book_it = browser.find_by_xpath("//td[. = '6:30pm']/following-sibling::td")
#         book_it.find_by_value('Book it').click()
#         browser.find_by_name('finalize_appt').click()
#     else:
#         browser.find_by_name('e_id').click()
#         browser.find_by_value('4807').click() 

if browser.is_element_present_by_text('7:00pm'):
    book_it = browser.find_by_xpath("//td[. = '7:00pm']/following-sibling::td")
    book_it.find_by_value('Book it').click()
    browser.find_by_name('finalize_appt').click()

if browser.is_element_present_by_text('7:00pm') == False:
    browser.find_by_name('e_id').click()
    browser.find_by_value('5311').click()
    if browser.is_element_present_by_text('7:00pm'):
        book_it = browser.find_by_xpath("//td[. = '7:00pm']/following-sibling::td")
        book_it.find_by_value('Book it').click()
        browser.find_by_name('finalize_appt').click()
    else:
        browser.find_by_name('e_id').click()
        browser.find_by_value('4807').click() 

if browser.is_element_present_by_text('7:30pm'):
    book_it = browser.find_by_xpath("//td[. = '7:30pm']/following-sibling::td")
    book_it.find_by_value('Book it').click()
    browser.find_by_name('finalize_appt').click()

if browser.is_element_present_by_text('7:30pm') == False:
    browser.find_by_name('e_id').click()
    browser.find_by_value('5311').click()
    if browser.is_element_present_by_text('7:30pm'):
        book_it = browser.find_by_xpath("//td[. = '7:30pm']/following-sibling::td")
        book_it.find_by_value('Book it').click()
        browser.find_by_name('finalize_appt').click()
    else:
        browser.find_by_name('e_id').click()
        browser.find_by_value('4807').click() 

if browser.is_element_present_by_text('8:00pm'):
    book_it = browser.find_by_xpath("//td[. = '8:00pm']/following-sibling::td")
    book_it.find_by_value('Book it').click()
    browser.find_by_name('finalize_appt').click()

if browser.is_element_present_by_text('8:00pm') == False:
    browser.find_by_name('e_id').click()
    browser.find_by_value('5311').click()
    if browser.is_element_present_by_text('8:00pm'):
        book_it = browser.find_by_xpath("//td[. = '8:00pm']/following-sibling::td")
        book_it.find_by_value('Book it').click()
        browser.find_by_name('finalize_appt').click()
    
if browser.is_element_present_by_name('next'):
        browser.find_by_name('next').click()
else: print("no time available")

if browser.is_element_present_by_text('7:00pm'):
    book_it = browser.find_by_xpath("//td[. = '7:00pm']/following-sibling::td")
    book_it.find_by_value('Book it').click()
    browser.find_by_name('finalize_appt').click()

if browser.is_element_present_by_text('7:00pm') == False:
    browser.find_by_name('e_id').click()
    browser.find_by_value('5311').click()
    if browser.is_element_present_by_text('7:00pm'):
        book_it = browser.find_by_xpath("//td[. = '7:00pm']/following-sibling::td")
        book_it.find_by_value('Book it').click()
        browser.find_by_name('finalize_appt').click()
    else:
        browser.find_by_name('e_id').click()
        browser.find_by_value('4807').click() 

if browser.is_element_present_by_text('7:30pm'):
    book_it = browser.find_by_xpath("//td[. = '7:30pm']/following-sibling::td")
    book_it.find_by_value('Book it').click()
    browser.find_by_name('finalize_appt').click()

if browser.is_element_present_by_text('7:30pm') == False:
    browser.find_by_name('e_id').click()
    browser.find_by_value('5311').click()
    if browser.is_element_present_by_text('7:30pm'):
        book_it = browser.find_by_xpath("//td[. = '7:30pm']/following-sibling::td")
        book_it.find_by_value('Book it').click()
        browser.find_by_name('finalize_appt').click()
    else:
        browser.find_by_name('e_id').click()
        browser.find_by_value('4807').click() 

if browser.is_element_present_by_text('8:00pm'):
    book_it = browser.find_by_xpath("//td[. = '8:00pm']/following-sibling::td")
    book_it.find_by_value('Book it').click()
    browser.find_by_name('finalize_appt').click()

if browser.is_element_present_by_text('8:00pm') == False:
    browser.find_by_name('e_id').click()
    browser.find_by_value('5311').click()
    if browser.is_element_present_by_text('8:00pm'):
        book_it = browser.find_by_xpath("//td[. = '8:00pm']/following-sibling::td")
        book_it.find_by_value('Book it').click()
        browser.find_by_name('finalize_appt').click()
    
if browser.is_element_present_by_name('next'):
        browser.find_by_name('next').click()
else: print("no time available")


browser.quit


