periodic_table = {
    1: ["H", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "", "He"],
    2: ["Li","Be","","","","","","","","","","","","","B","C","N","O","F","Ne"],
    3: ["Na","Mg","","","","","","","","","","","","","Al","Si","P","S","Cl","Ar"],
    4: ["K","Ca","Sc","Ti","V","Cr","Mn","Fe","Co","Ni","Cu","Zn","","","Ga","Ge","As","Se","Br","Kr"],
    5: ["Rb","Sr","Y","Zr","Nb","Mo","Tc","Ru","Rh","Pd","Ag","Cd","","","In","Sn","Sb","Te","I","Xe"],
    6: ["Cs","Ba","La","Hf","Ta","W","Re","Os","Ir","Pt","Au","Hg","Tl","Pb","Bi","Po","At","Rn"],
    7: ["Fr","Ra","Ac","Rf","Db","Sg","Bh","Hs","Mt","Ds","Rg","Cn","Nh","Fl","Mc","Lv","Ts","Og"],
    "Lanthanides": ["Ce","Pr","Nd","Pm","Sm","Eu","Gd","Tb","Dy","Ho","Er","Tm","Yb","Lu"],
    "Actinides": ["Th","Pa","U","Np","Pu","Am","Cm","Bk","Cf","Es","Fm","Md","No","Lr"]
}

integer_keys = sorted([key for key in periodic_table.keys() if isinstance(key, int)])
string_keys = [key for key in periodic_table.keys() if isinstance(key, str)]

for period in integer_keys:
    print("\t".join(periodic_table[period]))

for period in string_keys:
     print("\t".join(periodic_table[period]))
