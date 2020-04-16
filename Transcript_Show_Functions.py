def RACHEL_MADDOW_SHOW_Fix(text,AiredOn):
    if text.startswith('MEGAN TWOHEY, INVESTIGATIVE REPORTER, The NEW YORK TIMES:'):
        text=text.replace('The','THE')
    elif (text.startswith('THE RACHEL MADDOW SHOW starts right now.') and AiredOn.date() ==datetime.date(2019,12,11)) \
        or (text.startswith('THE RACHEL MADDOW SHOW starts now.') and AiredOn.date()==datetime.date(2015,5,1)):
        text='CHRIS HAYES'+text
    return text
def THE_LAST_WORD_Fix(text,AiredOn):
    return text
def MSNBC_LIVE_Fix(text,AiredOn):
    return text
def THE_BEAT_WITH_ARI_MELBER_Fix(text,AiredOn):
    return text
def THE_11TH_HOUR_WITH_BRIAN_WILLIAMS_Fix(text,AiredOn):
    if text.startswith('SEN, MICHAEL BENNET, (D) COLORADO, CANDIDATE FOR PRESIDENT'):
        text=text.replace('SEN,','SEN.')
    elif text.startswith('MAYOR, FRANCIS SUAREZ, (R) MIAMI'):
        text=text.replace('MAYOR,','MAYOR')
    return text


def HARDBALL_Fix(text,AiredOn):
    if text.startswith('ROBERT GIBBS, FMR. WHITE hOUSE PRESS SECRETARY, MSNBC CONTRIBUTOR:'):
        text=text.replace('hOUSE','HOUSE')
    elif text.startswith('JESSICA STERN, AUTHOR, “ISIS, The STATE OF TERROR”:'):
        text=text.replace('The','THE')
    return text

def ALL_IN_Fix(text,AiredOn):
    if AiredOn.date()==datetime.date(2015,12,18) and text.startswith('JOAN WALSH.'):
        text=text.replace('JOAN WALSH.','JOAN WALSH,')
    elif text.startswith('“JOHN MILLER”'):
        text=text.replace('“JOHN MILLER”','JOHN MILLER')
    elif text.startswith('NICK AKERMAN MSNBC LEGAL ANALYST:'):
        text=text.replace('NICK AKERMAN MSNBC','NICK AKERMAN, MSNBC')
    elif text.startswith('DANIELLE MOODIE MILLS, HOST, DEMOCRACY-ISH:'):
        text=text.replace('MOODIE MILLS','MOODIE-MILLS')
    elif text.startswith('FRANK, FIGLIUZZI MSNBC NATIONAL:'):
        text=text.replace('FRANK, FIGLIUZZI','FRANK FIGLIUZZI,')
    elif text.startswith('BARBARA, BOXER, FORMER SENATOR FROM CALIFORNIA:'):
        text=text.replace('BARBARA, BOXER,','BARBARA BOXER,')
    elif text.startswith('DAVID CORN,WASHINGTON BUREAU CHIEF, MOTHER JONES:'):
        text=text.replace('DAVID CORN,WASHINGTON','DAVID CORN, WASHINGTON')
    elif text.startswith('BRIAN SCHATZ UNITED STATES SENATOR FROM HAWAII:'):
        text=text.replace('BRIAN SCHATZ UNITED','BRIAN SCHATZ, UNITED')
    elif text.startswith('KATRINA VANDENHEUVEL'):
        text=text.replace('VANDENHEUVEL','VANDEN HEUVEL')
    elif text.startswith('ANNE WEISMANN,CHEIF FOIA COUNCIL:'):
        text=text.replace('ANNE WEISMANN,CHEIF','ANNE WEISMANN, CHIEF')
    elif text.startswith('WILLIAM WELD, (Lib) VICE PRESIDENTIAL CANDIDATE:'):
        text=text.replace('WILLIAM WELD, (Lib)','WILLIAM WELD, (LIB)')
    elif text.startswith('SARI, HORWITZ, THE WASHINGTON POST REPORTER:'):
        text=text.replace('SARI, HORWITZ,','SARI HORWITZ,')
    elif text.startswith('WENDY SHERMAN MSNBC GLOBAL AFFAIRS CONTRIBUTOR: '):
        text=text.replace('WENDY SHERMAN MSNBC','WENDY SHERMAN, MSNBC')
    elif text.startswith('PRICEY, HARRISON, NORTH CAROLINA STATE REPRESENTATIVE:'):
        text=text.replace('PRICEY, HARRISON, NORTH','PRICEY HARRISON, NORTH')
    elif text.startswith('ANNA CALLAND, MOVEON.ORG:'):
        text=text.replace('ANNA CALLAND, MOVEON.ORG:','ANNA GALLAND, MOVEON.ORG:')
    elif text.startswith('SCOTT: Or is looking forward'):
        text=text.replace('SCOTT:','UNIDENTIFIED FEMALE:')
    elif text.startswith('SCOTT PELLEY CORRESPONDENT CBS NEWS:'):
        text=text.replace('SCOTT PELLEY ','SCOTT PELLEY, ')
    elif text.startswith('JOSE DIAZ BALART, MSNBC:'):
        text=text.replace('DIAZ BALART','DIAZ-BALART')
    elif text.startswith('MAGGIE SANDROCK (ph):'):
        text=text.replace('MAGGIE SANDROCK (ph):','MAGGIE SANDROCK:')
    elif text.startswith('MAGGIE SANCROCK (ph):'):
        text=text.replace('SANCROCK (ph):','MAGGIE SANDROCK:')
    elif text.startswith('JULIA AINSLEY, NBC News National Security and'):
        text=text.replace('JULIA AINSLEY, NBC News National Security and','JULIA AINSLEY, NBC NEWS NATIONAL SECURITY AND')
    elif text.startswith('NICK, CONFESSORE'):
        text=text.replace('NICK, CONFESSORE','NICK CONFESSORE,')
    elif text.startswith('EZEKIEL, EMANUEL'):
        text=text.replace('EZEKIEL, EMANUEL','EZEKIEL EMANUEL')
    elif text.startswith('FRANK, FIGLIUZZI '):
        text=text.replace('FRANK, FIGLIUZZI ','FRANK FIGLIUZZI, ')
    elif text.startswith('DANIELLE MOODY-MILLS,'):
        text=text.replace('MOODY','MOODIE')
    elif text.startswith('AISHA MOODY MILLS,'):
        text=text.replace('MOODY MILLS','MOODIE-MILLS')
    elif text.startswith('AMANDO CHAVZ'):
        text=text.replace('AMANDO CHAVZ','ARMANDO CHAVEZ')
    elif text.startswith('MANUEL RANDON (ph)') or text.startswith('REBA HOENIGER (ph)')  or text.startswith('SANCROCK (ph)') or text.startswith('HOENIGER (ph)'):
        text=text.replace(' (ph)','')
    elif text.startswith('CLAIRE FINKELSTEIN UNIVERSITY OF PENNSYLVANIA LAW PROFESSOR:'):
        text=text.replace('CLAIRE FINKELSTEIN ','CLAIRE FINKELSTEIN, ')
    elif text.startswith('MINE JUSTICE, MOTHER:'):
        text=text.replace('MINE','MINA')
    elif text.startswith('REP. TAMMY DUCKWORK, (D-IL) CANDIDATE FOR SENATE:'):
        text=text.replace('DUCKWORK','DUCKWORTH')
    elif text.startswith('ARMSTRONG WILLAMS, BEN CARSON CAMPAIGN:'):
        text=text.replace('WILLAMS','WILLIAMS')
    elif text.startswith('REP, CHARLIE DENT (R), PENNSYLVANIA:'):
        text=text.replace('REP,','REP.')
    elif text.startswith('CHRIS AND LAUREN CLAROS, COLUMBUS, OHIO:'):
        text=text.replace('COLUMBUS, OHIO','COLUMBUS OHIO')
    return text

