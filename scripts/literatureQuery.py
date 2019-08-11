from crossref.restful import Works
import pandas as pd
import scholarly

"""
Perform the query based on a specific word
"""
def doQuery():
    # works = Works()
    # w1 = works.query(title='zika', author='johannes', publisher_name='Wiley-Blackwell')
    # for item in w1:
    #     print(item['title'])

    search_query = scholarly.search_pubs_query('wearable')
    print(next(search_query))

"""
Main function
"""
def main():
    doQuery()

#Just in case functions from this fild need to be imported
if __name__ == "__main__":
	main()
