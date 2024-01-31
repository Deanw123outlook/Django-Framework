# install package if required
pip install pyodbc

# import packages
import pyodbc 
import pandas as pd # Enables SQL table to be imported as CSV file into JupyterNotebook

# connect db setup
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-xxxxxx\SQLEXPRESS;'
                      'Database=AdventureWorksLT2008R2;'
                      'Trusted_Connection=yes;')

# read sql query to pandas dataframe                  
data = pd.read_sql_query('SELECT t1.[FixtureId],t4.[Name] AS "HomeTeam",t4.[TeamId],t5.[Name] AS "AwayTeam",t5.[TeamId], t1.[LeagueId],t2.[MasterSource], t2.[EndDate] AS [LeagueEndDate],t2.[CompetitionId],t3.[Name] AS "CompetitionName",t2.[Active] AS [CompetitonLeagueActive],t1.[StartTimeUTC],t1.[FeedProviderId],t1.[Set],t1.StartTimeUpdates] FROM [database_name].[dbo].[Fixture] AS t1 FULL OUTER JOIN [database_name].[dbo].[League] AS t2 ON t1.LeagueId = t2.LeagueId FULL OUTER JOIN [database_name].[dbo].[Competition] AS t3 ON t2.CompetitionId = t3.CompetitionId FULL OUTER JOIN [database_name].[dbo].[Team] AS t4 ON t1.HomeTeamId = t4.TeamId 
FULL OUTER JOIN [database_name].[dbo].[Team] AS t5 ON t1.AwayTeamId = t5.TeamId WHERE t1.[StartTimeUTC] BETWEEN '2024-01-31 00:00:00.000' AND '2024-02-04 00:00:00.000' AND t1.[LeagueId] = 1000  ORDER BY t1.[StartTimeUTC];', conn)

# display dataframe
data
