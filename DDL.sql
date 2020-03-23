-- Check for enabling external scripts, openrowset, fulltext indexes,etc
Use Master
Go
Drop Database If Exists MSM
Go
Create Database MSM Collate LATIN1_GENERAL_100_CI_AS_SC_UTF8
Go
Use MSM
Go
Alter Database MSM Set Recovery Simple
Go
Create FullText Catalog MSM With Accent_Sensitivity = On As Default
Go
Create Table Media_People(
	[Name] VarChar(20) Not Null Constraint PK_Media_People Primary Key
	)
Go
Create Table Show(
	Show VarChar(30) Not Null Constraint PK_Show Primary Key,
	Network VarChar(5) Not Null Constraint CK_Network Check(Network In ('MSNBC','CNN','FN','NBC','CBS','ABC','NPR','PBS')),
	Host VarChar(20) Not Null Constraint FK_Show_Media_People Foreign Key References Media_People
	)
Go
Create Index Host On Show(Host)
Go
Create Table Transcript (
	Id Int Not Null Constraint PK_Transcript Primary Key,
	[Text] VarChar(Max) Collate LATIN1_GENERAL_100_CI_AS_SC_UTF8 Not Null,
	Show VarChar(30) Not Null Constraint FK_Transcript_Show Foreign Key References Show,
	AiredOn DateTimeOffset(0) Not Null,
	Guest_Host VarChar(20) Null Constraint FK_Transcript_Media_People Foreign Key References Media_People,
	Constraint U_Transcript Unique(Show,AiredOn)
	)
Go
Create Index Show On Transcript(Show)
Create Index Guest_Host On Transcript(Guest_Host)
Create FullText Index
	On Transcript(
		[Text] Language English Statistical_Semantics)
	Key Index PK_Transcript
Go
Alter Fulltext Index On Transcript Start Full Population;
Go
