import string, sys, pprint, itertools

#Source: https://www3.nd.edu/~busiforc/handouts/cryptography/letterfrequencies.html
CONST_LETTERS_SORTED_BY_OCCURENCE = [
    "E", "A", "R", "I", "O", "T", "N", "S", "L", "C", "U", "D", "P", "M", "H", "G", "B", "F", "Y", "W", "K", "V", "X", "Z", "J", "Q",
]

#Few letters have nearly the same probability of occurence. Just swap out these letters here, if you identify the errors -> Trial + Error
#index = plaintext key, value = ciphertext key (mapping is done after frequence analysis below)
guessed_plaintext_mapping = [
    "E", "A", "T", "S", "O", "R", "N", "I", "H", "L", "C", "D", "U", "P", "M", "F", "W", "G", "Y", "B", "K", "V", "X", "Z", "J", "Q",
]

#Configuration
ciphertext = "YYICS JIZIB AGYYX RIEWV IXAFN JOOVQ QVHDL CRKLB SSLYX RIQYI IOXQT WXRIC RVVKP BHZXI YLYZP DLCDI IKGFJ UXRIP TFQGL CWVXR IEZRV NMYSF JDLCL RXOWJ NMINX FNJSP JGHVV ERJTT OOHRM VMBWN JTXKG JJJXY TSYKL OQZFT OSRFN JKBIY YSSHE LIKLO RFJGS VMRJC CYTCS VHDLC LRXOJ MWFYB JPNVR NWUMZ GRVMF UPOEB XKSDL CBZGU IBBZX MLMKK LOACX KECOC IUSBS RMPXR IPJZW XSPTR HKRQB VVOHR MVKEE PIZEX SDYYI QERJJ RYSLJ VZOVU NJLOW RTXSD LYYNE ILMBK LORYW VAOXM KZRNL CWZRA YGWVH DLCLZ VVXFF KASPJ GVIKW WWVTV MCIKL OQYSW SBAFJ EWRII SFACC MZRVO MLYYI MSSSK VISDY YIGML PZICW FJNMV PDNEH ISSFE HWEIJ PSEEJ QYIBW JFMIC TCWYE ZWLTK WKMBY YICGY WVGBS UKFVG IKJRR DSBJJ XBSWM VVYLR MRXSW BNWJO VCSKW KMBYY IQYYW UMKRM KKLOK YYVWX SMSVL KWCAV VNIQY ISIIB MVVLI DTIIC SGSRX EVYQC CDLMZ XLDWF JNSEP BRROO WJFMI CSDDF YKWQM VLKWM KKLOV CXKFE XRFBI MEPJW SBWFJ ZWGMA PVHKR BKZIB GCFEH WEWSF XKPJT NCYYR TUICX PTPLO VIJVT DSRMV AOWRB YIBIR MVWER QJKWK RBDFY MELSF XPEGQ KSPML IYIBX FJPXR ELPVH RMKFE HLEBJ YMWKM TUFII YSUXE VLJUX YAYWU XRIUJ JXGEJ PZRQS TJIJS IJIJS PWMKK KBEQX USDXC IYIBI YSUXR IPJNM DLBFZ WSIQF EHLYR YVVMY NXUSB SRMPW DMJQN SBIRM VTBIR YPWSP IIIIC WQMVL KHNZK SXMLY YIZEJ FTILY RSFAD SFJIW EVNWZ WOWFJ WSERB NKAKW LTCSX KCWXV OILGL XZYPJ NLSXC YYIBM ZGFRK VMZEH DSRTJ ROGIM RHKPQ TCSCX GYJKB ICSTS VSPFE HGEQF JARMR JRWNS PTKLI WBWVW CXFJV QOVYQ UGSXW BRWCS MSCIP XDFIF OLGSU ECXFJ PENZY STINX FJXVY YLISI MEKJI SEKFJ IEXHF NCPSI PKFVD LCWVA OVCSF JKVKX ESBLM ZJICM LYYMC GMZEX BCMKK LOACX KEXHR MVKBS SSUAK WSSKM VPCIZ RDLCF WXOVL TFRDL CXLRC LMSVL YXGSK LOMPK RGOWD TIXRI PJNIB ILTKV OIQYF SPJCW KLOQQ MRHOW MYYED FCKFV ORGLY XNSPT KLIEL IKSDS YSUXR IJNFR GIPJK MBIBF EHVEW IFAXY NTEXR IEWRW CELIW IVPYX CIOTU NKLDL CBFSN QYSRR NXFJJ GKVCH ISGOC JGMXK UFKGR YYIIA CWVSL PGLVH DSAFD TYYRY YEDRG LYXER BJIEV EPLVX BICNE XRIDT IICXD TIXRI PJNIB ILTYS EWCXE IKVRM VXBIC RRHOE ETFHD LGHBG YZCWZ RQXMU ISDIA YKLOQ DWFQD LCIVA KRBYY IDMLB FSNQY STLYT NJUEQ VCFKT SPCTW AYSBB ZXRLG XRBOE LIUSB SRMPF EMJYR WZPCS UMNJG WVXRE RBRVW IBMVV KRBRR HOLCW WIOPJ JJWVS LJCCC LCFEH DSRTR XOXFJ CECXM KKLOM PGIIK HYSUR YAQMV HSHLT KOXSU BYEDX FJPAY YJIUS PSPGI IKODF JXSJW TLASW FXRMN XFJCM YRGBZ PVKMN EXYXF JWSBI QYRRN OGQCE NICWW SBCMZ PSEGY SISKW RNKFI XFJWM BIQNE GOCMZ IXKWR JJEBI QTGIM YJNRV DLYYP SETPJ WIBGM TBINJ MTUEX HRMVR ISSBZ PVLYA VEFIP DXSYH ZWVEU JYXKH YRRUC IKWCI FRDFC LXINX FJKMX AMTUQ KRGXY SEPBH VVDEG SCCGI CUZJI SSPZP VIBFG SYVBJ VVKRB YYIXQ WORAC AMZCH BYQYR KKMLG LXDLC QZSXA CSKEG EWNEX YXFJW SBIQY RRNJM ZEHRM QTNRC YNUVV KRBSF SXICA VVURC BNLKX GYNEC JMWYI NMBSK QORRN FRSXY SUXRI QHRVO GPTNJ YYLIR XBICK LPVSD SLXCE LIWMV PCIUS BSRMP WLEQP VXGMR MKLOQ QTKLK XQMVA YYJIE SDFCM LRQVW KFVKP MSXXS QCXYI DLMZX LDXFN JAKWT JICUM LIRRN XFTLK RXDZC SPXFJ JGKVC HISGF SYJLO PYZXL OHFJR VDMJD RXDLC FNOGE PINEI MLBYM MLRMV TYSPH IIKXS WVTSG IJUYZ XFJEY DWFNJ TKHBJ ULKRB XNIBI QTTPE QQDRR NXFJE YDWUJ IICSQ RRPVX FFKLO HPTGT OHYQD SCXYX DEXCY XYIZY RNEXR IZFJO OXZZK XRIQH RVOGP TNHSH LTKQS RBMFA VSLLZ XDSMP YMWXM KZPVX FJSEC OCYWS BMRJE ELPCI YMWXM PVIZE UFPJB SKYYI PMPJR WRIDJ RVOHY XGEBO KNXLD KCYZR DSFNJ WDVYB RRNFS WELSQ SUJSR IIJGX KKMTU HSWRF EGOEU FPJBS KYYIP PYRVW KRBTE PIGYR VROEP YFGYZ CWUSB SRMPA SXFII CVIYA VWGLC SJLOP YDUSG RRTJP OINYY ICIIJ GXRIP AVVIW LZXEX HUFIQ KRBXY ICPCU KWYYL ICCER RNCQY VLNEK GLCSZ XGEQI RCVME MKXRI ENIPL ERMVH RIPKR GOMLF CMDXJ JIMZT JNEKL VMTBE XHQTF RKJRJ IXRIW FCPCX YWKIN XMBRV NXFJV QOVYQ UGSXW YYMCA YXKSL IYSVZ ORRKL PNEWK FVDLC YIEFI JJIWD LCDYE NLYWU PIFCJ EAKPI NEKKR FTLVG LCSKL OCQFN FOJMW VXRIK FXVOE RIZXM LRMRX MVMXJ INXFJ ISKHY SUHSZ GIVHD LCKFV OWRFJ JKVYX KLOCA TLPNW CJFRO MRMVV CMBJZ XGEQF MIBCU NUINM RHYEX HUMVR DLCDT VOTRZ GXYXF JVHQI YSUPY SIJUM XXMNK XRIWH FYVHQ JVMDA YXRPC STJIC NICUR RNXFJ IIGIP JDEXC ZNXNK KEJUV YGIXR XDLCG FXDSK YYICM BJJAO VCXFW DICUK LKXLT EIYJR MVQMS SQUGV MKGUS GRYSU JYVYR FQORR NKWOI KJUXR ERYYI SVHTL VXIWR LWDIL INLKX QMRPV ACIFE COCIU SBSRM PHOWN FZVSR EQPMR ETJEX DLCKR MXXCX KMNIY XRMNX FJKMX AMTUQ KRYSU XRIJN FRCLM TBLSW QMRKQ CKFEI KRBQF SUIBY YSEKF YWYVF SYKLO WAFII MVMBJ ESHUJ TEXRM YWPIX FFKMC GCWKE SRLJZ XRIPH RRGIA QZQLH MBEMX XMYYM CKPJR XNMRH YXRIP JWSBI GKNIM ELSFX TYKUF ZOVGY NIWYQ YJXYT UMVVO ACFII SXFNE OSGMZ CHTYK UFZOV GYJES HRMVG YAYWU PIPGT EEPXC WDIKW SWZRQ XFJUM CXYST IMEPJ WYVPW NELSW KNEHD LCSNI KVCFC PBMEM KEXWU JIINX FJJGK VCHIS GJMWP SEGYS TEBVW ZJEVP MAVVY RWTLV LEAPF ROERF KMWIU JCPSP JYICS XQFZH DLCQZ SXAFT NMVPE TWMBW RNNMV PBJTP KVCIK LOWAF IIMVM BWSBM DDFYP SSSUX RERDF YMSSQ URYXH ZDTYZ CWKLO KSQWH YVMYY CGSSQ UFOOG QCINS PYYID MLBFS NQYSS ENPWI VRDIB TEXRI PTTOC FCQFA LYRNW MKQMS PSEVZ FTOSX UNCPX SRRRX DIPXF QEGFK FVDLC KRPVA MZCHX SRMLV DQCFK EVP"
encrypted_challenge = "HCIKV RJOX"
#Replace Whitespaces
ciphertext = ciphertext.replace(" ", "").upper() 
encrypted_challenge = encrypted_challenge.replace(" ", "").upper() 
key_length = 6

