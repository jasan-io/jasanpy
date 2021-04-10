import requests

class Lists:

    def get_companies_by_keywords(self, keyword):
        PARAMS = {'type': 'search', 'keyword': keyword}
        r = requests.get(url = f"https://api.jasan.io/v2/symbols", params = PARAMS)
        return r.json()
              
# if __name__ == "__main__":
#     l = Lists()
#     print(l.get_companies_by_keywords("TSLA"))

    

                
                