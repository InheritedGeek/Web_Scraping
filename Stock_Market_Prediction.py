
#By Default Assuming Code and Input files are the same folder
inputFile =  open("cme.20181026.c.pa2", 'r')
inputFile2 =  open("cme.20181026.c.pa2", 'r')
outputFile = open("CL_expirations_and_settlements.txt", 'w')

#Writes to Ouput File
outputFile.write('Futures   Contract   Contract   Futures     Options   Options' + "\n")
outputFile.write('Code      Month      Type       Exp Date    Code      Exp Date' + "\n")
outputFile.write('-------   --------   --------   --------    -------   --------' + "\n")

#Iterate Line by Line to write the first table
for line in inputFile:
    if line[0] == 'B':

        #If of the 'CL' form then parse values
        if line[2:8] == 'NYMCL ':
            futuresCode = line[5:7]
            contractType = line[15:18].lower().capitalize()
            contractMonth = line[18:24]
            settlementDate = line[91:99]
            contractFormattedMonth = line[18:22] + "-" + line[22:24]
            settlementFormattedDate = line[91:95] + "-" + line[95:97] + "-" + line[97:99]
            optionsCode = ""
            optionsExpDate= ""
            if 201812 <= int(contractMonth) <= 202012:
                outline = '{:<7s}   {:<8s}   {:<8s}   {:<10s}   {:<7s}   {:<8s}'.format(futuresCode, contractFormattedMonth, contractType , settlementFormattedDate, "","")
                outputFile.write(outline + "\n")

        #If of the 'LO' form then parse values
        elif line[2:8] == 'NYMLO ':
            futuresCode = 'CL'
            optionsCode = line[5:7]
            contractType = "Opt"
            contractMonth = line[27:33]
            settlementDate = line[91:99]
            contractFormattedMonth = line[27:31] + "-" + line[31:33]
            optionsCode = "LO"
            optionsExpDate = line[91:95]+"-"+line[95:97] +"-"+line[97:99]
            if 201812 <= int(contractMonth) <= 202012:
                outline = '{:<7s}   {:<8s}   {:<8s}   {:<10s}   {:<7s}   {:<8s}'.format(futuresCode, contractFormattedMonth, contractType, "", optionsCode,optionsExpDate)
                outputFile.write(outline + "\n")

#Writes to Ouput File
outputFile.write('\n'+ "\n")
outputFile.write('Futures   Contract   Contract   Strike      Settlement' + "\n")
outputFile.write('Code      Month      Type       Price       Price     '+ "\n")
outputFile.write('-------   --------   --------   --------    -------   '+ "\n")


#Iterate Line by Line to write the second table
for line in inputFile2:
    if line[0:2] == '81':
        futuresCode = ''

        #If of the 'CL' form then parse values
        if line[2:8] == 'NYMCL ':
            futuresCode = line[5:7]
            contractType = line[25:28].lower().capitalize()
            contractMonth = line[29:33]+"-"+line[33:35]
            date = line[29:35]
            strikePrice = 0
            settlementPrice = float(line[108:122])/100

            #Date Requirements
            if 201812 <= int(date) <= 202012:
                outline = '{:<7s}   {:<8s}   {:<8s}   {:<10s}   {:<7s}'.format(futuresCode,contractMonth, contractType, str(("%.2f" % strikePrice)), str(("%.2f" % settlementPrice)))
                outputFile.write(outline + "\n")

        #If of the 'LO' form then parse values
        elif line[2:8] == 'NYMLO ':
            futuresCode = "CL"
            contractType = ''

            if line[28] == 'P':
                contractType = 'Put'
            elif line[28] == 'C':
                contractType = 'Call'

            optionsCode = line[5:7]
            date = line[38:44]
            contractMonth = line[38:42]+"-"+line[42:44]
            strikePrice = float(line[47:54])/100
            settlementPrice = float(line[108:122])/100

            #Date Requirements
            if 201812 <= int(date) <= 202012:
                outline = '{:<7s}   {:<8s}   {:<8s}   {:<10s}   {:>5s}'.format(futuresCode,contractMonth, contractType, str(("%.2f" % strikePrice)), str(("%.2f" % settlementPrice)))
                outputFile.write(outline + "\n")

inputFile.close()
inputFile2.close()
outputFile.close()
