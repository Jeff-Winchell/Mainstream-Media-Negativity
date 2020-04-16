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
	[Name] VarChar(30) Not Null Constraint PK_Media_People Primary Key
	)
Go
Create Table Show(
	Show VarChar(40) Not Null Constraint PK_Show Primary Key,
	Network VarChar(5) Not Null Constraint CK_Network Check(Network In ('MSNBC','CNN','FN','NBC','CBS','ABC','NPR','PBS')),
	Host VarChar(30) Not Null Constraint FK_Show_Media_People Foreign Key References Media_People
	)
Go
Create Index Host On Show(Host)
Go
Create Table Episode (
	Show VarChar(40) Not Null Constraint FK_Episode_Show Foreign Key References Show,
	AiredOn DateTime Not Null,
	Guest_Host VarChar(30) Null Constraint FK_Episode_Media_People Foreign Key References Media_People,
	Constraint PK_Episode Primary Key(Show,AiredOn)
	)
Go
Create Index Show On Episode(Show)
Create Index Guest_Host On Episode(Guest_Host)
Go
Create Table Transcript (
	Id Int Not Null Identity Constraint PK_Transcript Primary Key,
	Show VarChar(40) Not Null,
	AiredOn DateTime Not Null,
	[Text] VarChar(Max) Collate LATIN1_GENERAL_100_CI_AS_SC_UTF8 Not Null,
	Speaker VarChar(30) Not Null Constraint FK_Speaker_Media_People Foreign Key References Media_People,
	Constraint FK_Transcript_Episode Foreign Key (Show,AiredOn) References Episode
	)
Create Index FK_Transcript_Episode On Transcript(Show,AiredOn)

Create FullText Index
	On Transcript(
		[Text] Language English Statistical_Semantics)
	Key Index PK_Transcript
Go
Alter Fulltext Index On Transcript Start Full Population;
Go
Create Or Alter Procedure Add_Transcript_Text(@Show VarChar(40),@AiredOn VarChar(19),@Speaker VarChar(30),@Text VarChar(Max))
As Begin
	If Not Exists(Select * From Media_People Where [Name]=@Speaker)
		Insert Into Media_People ([Name]) Values (@Speaker)
	If Not Exists(Select * From Episode Where Episode.Show=@Show And Episode.AiredOn=Convert(DateTime,@AiredOn,120))
		Insert Into Episode (Show,AiredOn) Values (@Show,@AiredOn)
	Insert Into Transcript (Show,AiredOn,Speaker,[Text]) Values (@Show,Convert(DateTime,@AiredOn,120),@Speaker,@Text)
End