def RACHEL_MADDOW_SHOW_Last_Name_Fix(last_name,AiredOn):
    return last_name
def THE_LAST_WORD_Last_Name_Fix(last_name,AiredOn):
    return last_name
def MSNBC_LIVE_Last_Name_Fix(last_name,AiredOn):
    return last_name
def THE_11TH_HOUR_WITH_BRIAN_WILLIAMS_Last_Name_Fix(last_name,AiredOn):
    return last_name
def THE_BEAT_WITH_ARI_MELBER_Last_Name_Fix(last_name,AiredOn):
    return last_name

def HARDBALL_Last_Name_Fix(last_name,AiredOn):
    if last_name=='SCOTT' and AiredOn.date()==datetime.date(2015,1,2):
        last_name='SCOTTO'
    elif last_name=='PERRY' and AiredOn.date()==datetime.date(2015,2,4):
        last_name='BACON'
    elif last_name=='ALLAN' and AiredOn.date()==datetime.date(2015,3,3):
        last_name='ALLEN'
    elif last_name=='BRENNAN' and AiredOn.date()==datetime.date(2015,5,11):
        last_name='BERNARD'
    elif last_name=='BLITZER' and AiredOn.date()==datetime.date(2015,5,19):
        last_name='MATTHEWS'
    elif last_name=='FINEMAN' and AiredOn.date() == datetime.date(2016,3,31):
        last_name='TRUMP'
    elif last_name=='FINEMAN' and AiredOn.date() == datetime.date(2016,8,2):
        last_name='DENT'
    elif last_name=='FINEMAN' and AiredOn.date() == datetime.date(2017,1,13):
        last_name='MARCUS'
    elif last_name=='FINEMAN' and AiredOn.date() in [datetime.date(2015,7,2),datetime.date(2016,1,25)]:
        last_name='MATTHEWS'
    elif last_name=='PICKER' and AiredOn.date() in [datetime.date(2015,4,3),datetime.date(2015,5,5)]:
        last_name='PICKLER'
    return last_name

