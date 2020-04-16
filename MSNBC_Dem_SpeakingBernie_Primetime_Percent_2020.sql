Declare @FirstDate Date = '2019-01-01',@LastDate Date = GetDate();
With CTE AS (
Select FromDate From
(
Select Top (DateDiff(Day, @FirstDate, @LastDate) + 1)
    FromDate = DateAdd(Day, Row_Number() Over(Order By A.Object_Id) - 1,@FirstDate)
From Sys.All_Objects a
    Cross Join sys.All_Objects b
) Temp 
Where DateName(Weekday,FromDate) not in ('Saturday','Sunday')
)
Select FromDate As [Date],
		Coalesce(Summary.Bernie_Words,0) As Bernie_Words,
		Cast(100.*Coalesce(Summary.Bernie_Words,0)/Summary.All_Words As Numeric(5,2)) As Percent_Bernie_Speaking,
		Cast(100.*Coalesce(Summary.Biden_Words,0)/Summary.All_Words As Numeric(5,2)) As Percent_Biden_Speaking,
		Cast(100.*Coalesce(Summary.Bloomberg_Words,0)/Summary.All_Words As Numeric(5,2)) As Percent_Bloomberg_Speaking,
		Cast(100.*Coalesce(Summary.Warren_Words,0)/Summary.All_Words As Numeric(5,2)) As Percent_Warren_Speaking,
		Cast(100.*Coalesce(Summary.Pete_Words,0)/Summary.All_Words As Numeric(5,2)) As Percent_Pete_Speaking,
		Cast(100.*Coalesce(Summary.Kamala_Words,0)/Summary.All_Words As Numeric(5,2)) As Percent_Kamala_Speaking
	From CTE
			Left Outer Join
		(Select [Date],Sum(Bernie_Words) As Bernie_Words,Sum(Biden_Words) As Biden_Words,Sum(Warren_Words) As Warren_Words,Sum(Pete_Words) As Pete_Words,Sum(Bloomberg_Words) As Bloomberg_Words,Sum(Kamala_Words) As Kamala_Words,Sum(All_Words) As All_Words
			From (Select Cast(AiredOn As Date) As [Date],
						Case When Speaker In ('JUNIOR SEN. BERNIE SANDERS','BERNIE SANDERS','SEN BERNIE SANDERS','SEN. BERNIE SANDER','SEN.BERNIE SANDERS','SEN. BERNIE SANDERS','SENATOR BERNIE SANDERS') 
							Then 1 + Len([Text]) - Len(Replace([Text],' ',''))
							Else 0 
						End As Bernie_Words,
						Case When Speaker In ('FMR. SEN. JOE BIDEN','J. BIDEN','JOE BIDEN','JOE BIDEN. FORMER VICE PRESIDE','JOSEPH BIDEN','SEN. JOE BIDEN','THEN-SENATOR JOE BIDEN','VICE PRES. JOE BIDEN','VICE PRESIDENT JOSEPH BIDEN')
							Then 1 + Len([Text]) - Len(Replace([Text],' ',''))
							Else 0 
						End As Biden_Words,
						Case When Speaker In ('ELIZABETH WARREN','NONE:SEN.WARREN','PROF. ELIZABETH WARREN','PROFESSOR ELIZABETH WARREN','REP. ELIZABETH WARREN','SEN ELIZABETH WARREN','SEN. ELIZABETH WARREN','SEN. WARREN','SENATOR ELIZABETH WARREN')
							Then 1 + Len([Text]) - Len(Replace([Text],' ',''))
							Else 0 
						End As Warren_Words,
						Case When Speaker In ('FMR. MAYOR PETE BUTTIGIEG','MAYOR PETE BUTIGIEG','MAYOR PETE BUTTIGIEG','MAYOR PETER BUTTIGIEG','PETE BUTTIGIEG','PETER BUTTIGIEG','NONE:BUTTIEGIEG')
							Then 1 + Len([Text]) - Len(Replace([Text],' ',''))
							Else 0 
						End As Pete_Words,
						Case When Speaker In ('MICHAEL BLOOMBER','MICHAEL BLOOMBERG','MIKE BLOOMBERG','NONE:BLOOMBERG')
							Then 1 + Len([Text]) - Len(Replace([Text],' ',''))
							Else 0 
						End As Bloomberg_Words,
						Case When Speaker In ('KAMALA HARRIS','SEN. KAMAL HARRIS','SEN. KAMALA DEVI HARRIS','SEN. KAMALA HARRIS','SENATOR KAMALA HARRIS')
							Then 1 + Len([Text]) - Len(Replace([Text],' ',''))
							Else 0 
						End As Kamala_Words,
						1 + Len([Text]) - Len(Replace([Text],' ','')) As All_Words
					From Transcript 
					Where AiredOn >= '2019-01-01'
				) Temp 
			Group By [Date]
		) Summary
				On Summary.[Date]=CTE.FromDate
	Where DateName(Weekday, CTE.FromDate) Not In ('Saturday','Sunday') 
		And Summary.All_Words Is Not Null
	Order By 1
	Option (MaxRecursion 370)
Select Distinct Show,AiredOn From Transcript Where AiredOn Between '2019-01-01' And '2020-04-10'
/*
select * from Media_People 
	where name like '%amala%' 
	or name like '%kamal%' 
	or name like '%arris%'
	or name like '%harri%'
*/