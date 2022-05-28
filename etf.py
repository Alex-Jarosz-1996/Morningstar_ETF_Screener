import pandas as pd

class WebScraper:
    def scrapeWebsite():
        """
        web scrapping data and arranging into a df
        """
        url = 'https://www.morningstar.com.au/ETFs/PerformanceTable'
        return pd.read_html(url)[0]

    def addHeaderNames(df):
        """
        providing df with header names
        """
        header_name = ["ASX_Code", "ETF_Name", "YTD_Return_%", "6_Month_Return_%", "1_Year_Return_%", "3_Year_Return_%",
                       "Add_to_Portfolio"]
        df.columns = header_name
        return df

    def removeExcess(df):
        """
        removing the: (1) first column, (2) last column, (3) converting all 'nan' obs to 0 and, (4) converting all '--'
        obs to 0
        """
        return df.iloc[1:].iloc[:, :-1].replace('NaN', 0).replace('--', 0)

    def forceColsAsTypeFloat(df):
        """
        force columns as appropriate data type
        """
        df[['ASX_Code', 'ETF_Name']] = df[['ASX_Code', 'ETF_Name']].astype(str)
        df[['YTD_Return_%', '6_Month_Return_%', '1_Year_Return_%', '3_Year_Return_%']] = df[
            ['YTD_Return_%', '6_Month_Return_%', '1_Year_Return_%', '3_Year_Return_%']].astype(float)
        return df

    def createDF():
        """
        creating entire df
        """
        scrapped_df = WebScraper.scrapeWebsite()
        new_df = WebScraper.addHeaderNames(scrapped_df)
        altered_df = WebScraper.removeExcess(new_df)
        return WebScraper.forceColsAsTypeFloat(altered_df)