def ALL_IN_Last_Name_Fix(last_name,AiredOn):
    if last_name=='CHRIS' and AiredOn.date()==datetime.date(2020,2,12):
        last_name='HAYES'
    elif last_name=='CORTEZ' and AiredOn.date() in [datetime.date(2018,7,24),datetime.date(2018,10,5),
        datetime.date(2018,11,14),datetime.date(2019,1,16),datetime.date(2019,3,5)]:
        last_name='OCASIO-CORTEZ'
    elif last_name=='ANDERSON' and AiredOn.date() in [datetime.date(2016,6,30),datetime.date(2016,10,6),datetime.date(2017,2,14),datetime.date(2017,6,9)]:
        last_name='HAYES'
    elif last_name=='TAPPER' and AiredOn.date() ==datetime.date(2016,11,17):
        last_name='HAYES'
    elif last_name=='GODDARD' and AiredOn.date() ==datetime.date(2015,9,29):
        last_name='STODDARD'
    elif last_name=='MCDANIELS' and AiredOn.date() ==datetime.date(2015,2,18):
        last_name='MCDANIEL'
    elif last_name=='HENRY' and AiredOn.date() ==datetime.date(2016,8,23):
        last_name='JONES'
    elif last_name=='AKERMAN' and AiredOn.date() ==datetime.date(2015,2,24):
        last_name='ACKERMAN'
    elif last_name=='WILDERSON' and AiredOn.date() ==datetime.date(2015,3,4):
        last_name='WILKERSON'
    elif last_name=='ACKERMAN' and AiredOn.date() in [datetime.date(2018,4,9),datetime.date(2018,5,2)]:
        last_name='AKERMAN'
    elif last_name=='SAH' and AiredOn.date() ==datetime.date(2015,7,10):
        last_name='SHAH'
    elif last_name=='STEWARD' and AiredOn.date() ==datetime.date(2015,2,11):
        last_name='STEWART'
    elif last_name=='LUCY' and AiredOn.date() ==datetime.date(2017,6,12):
        last_name='PANZA'
    elif last_name=='DALEY' and AiredOn.date() ==datetime.date(2017,5,26):
        last_name='DALY'
    elif last_name=='CHAMBER' and AiredOn.date() ==datetime.date(2017,12,13):
        last_name='CHAMBERS'
    elif last_name=='GOODARD' and AiredOn.date() ==datetime.date(2015,8,26):
        last_name='GODDARD'
    elif last_name=='MILLER' and AiredOn.date() in [datetime.date(2016,5,13)]:
        last_name='TRUMP'
    elif last_name=='MEYER' and AiredOn.date() in [datetime.date(2018,8,8)]:
        last_name='MEYERS'
    elif last_name=='JOHNSON' and AiredOn.date() in [datetime.date(2015,8,31)]:
        last_name='JOHNSTON'
    elif last_name=='MCCARTNEY' and AiredOn.date() in [datetime.date(2015,6,5)]:
        last_name='MCCARTHY'
    elif last_name=='O`NIELL' and AiredOn.date() in [datetime.date(2015,4,16),datetime.date(2015,8,4)]:
        last_name='O`NEILL'

    elif last_name=='JEFFER' and AiredOn.date() in [datetime.date(2015,5,7)]:
        last_name='JAFFER'
    elif last_name=='FALLOW' and AiredOn.date() in [datetime.date(2015,3,30)]:
        last_name='FALLON'
    elif last_name=='CAUDLEY' and AiredOn.date() in [datetime.date(2015,3,30)]:
        last_name='CAULEY'
    elif last_name=='RASON' and AiredOn.date() in [datetime.date(2015,3,30)]:
        last_name='RASCON'
    elif last_name=='COST' and AiredOn.date() in [datetime.date(2017,8,9)]:
        last_name='COSTA'
    elif last_name=='NIESEN' and AiredOn.date() in [datetime.date(2019,4,10)]:
        last_name='NIELSEN'
    elif last_name=='O`MEARA' and AiredOn.date() in [datetime.date(2019,10,14)]:
        last_name='OMERO'
    elif last_name=='FITZGERALD' and AiredOn.date() in [datetime.date(2018,3,6)]:
        last_name='FITZPATRICK'
    elif last_name=='PAUL' and AiredOn.date() in [datetime.date(2016,4,12)]:
        last_name='RYAN'
    elif last_name=='TUCKER' and AiredOn.date() in [datetime.date(2019,2,22)]:
        last_name='CARLSON'
    elif last_name=='KENNEY' and AiredOn.date() in [datetime.date(2015,9,22)]:
        last_name='KENNEDY'
    elif last_name=='STEYERS' and AiredOn.date() in [datetime.date(2015,9,28)]:
        last_name='STEYER'
    elif last_name=='THOMAS' and AiredOn.date() in [datetime.date(2015,8,7)]:
        last_name='ROBERTS'
    elif last_name=='DALE' and AiredOn.date()==datetime.date(2017,10,31):
        last_name='DALY'
    elif last_name=='MILLS' and AiredOn.date()==datetime.date(2018,11,2):
        last_name='MOODIE-MILLS'
    elif last_name=='BOEHLER' and AiredOn.date()==datetime.date(2015,4,23):
        last_name='BOEHLERT'
    elif last_name=='SWAINE' and AiredOn.date()==datetime.date(2015,4,23):
        last_name='SWAIN'
    elif last_name=='CLINT' and AiredOn.date()==datetime.date(2016,1,18):
        last_name='CLINTON'
    elif last_name=='HADLEY' and AiredOn.date()==datetime.date(2018,6,28):
        last_name='NADLER'
    elif last_name=='DAVID' and AiredOn.date() in [datetime.date(2017,7,14),datetime.date(2018,5,25)]:
        last_name='DAVIDSON'
    elif last_name=='PIERRE' and AiredOn.date() in [datetime.date(2017,12,7),datetime.date(2018,6,26)]:
        last_name='JEAN-PIERRE'
    elif last_name=='ROY' and AiredOn.date()==datetime.date(2019,3,1):
        last_name='NORMAN'
    elif last_name=='RUSSELL' and AiredOn.date()==datetime.date(2017,8,24):
        last_name='WALKER'
    elif last_name=='RICK' and AiredOn.date()==datetime.date(2016,4,6):
        last_name='SCOTT'
    elif last_name=='LEVY' and AiredOn.date()==datetime.date(2018,10,15):
        last_name='EDWARDS-LEVY'
    elif last_name=='JILL' and AiredOn.date()==datetime.date(2018,10,11):
        last_name='WINE-BANKS'
    elif last_name=='MCKAY' and AiredOn.date()==datetime.date(2015,12,17):
        last_name='COPPINS'
    elif last_name=='HECTOR' and AiredOn.date()==datetime.date(2015,9,14):
        last_name='RANDON'
    elif last_name=='BROWN' and AiredOn.date()==datetime.date(2015,12,30):
        last_name='BROWNE'
    elif last_name=='REED' and AiredOn.date()==datetime.date(2015,3,31):
        last_name='REID'
    elif last_name=='SHULTZ' and AiredOn.date()==datetime.date(2015,9,16):
        last_name='SCHULTZ'
    elif last_name=='CARTER' and AiredOn.date()==datetime.date(2017,11,7):
        last_name='PAGE'
    elif last_name=='WITTMAN' and AiredOn.date()==datetime.date(2016,2,29):
        last_name='WHITMAN'
    elif last_name=='WELL' and AiredOn.date()==datetime.date(2019,3,7):
        last_name='SWALWELL'
    elif last_name=='HAWKS' and AiredOn.date()==datetime.date(2018,9,12):
        last_name='HAWK'
    elif last_name=='WELSH' and AiredOn.date()==datetime.date(2015,12,23):
        last_name='WELCH'
    elif last_name=='BOWE' and AiredOn.date()==datetime.date(2017,8,18):
        last_name='WOODRUFF'
    elif last_name=='BOWE' and AiredOn.date()==datetime.date(2018,3,23):
        last_name='HOWE'
    elif last_name=='KING' and AiredOn.date()==datetime.date(2016,8,19):
        last_name='KINGSTON'
    elif last_name=='GREEN' and AiredOn.date()==datetime.date(2018,7,10):
        last_name='GREENE'
    elif last_name=='GOLDMAN' and AiredOn.date()==datetime.date(2018,9,26):
        last_name='GOLDBERG'
    elif last_name=='CATES' and AiredOn.date()==datetime.date(2015,7,14):
        last_name='COATES'
    elif last_name=='ARTHUR' and AiredOn.date()==datetime.date(2017,3,27):
        last_name='SCHMIDT'
    elif last_name=='ANGUS' and AiredOn.date()==datetime.date(2017,6,13):
        last_name='KING'
    elif last_name=='LEONARD' and AiredOn.date()==datetime.date(2017,6,14):
        last_name='LANCE'
    elif last_name=='BRUCE' and AiredOn.date()==datetime.date(2016,4,27):
        last_name='REDDEN'
    elif last_name=='EDWARD' and AiredOn.date()==datetime.date(2016,10,24):
        last_name='EDWARDS'
    elif last_name=='WALTER' and AiredOn.date()==datetime.date(2015,8,3):
        last_name='ALTER'
    elif last_name=='SISA' and AiredOn.date()==datetime.date(2015,7,24):
        last_name='SISKA'
    elif last_name=='RICHARD' and AiredOn.date()==datetime.date(2019,5,31):
        last_name='RICHARDS'
    elif last_name=='MANUEL' and AiredOn.date()==datetime.date(2015,3,9):
        last_name='MIRANDA'
    elif last_name=='BELL' and AiredOn.date()==datetime.date(2016,8,30):
        last_name='BALL'
    elif last_name=='WEINTER' and AiredOn.date()==datetime.date(2015,10,8):
        last_name='WEINER'
    elif last_name=='CAMBELL' and AiredOn.date()==datetime.date(2015,10,6):
        last_name='CAMPBELL'
    elif last_name=='CLEMENTS' and AiredOn.date()==datetime.date(2018,4,4):
        last_name='CLEMENT'
    elif last_name=='PEARCE' and AiredOn.date()==datetime.date(2015,7,15):
        last_name='PIERCE'
    elif last_name=='POLICE' and AiredOn.date()==datetime.date(2015,7,22):
        last_name='OFFICER'
    elif last_name=='CARTWRIGHT' and AiredOn.date()==datetime.date(2016,3,17):
        last_name='MCCARTHY'
    elif last_name=='BARBARA' and AiredOn.date()==datetime.date(2018,6,22):
        last_name='MCQUADE'
    elif last_name=='LEVINE' and AiredOn.date()==datetime.date(2018,2,13):
        last_name='LEMIRE'
    elif last_name=='COATS' and AiredOn.date()==datetime.date(2017,9,15):
        last_name='COATES'
    elif last_name=='JEB' and AiredOn.date()==datetime.date(2016,3,14):
        last_name='LUND'
    elif last_name=='GOLDMAN' and AiredOn.date() in [datetime.date(2019,9,23),datetime.date(2019,11,19)]:
        last_name='GOLDBERG'
    elif last_name=='MILLS' and AiredOn.date() in [datetime.date(2019,1,7),datetime.date(2019,6,17)]:
        last_name='MOODIE-MILLS'
    return last_name

