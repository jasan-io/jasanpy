from jasanpy.lookup.lists import Lists
class Lookup:
    
    def list_example(self):
        ls = Lists()
        companies = ls.get_companies_by_keywords("TSLA")
        print(companies)
        # [{'symbol': 'TSLA', 'name': 'Tesla Inc', 'localName': 'Tesla Inc', 'market': 'NASDAQ'}]

if __name__ == "__main__":
    l = Lookup()
    l.list_example()