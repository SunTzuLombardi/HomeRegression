
def get_districts(zipcodes):
    nerural_1 = [98045, 98019, 98014, 98024, 98065, 98027,  98029, 98075, 98077, 98053, 98074, ]
    serural_2 = [ 98022, 98051, 98010, 98092, 98042, 98058, 98059, 98038,]
    fedway_3 = [98002, 98030, 98031, 98032, 98198, 98001,  98003, 98047, 98023,  ]
    vi_4 = [98070,]
    renton_5 = [98146,98166,98168,98057,98178,98056,98055,98158,98148,98055,98138, 98188]
    mercer_6 = [98040,]
    bellvue_7 = [98004, 98005, 98006, 98007, 98008, 98039,]
    redmond_8 = [98011, 98028, 98033, 98034, 98052, 98072]
    nseattle_9 = [98177, 98155, 98133, 98125, 98115, 98117, 98107, 98199, 98119, 98103, 98102, 98112, 98109, 98105,]
    dtseattle_10 = [98122, 98144, 98134, 98106, 98136, 98116, 98126, 98108, 98118, 98164, 98121 ]


    districts = []
    for i in zipcodes:
        if i in nerural_1:
            districts.append('anerural_1')
        elif i in serural_2:
            districts.append('serural_2')
        elif i in fedway_3:
            districts.append('fedway_3')
        elif i in vi_4:
            districts.append('vi_4')
        elif i in renton_5:
            districts.append('renton_5')
        elif i in mercer_6:
            districts.append('mercer_6')
        elif i in bellvue_7:
            districts.append('bellvue_7')
        elif i in redmond_8:
            districts.append('redmond_8')
        elif i in nseattle_9:
            districts.append('nseattle_9')
        elif i in dtseattle_10:
            districts.append('dtseattle_10')  

    return districts