def THE_LAST_WORD_Fix_Speakers(last_name,AiredOn,Speakers):
    return Speakers,True
def MSNBC_LIVE_Fix_Speakers(last_name,AiredOn,Speakers):
    return Speakers,True
def THE_11TH_HOUR_WITH_BRIAN_WILLIAMS_Fix_Speakers(last_name,AiredOn,Speakers):
    return Speakers,True
def THE_BEAT_WITH_ARI_MELBER_Fix_Speakers(last_name,AiredOn,Speakers):
    if last_name=='SANDERS' and AiredOn.date()==datetime.date(2019,4,16):
        Speakers[last_name]='SEN. BERNIE SANDERS'
    return Speakers,True

def RACHEL_MADDOW_SHOW_Fix_Speakers(last_name,AiredOn,Speakers):
    return Speakers,True

def HARDBALL_Fix_Speakers(last_name,AiredOn,Speakers):
    if last_name=='MADISON' and AiredOn.date()==datetime.date(2015,1,21):
        Speakers[last_name]='JOE MADISON'
    elif last_name=='TERKEL' and AiredOn.date()==datetime.date(2015,1,21):
        Speakers[last_name]='AMANDA TERKEL'
    elif last_name=='KNOWLES' and AiredOn.date()==datetime.date(2015,3,11):
        Speakers[last_name]='JAMES KNOWLES'
    elif last_name=='STEIN' and AiredOn.date()==datetime.date(2015,3,13):
        Speakers[last_name]='SAM STEIN'
    elif last_name=='BERNARD' and AiredOn.date()==datetime.date(2015,4,2):
        Speakers[last_name]='MICHELLE BERNARD'
    elif last_name=='ROBINSON' and AiredOn.date()==datetime.date(2015,6,23):
        Speakers[last_name]='EUGENE ROBINSON'
    elif last_name=='KOHLMANN' and AiredOn.date()==datetime.date(2015,5,7):
        Speakers[last_name]='EVAN KOHLMANN'
    elif last_name=='BUSH' and AiredOn.date() in [datetime.date(2015,5,15),datetime.date(2015,6,17)]:
        Speakers[last_name]='JEB BUSH'
    elif last_name=='FINEMAN' and AiredOn.date() in [datetime.date(2015,6,10),datetime.date(2017,10,25)]:
        Speakers[last_name]='HOWARD FINEMAN'
    elif last_name=='BRAD' and AiredOn.date()==datetime.date(2015,5,7):
        Speakers[last_name]=last_name
    elif last_name in ['TIMON','PUMBAA'] and AiredOn.date()==datetime.date(2015,5,26):
        Speakers[last_name]=last_name
    return Speakers,True

