# Mainstream Media Negativity
 Analysis of transciptis of shows on the major networks: cable, broadcast network and radio
 
The code relies heavily on the features of SQL Server 2019 on Windows and its integration with python. Porting this to SQL Server on LINUX will be mostly harmless, but I can't help with LINUX issues.

Your first step is to read and follow the file Installation Steps.txt

The lone jpg here is the first significant results of this project. It came from the lone Excel file here, which came from the sql query MSNBC_Dem_Speaking_Time(Words).sql which queried the database of transcripts generated from get_transcripts.ipynb. This image counts the words (as a proxy for time) of each candidate as aired on MSNBC (whether as a videos of their talking or during an interview on MSNBC). The words come from converting the webpages on http://msnbc.com/transcripts to words (including some cleanup of typos, especially the names of who is talking) into data stored in a relational database. 

Much more is coming.
