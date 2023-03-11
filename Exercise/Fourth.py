SP = 67836.43
RJ =  36678.66
MG =  29229.88
ES =  27165.48
Outros = 19849.53

Elements = [SP,RJ,MG,ES,Outros]
Element_Names = ['SP','RJ','MG','ES','Outros']
Representation = []

Total = SP + RJ + MG + ES + Outros
for i in range(len(Elements)):
    Element = Elements[i]
    Element_Name = Element_Names[i]
    Percentage  = str(round(Element*100/Total,3)) + '%'
    Representation.append(Percentage)
    print('Porcentagem de representação de %s : %s '%(Element_Name,Percentage))