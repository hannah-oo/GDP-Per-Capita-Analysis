first_line = True
f = open("homicide-rate-cleaned.csv", "w")

for line in open("homicide-rate.csv"):
  #  line = line.rstrip()
  #  line = line.split(",")
    if first_line == True:
        line = line.rstrip()
        line += ",2005-1010 crime rate ratio\n"
        f.write(line)
        first_line = False
    else:
        line = line.rstrip()
        line = line.split(",")

        # get rid of regions 
        if line[0] == "African Region (WHO)":
            line = line
        elif line[0] == "East Asia & Pacific (WB)":
            line = line
        elif line[0] == "Eastern Mediterranean Region (WHO)":
            line = line
        elif line[0] == "Europe & Central Asia (WB)":
            line = line
        elif line[0] == "European Region (WHO)":
            line = line
        elif line[0] == "G20":
            line = line
        elif line[0] == "Latin America & Caribbean (WB)":
            line = line
        elif line[0] == "Middle East & North Africa (WB)":
            line = line
        elif line[0] == "North America (WB)":
            line = line
        elif line[0] == "OECD Countries":
            line = line
        elif line[0] == "Region of the Americas (WHO)":
            line = line
        elif line[0] == "South Asia (WB)":
            line = line
        elif line[0] == "South-East Asia Region (WHO)":
            line = line
        elif line[0] == "Sub-Saharan Africa (WB)":
            line = line
        elif line[0] == "Western Pacific Region (WHO)":
            line = line
        elif line[0] == "World":
            line = line
        elif line[0] == "World Bank High Income":
            line = line
        elif line[0] == "World Bank Low Income":
            line = line
        elif line[0] == "World Bank Lower Middle Income":
            line = line
        elif line[0] == "World Bank Upper Middle Income":
            line = line
            
        else:
            # get 2005 , 2010
            # getting the ratio
            if line[2] == "2005":
                rate05 = float(line[3])
                line.append("NA")
            elif line[2] == "2010":
                rate10 = float(line[3])
                rate = rate10 / rate05
                rate = str(rate)
                line.append(rate)
                

            # writing it in new file
            if line[2] == "2005":
                if line[1] == "":
                    line[1] = "-1"
                line = ",".join(line)
                line += "\n"
                f.write(line)
            elif line[2] == "2010":
                if line[1] == "":
                    line[1] = "-1"
                line = ",".join(line)
                line += "\n"
                f.write(line)
                

f.close()

# now divided by then
# data first found on this website: https://ourworldindata.org/homicides 
