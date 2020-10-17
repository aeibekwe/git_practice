import requests
# import os <-- this would be for writing to files...

# usage examples:
# payload = {'key1': 'value1', 'key2': 'value2', 'key3': ['value3', 'value4']} # 'payload' will pass the specified parameters into the URL
# r = requests.get('http://hts.usitc.gov/api', params=payload) # 'r' is a "Response Object", and I can pull information from this.

class URL:
    def __init__(self, url='http://hts.usitc.gov/api'):
        self.url = url

    def __repr__(self):
        return f'{self.__class__.__name__}: {self.url!r}'

    def search(self, query=None):
        s_payload = {'query': query}
        search = self.url + '/search'
        results = requests.get(search, params=s_payload)
        return results.text

    def export(self, format=None, start=None, end=None, styles='false'): # this is to export the results (w/in a range of HTS #s) to a particular format (json, csv, or excel)
        e_payload = {'format': format, 'from': start, 'to': end, 'styles': styles}
        export = self.url + '/export'
        content = requests.get(export, params=e_payload)
        return content

# hts = URL() # Made hts.usitc.gov the default url, so i don't have to type it in each time

class HTS_Search: # This is a class to handle search results from hts.search()... get the name for these classes as your queries
    def __init__(self, query):
        self.hts = URL() # defined this within this function to reduce the steps you need to take to get the results... also, allows you to call things like self.HTS_Search.hts.export() <-- might just make another function within this though to make this a bit more accessible...
        self.query = query
        self.search_results = self.hts.search(query)

    def __repr__(self):
        return f'{self.__class__.__name__} of {self.query!r} in {self.hts!r}'

    def results(self): # plug in your results from URL.search() here to get a more readable result with the HTS Code and its Description
        null = 0
        dict = eval(self.search_results)
        results_dict = dict.get("results")
        counter = 0
        results_list = []
        # Add some code here that will (over)write the results to a text file located in ./search_results
        print('\nResult No. XX  | HTS Code Number  |  Description\n')
        for i in results_dict:
            null = 0
            hts_no = i.get("htsno")
            description = i.get("description")
            x = (hts_no, description)
            results_list.append(x)
            print('\nResult No. {0}  |  {1}  |  {2}\n'.format(counter, hts_no, description))
            counter += 1
        return #results_list #return this in case you need to index through the results list.  the index number should be equal to the "Result No.  "