import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


user_agent = UserAgent()
main_url = 'https://codingbat.com/java'
page = requests.get(main_url,headers={'user-agent':user_agent.chrome})
soup = BeautifulSoup(page.content,'lxml')

base_url = 'http://codingbat.com'

all_divs = soup.find_all('div',class_='summ')

all_links = [base_url + div.a['href'] for div in all_divs]

# above and below is line is equal in sence....

# for div in all_divs:
#     print(base_url + div.a['href'])
    # print(div.prettify())


for link in all_links:
	inner_page = requests.get(link,headers={'user-agent':user_agent.chrome})
	inner_soup = BeautifulSoup(inner_page.content,'lxml')    
	div = inner_soup.find('div',class_='tabc')
	# print(div.table.prettify())
	question_links = [base_url + td.a['href'] for td in div.table.find_all('td')]
	
	#up line is eqivalent to the below line...
	
	# for td in div.table.find_all('td'):
	# 	print(len(base_url + td.a['href']))
	# for question in question_url:
	# 	print(question)

	# break


	# 	examples = [sibling for sibling in test_statement if sibling.string is not None]
	# 	# print(problem_statement)
	# 	for example in examples:
	# 		print(example)


	# for question_link in question_links:
	# 	final_page = requests.get(question_link)
	# 	final_soup = BeautifulSoup(final_page.content,'lxml') 
	# 	minh_div = final_soup.find('div', attrs={'class':'minh'})
	# 	# problem_statement = indent_div.table.div.string
	# 	# problem_statement = indent_div.table.p.string
	# 	# print(problem_statement)
	# 	test_statement = minh_div.next_siblings

	# 	examples = [sibling for sibling in test_statement if sibling.string is not None]
	# 	print('test case is----->')
	# 	print(examples)
	# 	print('\n\n\n')
		# for example in examples:
		# 	print(example)


		


	 