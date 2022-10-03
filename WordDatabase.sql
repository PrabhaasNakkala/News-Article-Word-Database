bulk insert hello.dbo.Stats
from 'C:\WebScrape\Database.txt'
with (
	fieldterminator = '',
	rowterminator = '\n'
)