def ALL_IN_Fix_Speakers(last_name,AiredOn,Speakers):
    orig_Speakers_len=len(Speakers)
    if last_name=='AKERMAN' and AiredOn.date() in [datetime.date(2017,9,21),datetime.date(2018,5,2)]:
        Speakers[last_name]="NICK AKERMAN"
    elif last_name=='LUCY' and AiredOn.date()==datetime.date(2017,6,12):
        Speakers[last_name]="LUCY PANZA"
    elif last_name=='MOORE' and AiredOn.date()==datetime.date(2017,11,29):
        Speakers[last_name]="ROY MOORE"
    elif last_name=='CASTRO' and AiredOn.date()==datetime.date(2019,7,1):
        Speakers[last_name]='JOAQUIN CASTRO'
    elif last_name=='WARREN' and AiredOn.date()==datetime.date(2019,9,18):
        Speakers[last_name]="SEN. ELIZABETH WARREN"
    elif last_name=='CHAFETZ' and AiredOn.date()==datetime.date(2017,4,25):
        Speakers[last_name]="REP. JASON CHAFETZ"
    elif last_name=='GUPTA' and AiredOn.date()==datetime.date(2018,6,28):
        Speakers[last_name]="VANITA GUPTA"
    elif last_name=='RANGEL' and AiredOn.date()==datetime.date(2015,8,7):
        Speakers[last_name]="CHARLIE RANGEL"
    elif last_name=='EMMANUEL' and AiredOn.date()==datetime.date(2015,8,7):
        Speakers[last_name]='RAHM EMMANUEL'
    elif last_name=='KERRY' and AiredOn.date()==datetime.date(2015,8,7):
        Speakers[last_name]='JOHN KERRY'
    elif last_name=='BLITZER' and AiredOn.date()==datetime.date(2015,8,7):
        Speakers[last_name]='WOLF BLITZER'
    elif last_name=='FARENTHOLD' and AiredOn.date()==datetime.date(2016,6,22):
        Speakers[last_name]="DAVID FARENTHOLD"
    elif last_name=='MOORE' and AiredOn.date()==datetime.date(2019,5,1):
        Speakers[last_name]="STEPHEN MOORE"
    elif last_name=='SCHMIDT' and AiredOn.date()==datetime.date(2017,3,27):
        Speakers[last_name]='MICHAEL SCHMIDT'
    elif last_name=='BUSH' and AiredOn.date() in [datetime.date(2015,9,2),datetime.date(2015,8,7),
                                                  datetime.date(2015,10,20)]:
        Speakers[last_name]='JEB BUSH'
    elif last_name=='EARHARDT' and AiredOn.date()==datetime.date(2017,4,21):
        Speakers[last_name]='AINSLEY EARHARDT'
    elif last_name=='DEAN' and AiredOn.date()==datetime.date(2017,10,31):
        Speakers[last_name]="JONATHAN DEAN"
    elif last_name=='PERRY' and AiredOn.date()==datetime.date(2015,9,3):
        Speakers[last_name]='RICK PERRY'
    elif last_name=='WOLF' and AiredOn.date()==datetime.date(2018,6,13):
        Speakers[last_name]="LEON WOLF"
    elif last_name=='PAGE' and AiredOn.date()==datetime.date(2017,11,7):
        Speakers[last_name]="CARTER PAGE"
    elif last_name=="MILLER" and AiredOn.date()==datetime.date(2019,5,14):
        Speakers[last_name]="MATT MILLER"
    elif last_name=="PRICE" and AiredOn.date()==datetime.date(2018,4,23):
        Speakers[last_name]="NED PRICE"
    elif last_name=="REDDEN" and AiredOn.date()==datetime.date(2016,4,27):
        Speakers[last_name]='BRUCE REDDEN'
    elif last_name=="MCCARTHY" and AiredOn.date()==datetime.date(2016,3,17):
        Speakers[last_name]="GINA MCCARTHY"
    elif last_name=='TODD' and AiredOn.date()==datetime.date(2015,9,21):
        Speakers[last_name]='CHUCK TODD'
    elif last_name=='O`NEILL' and AiredOn.date()==datetime.date(2017,4,21):
        Speakers[last_name]='JAMES O`NEILL'
    elif last_name=='GARZA' and AiredOn.date()==datetime.date(2015,8,13):
        Speakers[last_name]='ALICIA GARZA'
    elif last_name=='BROWN' and AiredOn.date()==datetime.date(2015,3,23):
        Speakers[last_name]='GOV. JERRY BROWN'
    elif last_name=="STAPLES" and AiredOn.date()==datetime.date(2019,6,5):
        Speakers[last_name]="FRANK STAPLES"
    elif last_name=="NORMAN" and AiredOn.date()==datetime.date(2019,3,1):
        Speakers[last_name]="RALPH NORMAN"
    elif last_name=='KEILAR' and AiredOn.date()==datetime.date(2015,3,9):
        Speakers[last_name]='BRIANNA KEILAR'
    elif last_name=="JONES" and AiredOn.date()==datetime.date(2016,8,23):
        Speakers[last_name]="HENRY JONES"
    elif last_name=="WHITMAN" and AiredOn.date()==datetime.date(2016,2,29):
        Speakers[last_name]="CHRISTINE TODD WHITMAN"
    elif last_name=='DEAN' and AiredOn.date()==datetime.date(2015,12,18):
        Speakers[last_name]="HOWARD DEAN"
    elif last_name=='COATS' and AiredOn.date()==datetime.date(2017,6,7):
        Speakers[last_name]="DAN COATS"
    elif last_name=='STAHL' and AiredOn.date() in [datetime.date(2016,11,16)]:
        Speakers[last_name]="LESLIE STAHL"
    elif last_name=='WALKER' and AiredOn.date()==datetime.date(2015,2,17):
        Speakers[last_name]="SCOTT WALKER"
    elif last_name=='SIEGFRIED' and AiredOn.date()==datetime.date(2019,11,1):
        Speakers[last_name]="EVANS SIEGFRIED"
    elif last_name=='PETERS' and AiredOn.date()==datetime.date(2017,7,28):
        Speakers[last_name]="GARY PETERS"
    elif last_name=='LEE' and AiredOn.date() in [datetime.date(2018,9,12),datetime.date(2015,4,8)]:
        Speakers[last_name]='TRYMAINE LEE'
    elif last_name=='OSBOURNE' and AiredOn.date()==datetime.date(2015,7,30):
        Speakers[last_name]='STEVE OSBOURNE'
    elif last_name=='O`MALLEY' and AiredOn.date()==datetime.date(2015,7,20):
        Speakers[last_name]='MARTIN O`MALLEY'
    elif last_name=='SOMMER' and AiredOn.date()==datetime.date(2018,8,1):
        Speakers[last_name]="WILL SOMMER"
    elif last_name=='JOLLY' and AiredOn.date()==datetime.date(2018,11,9):
        Speakers[last_name]='DAVID JOLLY'
    elif last_name=='BARKAN' and AiredOn.date()==datetime.date(2019,4,30):
        Speakers[last_name]="ADY BARKAN"
    elif last_name=='GREEN' and AiredOn.date() in [datetime.date(2018,5,1)]:
        Speakers[last_name]='LISA GREEN'
    elif last_name=='CORSI' and AiredOn.date() in [datetime.date(2018,11,28)]:
        Speakers[last_name]='GEROME CORSI'
    elif last_name=='CRUZ' and AiredOn.date() in [datetime.date(2015,8,26),datetime.date(2016,2,26),
                                                  datetime.date(2016,4,13)]:
        Speakers[last_name]="TED CRUZ"
    elif last_name=='GOLDBERG' and AiredOn.date() in [datetime.date(2018,3,27),datetime.date(2018,7,24)]:
        Speakers[last_name]="MICHELLE GOLDBERG"
    elif last_name=='RODGERS' and AiredOn.date() in [datetime.date(2018,5,2)]:
        Speakers[last_name]="JENNIFER RODGERS"
    elif last_name=='GREER' and AiredOn.date() in [datetime.date(2018,3,27)]:
        Speakers[last_name]="CHRISTINA GREER"
    elif last_name=='NETHERTON' and AiredOn.date() in [datetime.date(2017,10,3)]:
        Speakers[last_name]='ART NETHERTON'
    elif last_name=='ROBINSON' and AiredOn.date() in [datetime.date(2018,11,6)]:
        Speakers[last_name]="GENE ROBINSON"
    elif last_name=='HEWITT' and AiredOn.date() in [datetime.date(2017,10,5)]:
        Speakers[last_name]="HUGH HEWITT"
    elif last_name=='PEREZ' and AiredOn.date() in [datetime.date(2017,4,18)]:
        Speakers[last_name]="TOM PEREZ"
    elif last_name=="CUMMINGS" and AiredOn.date()==datetime.date(2019,4,30):
        Speakers[last_name]="ELIJAH CUMMINGS"
    elif last_name=='HUNT' and AiredOn.date() in [datetime.date(2016,2,11)]:
        Speakers[last_name]="KASIE HUNT"
    elif last_name=='RYAN' and AiredOn.date() in [datetime.date(2017,3,22)]:
        Speakers[last_name]="PAUL RYAN"
    elif last_name=='MICHELLE' and AiredOn.date()==datetime.date(2017,6,12):
        Speakers[last_name]="MICHELLE"
    elif last_name=='PALADINO' and AiredOn.date()==datetime.date(2018,8,13):
        Speakers[last_name]="CARL PALADINO"
    elif last_name=='CONWAY' and AiredOn.date()==datetime.date(2018,8,13):
        Speakers[last_name]="KELLYANNE CONWAY"
    elif last_name=='AINSLEY' and AiredOn.date() in [datetime.date(2019,3,20),datetime.date(2019,3,21)]:
        Speakers[last_name]='JULIA AINSLEY'
    elif last_name=='CROPPER' and AiredOn.date()==datetime.date(2019,6,5):
        Speakers[last_name]="SUSAN CROPPER"
    elif last_name=='CHAVEZ' and AiredOn.date()==datetime.date(2019,2,14):
        Speakers[last_name]="ARMANDO CHAVEZ"
    elif last_name=='GOSAR' and AiredOn.date()==datetime.date(2019,2,27):
        Speakers[last_name]="REP. PAUL GOSAR"
    elif last_name=='ELLIOTT' and AiredOn.date()==datetime.date(2019,6,5):
        Speakers[last_name]="RENEE ELLIOTT"
    elif last_name=='BOYD' and AiredOn.date()==datetime.date(2019,6,5):
        Speakers[last_name]="DORA BOYD"
    elif last_name=='GUTIERREZ' and AiredOn.date()==datetime.date(2018,3,20):
        Speakers[last_name]="GABE GUTIERREZ"
    elif last_name=='GUTIERREZ' and AiredOn.date()==datetime.date(2016,9,2):
        Speakers[last_name]="MARCO GUTIERREZ"
    elif last_name=='BOYKIN' and AiredOn.date()==datetime.date(2017,2,10):
        Speakers[last_name]='RICHARD BOYKIN'
    elif last_name=='HONIG' and AiredOn.date()==datetime.date(2018,8,2):
        Speakers[last_name]="ELIE HONIG"
    elif last_name=='FOX' and AiredOn.date()==datetime.date(2018,5,25):
        Speakers[last_name]="EMILY JANE FOX"
    elif last_name=='BRANE' and AiredOn.date()==datetime.date(2018,5,29):
        Speakers[last_name]='MICHELLE BRANE'
    elif last_name=='WALSH' and AiredOn.date()==datetime.date(2016,9,1):
        Speakers[last_name]="JOAN WALSH"
    elif last_name=='BUSH' and AiredOn.date()==datetime.date(2016,10,14):
        Speakers[last_name]="BILLY BUSH"
    elif last_name=='RAWLINGS-BLAKE' and AiredOn.date() in [datetime.date(2015,4,27),datetime.date(2015,5,1)]:
        Speakers[last_name]='STEPHANIE RAWLINGS-BLAKE'
    elif last_name=='CARSON' and AiredOn.date() in [datetime.date(2015,11,3),datetime.date(2015,5,1)]:
        Speakers[last_name]='BEN CARSON'

    elif last_name=='FABIAN' and AiredOn.date()==datetime.date(2015,7,6):
        Speakers[last_name]=last_name
    elif last_name=='KARLY' and AiredOn.date()==datetime.date(2015,5,29):
        Speakers[last_name]=last_name
    elif last_name=='MACLAGGAN' and AiredOn.date()==datetime.date(2015,7,17):
        Speakers[last_name]=last_name
    elif last_name=='PEGGY' and AiredOn.date()==datetime.date(2016,8,24):
        Speakers[last_name]=last_name
    elif last_name=='RHONDA' and AiredOn.date()==datetime.date(2016,10,11):
        Speakers[last_name]=last_name
    elif last_name=='DAVE' and AiredOn.date()==datetime.date(2015,1,27):
        Speakers[last_name]=last_name
    elif last_name=='VIRGINIA' and AiredOn.date() in [datetime.date(2015,3,18),datetime.date(2015,3,19)]:
        Speakers[last_name]=last_name


    elif last_name=='HEMMING' and AiredOn.date()==datetime.date(2016,10,27):
        Speakers[last_name]='ANDREW HEMMING'
    elif last_name=='WATERS' and AiredOn.date()==datetime.date(2019,4,9):
        Speakers[last_name]="MAXINE WATERS"
    elif last_name=='COHEN' and AiredOn.date() in [datetime.date(2019,2,28),datetime.date(2019,3,1),datetime.date(2019,3,5),datetime.date(2019,3,6)]:
        Speakers[last_name]="MICHAEL COHEN"
    elif last_name=='MILLS' and AiredOn.date() in [datetime.date(2019,1,7),datetime.date(2019,6,17)]:
        Speakers[last_name]='DANIELLE MOODIE-MILLS'
    elif last_name=='WILSON' and AiredOn.date() in [datetime.date(2019,8,12),datetime.date(2018,3,21)]:
        Speakers[last_name]='RICK WILSON'
    elif last_name=='INGRAM' and AiredOn.date() in [datetime.date(2019,9,25)]:
        Speakers[last_name]='LAURA INGRAM'
    elif last_name=='JORDAN' and AiredOn.date() in [datetime.date(2019,4,2)]:
        Speakers[last_name]='REP. JIM JORDAN'
    elif last_name=='MILLER' and AiredOn.date() in [datetime.date(2019,4,4)]:
        Speakers[last_name]='MATT MILLER'
    elif last_name=='FARRIS' and AiredOn.date() in [datetime.date(2018,1,15)]:
        Speakers[last_name]='ISAAC NEWTON FARRIS JR.'
    elif last_name=='COPPINS' and AiredOn.date() in [datetime.date(2018,1,3)]:
        Speakers[last_name]='MCKAY COPPINS'
    elif last_name=='ALI' and AiredOn.date() in [datetime.date(2019,1,10)]:
        Speakers[last_name]='WAJAHAT ALI'
    elif last_name=='RACHEL' and AiredOn.date() in [datetime.date(2017,2,10)]:
        Speakers[last_name]='RACHEL'
    elif last_name=='MOSKOS' and AiredOn.date()==datetime.date(2015,10,27):
        Speakers[last_name]='PETER MOSKOS'
    elif last_name=='COBB' and AiredOn.date()==datetime.date(2019,2,1):
        Speakers[last_name]="JELANI COBB"
    elif last_name=='REID' and AiredOn.date() in [datetime.date(2015,3,31)]:
        Speakers[last_name]='SEN. HARRY REID'
    elif last_name=='REID' and AiredOn.date() in [datetime.date(2016,6,16),datetime.date(2016,6,17),
        datetime.date(2016,7,29),datetime.date(2015,6,30),datetime.date(2015,5,28),
        datetime.date(2016,8,19),datetime.date(2016,9,1),datetime.date(2016,9,2),datetime.date(2016,9,6),
        datetime.date(2016,10,27),datetime.date(2017,11,17)]:
        Speakers[last_name]="JOY REID"
    elif last_name=='SANDERS' and AiredOn.date() in [datetime.date(2015,12,29),datetime.date(2015,9,14),
        datetime.date(2015,11,19),datetime.date(2016,1,21),datetime.date(2016,2,22),datetime.date(2016,2,26),
        datetime.date(2016,3,3),datetime.date(2016,3,23),datetime.date(2016,5,23),datetime.date(2016,6,2),
        datetime.date(2016,6,22),datetime.date(2016,6,24),datetime.date(2017,9,19),datetime.date(2020,3,12),datetime.date(2020,4,8)]:
        Speakers[last_name]="SEN. BERNIE SANDERS"
    elif last_name=='SANDERS' and AiredOn.date() in [datetime.date(2017,11,3),datetime.date(2017,12,12),datetime.date(2018,12,18)]:
        Speakers[last_name]="SARAH HUCKABEE SANDERS"
    elif last_name=='CLINTON' and AiredOn.date() in [datetime.date(2015,4,17),datetime.date(2015,12,29),
        datetime.date(2015,8,7),datetime.date(2015,9,11),datetime.date(2015,11,20),
        datetime.date(2016,1,6),datetime.date(2016,1,29),datetime.date(2016,2,11),datetime.date(2016,2,15),
        datetime.date(2016,3,21),datetime.date(2016,6,3),datetime.date(2016,8,11),datetime.date(2016,9,14),
        datetime.date(2016,10,10),datetime.date(2016,10,11),datetime.date(2016,1,18),datetime.date(2016,11,4),
        datetime.date(2017,3,20)
        ]:
        Speakers[last_name]="HILLARY CLINTON"

    return Speakers,len(Speakers)==orig_Speakers_len