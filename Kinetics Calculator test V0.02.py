import math
unknown = input("Please enter your requested value: ")
if unknown == "u":
    xt,xt_unit = input("Please enter the final biomass in g/L or mg/L:").split()
    if xt_unit == "g":
        xt = float(xt)*1000
    x0,x0_unit= input("Please enter the initial biomass in g/L or mg/L:").split()
    if x0_unit == "g":
        x0 = float(x0)*1000
    t,t_unit = input("Please enter the fermentation time in hr or day:").split()
    if t_unit == "days":
        t = float(t)*24
    p_conc, p_unit = input("Please enter the product volume:").split()
    if p_unit == "mg":
        p_conc = p_conc/1000
    s0 = input("please enter the substrate concentration at time zero:")
    st = input("Please enter the substrate concentration at the end of fermentation:")

    #specific growth rate
    u = (math.log(xt)-math.log(x0))/t

    #number of generations
    n = 3.33*(math.log10(xt)-math.log10(x0))

    #doubling time
    d_time = math.log(2)/u

    #volumetric production rate
    v_production = float(p_conc)/t

    #specific production rate
    specific_production = float(p_conc)/xt/(t/24)

    #Volumetric cell mass productio rate
    v_c_m = (xt/1000)/t

    #volumetric substrate consumption
    v_s_c = float(s0)-float(st)/t

    #specific rate of substrate consumption
    ssc = v_s_c/v_c_m

    print(str(u) + "    "+ str(n)+"    " + str(d_time)+"    " + str(v_production) + "      "+ str(specific_production) +"    " + str(v_c_m)+ "   " +str( v_s_c)+"   " + str(ssc))