#Setup
letterToPositionDict = {letter: position for position, letter in enumerate(string.ascii_uppercase)}
positionToLetterDict = dict(enumerate(string.ascii_uppercase))
print(letterToPositionDict)




#Reusable decrypt function for vigenere cipher
def decrypt(ciphertext, key):
    #Decrypt using a key_dict of this format: cipherletter : plaintextletter
    key_stretched = key * (len(ciphertext) // len(key)) + key #Stretch the key to a sufficient length
    
    #print(f"Ciphertext:\n{ciphertext}")
    plaintext = ""
    for i in range (0, len(ciphertext)):
        plaintext_position = (letterToPositionDict[ciphertext[i]] - letterToPositionDict[key_stretched[i]]) % 26 #Add the positions of both letters according to Vigenere defintion
        plaintext += positionToLetterDict[plaintext_position]
    print(f"Plaintext:\n{plaintext}")

def guess_key(most_occuring_letter):
    #We guess that this letter is either an E, S, I because they are the most probably characters (in dictionaries). https://en.wikipedia.org/wiki/Letter_frequency
    #We then calculate the corresponding key by inversing the encryption with our guessed letter
    guess1 = (letterToPositionDict[most_occuring_letter] - letterToPositionDict["E"]) % 26
    guess1 = positionToLetterDict[guess1] #Cast from position to letter

    guess2 = (letterToPositionDict[most_occuring_letter] - letterToPositionDict["S"]) % 26
    guess2 = positionToLetterDict[guess2] #Cast from position to letter

    guess3 = (letterToPositionDict[most_occuring_letter] - letterToPositionDict["I"]) % 26
    guess3 = positionToLetterDict[guess3] #Cast from position to letter

    print(f"Guesses for {most_occuring_letter}: {guess1}, {guess2}, {guess3}")
    return [guess1, guess2, guess3]


#Count cipher letter occurence in ciphertext for each position of the key (as these were encrypted with the same letter)
possible_key_letters = {}
for key_position in range(0,key_length):
    frequenceAnalysis = {}
    cipher_letter_position = key_position
    while(cipher_letter_position < len(ciphertext)):
        cipher_letter = ciphertext[cipher_letter_position]
        if(cipher_letter in frequenceAnalysis):
            frequenceAnalysis.update({cipher_letter : frequenceAnalysis[cipher_letter] + 1})
        else:
            frequenceAnalysis.update({cipher_letter : 1})
        cipher_letter_position += key_length
    frequenceAnalysis = sorted(frequenceAnalysis.items(), key=lambda item: item[1], reverse=True)
    
    possible_key_letters.update({key_position : guess_key(frequenceAnalysis[0][0]) + guess_key(frequenceAnalysis[1][0]) + guess_key(frequenceAnalysis[2][0])})

pprint.pprint(possible_key_letters)



guessed_key = "FREKEY"

#decrypt(ciphertext, guessed_key)
decrypt(encrypted_challenge, guessed_key)



