import pandas as pd
from dagster import asset, get_dagster_logger

@asset
def df_site() -> None: 
# assign data of lists. 
    df = pd.read_csv("df_site.csv")
    print(df)
#    data = {'name': ['hello', 'world'], 'url': ["http://hello.com/home", "https://world.org/"]}
# Create DataFrame
#    df = pd.DataFrame(data)
    df['domain_of_url'] = df['url'].map(lambda x: str(x).partition("://")[2].partition("/")[0])
    print(df)
    df.to_csv('df_new_site.csv')
