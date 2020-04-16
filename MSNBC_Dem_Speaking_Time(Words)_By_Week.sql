Select [Year-Week],
		Sum(Bernie_Words) As Bernie_Words,
		Cast(100.*Sum(Bernie_Words)/Sum(All_Words) As Numeric(5,2)) As Percent_Bernie_Speaking,
		Cast(100.*Sum(Biden_Words)/Sum(All_Words) As Numeric(5,2)) As Percent_Biden_Speaking,
		Cast(100.*Sum(Bloomberg_Words)/Sum(All_Words) As Numeric(5,2)) As Percent_Bloomberg_Speaking,
		Cast(100.*Sum(Warren_Words)/Sum(All_Words) As Numeric(5,2)) As Percent_Warren_Speaking,
		Cast(100.*Sum(Pete_Words)/Sum(All_Words) As Numeric(5,2)) As Percent_Pete_Speaking,
		Cast(100.*Sum(Kamala_Words)/Sum(All_Words) As Numeric(5,2)) As Percent_Kamala_Speaking
	From (Select Str(Year(AiredOn),4)+'-'+Replace(Str(DatePart(week,AiredOn),2),' ','0') As [Year-Week],
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
	Group By [Year-Week]
	Order By [Year-Week]