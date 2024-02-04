# Funciones para mostrar arte ASCII y otros elementos de UI
def print_headerTower():
    print("""
..........................................................................................................................
..........................................................................................................................
..........................................................................................................................
...............................................:o:,.......................................................................
..............................................:dxkxo:'....................................................................
.............................................:d:lolkxxl;..................................................................
.............................................xd:dlloldxkxc,...............................................................
............................................dklcdcoololddkko:'...........................................................
...........................................dkk:lx:dllololodxkxxo;.........................................................
..........................................,okOddd:dllololooooodkkdc,......................................................
........................................'okkOl:xl:xcodldlooodloodxkxd:'...................................................
.......................................'okkkk:ck:lx:ooldloooocodododxkxl;.................................................
.......................................'lkOkOdoxox:docdldooo:odododddxkkdc,..............................................
.......................................lkOOkOlxd,dd:xocxcdoooooodododdddxkko;............................................
.....................................ckOOkkk::Olxo:xlcxcdood:odoodddddddddxkx,...........................................
.....................................;xOOOkOxlO::kl:klcxcdoldlldoododddddddddxl...........................................
.....................................oOOOOkOlxkckc:kclkcddlddldoodododddddddxd;..........................................
....................................:xOOOOkk:Odok:ckclkcddcxklooodododdddddddxl'.........................................
...................................'oOOOOkOx:0l'dklk:lkcoxcx0oodododdoddddddddd:.........................................
..................................:kOOOOkOo'o0:,kxok:lkcoxcxKolxldoddododddddddo,........................................
.................................'oOOOOOOO:'kk,;Od,dklk:okcdKdlxldoododddddddddxl........................................
..................................:kOOOOkOx,0d'cOl,xklO:lkcoKxcxoodododdddddddddd:.......................................
.................................'dOOOOOkOol0l'lOc,xklO:lkcoKxcddlxldoddodddddddxo,......................................
................................ckOOOOkOO:'x0:'dO:,kxoO:cOclOkcdxcxoodododddddddddc......................................
................................'dOOOOOkOk,,OO'xO;;OxoO:cOlckkloxcddododooddddddddd;.....................................
................................ckOOOOOkOo.c0x'Ok,:OdoO:cOlcxklckloxldoodododddddddl'....................................
...............................,dOOOOOOkOc.oKo:0x'c0odO:cOo:okockolxlddodododddddddd:....................................
...............................ckOOOOOkOk,'k0cl0o'c0o,dO::Oockd:xdcxlodldoddodddddddo,...................................
..............................,dOOOOOOkOd.;0O:o0l'l0l,dO::Od:xx:dx:xdlxlddodododdddddc...................................
..............................ckOOOOOOkOc.lKx'x0c'o0l'dO:;Od;dk:ok:dxcxooxldoddodddddo;..................................
.............................,xOOOOOOkOk,.dKo'kO:'d0c'dO:;kx'oO:lkclkcddcxoodododdddddl'.................................
.............................lkkOOOOOkOx.,k0l.OO;'x0c'dO:,kk'lOccOlckllklddlxoddoddddddc.................................
............................,xOOOOOOOkOl.:0O:c0x,'x0:'x0:,kk;cOl:kd:xdcxolxlddodododdddo,................................
............................lkkOOOOOkOO;.oKx,l0d',kO:'x0:,xk;.cOoxx:dx:dxcxolxldoododdddl................................
...........................;xOkkOOOOkOx.xKd''dKo.;kO;'x0:,xO:.:Oddk:lkclkcdxlxoodododdddd:...............................
...........................lkkOOOOOkkOo.;O0l.x0l.:OO;'x0:'xO:.;kklOcckockolxloxlxoddoddddo,..............................
..........................;xOOOOOOkkOO:.c0Oc.k0c.:0k,,x0c'd0c.,xk;cOokd:xdcxolxlddododddddc..............................
.........................'lkkOOOOkOkOx'.dKk;:OO:.c0k,,x0c'd0l.,dO::kddk:okcoxcddlxoddododdd;.............................
.........................;xkkOkOOkkkOo.'kKd,c0k;.l0x,,x0c'o0l',o0c;xxlOccklckllxlddoxodddddl'............................
........................'lkkOkkOkkkkO:.:O0o.l0x,.oKd,,x0c'o0o,'l0ldO:cOo:xd:xdcxolxlddododdd:............................
........................;xOkOkOOkkkOk,.l00l'dKd'.oKd',x0c'l0d;'c0d,oOc;kxdk:okcdxcxdoxldoodoo,...........................
.......................'lkkkOOOOkkkOd..d0O:.xKo''dKd',x0l'l0d;,:Ox,cOodk:lklcklckloxlddodododl...........................
.......................;xkkOOOOkkkkOl.,k0x;.k0l.,dKo',x0l'c0x:,;Ok;:OdoOc:kd:xd:xdcxolxldoodod;..........................
......................'lkkOOOOOkkkOO;.cO0d'cO0l.,xKo',x0l'c0kc,;kk;;kk;cOoxx:okcoxcoxcdoldododo'..........................
......................:xkOOOOOOkkkOx'.o0Ol'l0Oc.;xKo';x0l'cOkl;,x0c,xO:;kxoOccklckocxloxldoodod:..........................
,,,,,'''''...........'okkOOOOOkkkOOl.,x0Oc'o0k:.;kKl';x0o'cOko:,d0l;dOlxk:cOo:xx:dxcddcxolxldood,........................
;;;;::;;,,,,,''......:xOkOOOOOkkkOO:.:O0k;.dKk:.:k0l';x0o,cOOdc;d0o;oOodOl:kx:okclkllkloxldoldldl'.......................
:;;;;;;;;,,,,,,,'''.,okkOOOOOOkkkOx,.lO0d,.;xKx'cO0l':x0o,ckOxl;o0d;lOx;lOodkccko:xd:xdcxolxloold;........................
;;;;;;;;;;;,,,,,,''':xkkOOOOOOkkk0o.'d00o'.:k0d'cOOl':kKo;:k0kl;lOx:cOk:cOx;lOoxx:okcoxcodcdoldloo,.......................
;;;;;;,,,,,,,,,,,,';okkOOOOOkkkkOOc.;k00l''cO0o'l0Oc':x0o,:k0Oo,lOk::kOc;xk::kxokcckocxocxolxlodldc''''''''...............
,,;;;;;;;;;;,,,,,,,cxkkOOOOOkkkkOk;cOOk:''l00o''l0Oc.;x0o,;x0Oo,cOO:;x0l,dOcxk::ko;dx:oxcodcddcdlld;''''''''''''''''''''''
,;;;;;;;;::;;;;;;;;dkkOOOOOOkkkkOd'.o00x;.o0Oc''o0Oc.:kKo,;xK0o,:kOc'o0o,lOd,oOl;xxlkccklcxlcxlldcdl''''''''''''''''''''''
,,,;;;;;;;::::::::lxkkOOOOOOkkkOOl.'x00d,.d0O:.,o0k:.;x0o,,dK0d,;x0l'lOd,:kx;ckd;oOc:kddd:odcddcdold:'''''''''''''''''''''
',,,,,,,,,;;;;;;;:dkkOOOkOOkkkkOk;.;k00o'.kKk:.,dKk:.;xKo''o00d,,d0o':Ok;;xO:;xk::kdokccklcxlcxlldcoo;''''''''''''''',,,',
''''''',,',,,,,,,cxkkkkOkkkkkkkOd'.cOOO:.:k0x;.,xKk;.;kKo''oKKx,'o0d,;kO:,dOl,oOlxk:cko:dd:dx:odcdocdl,'''''''''''',,,,,,,
''''''',,'''',,,;okkkOOOkkOkkkkOl..o00k;'cO0d'.,xKx,.;kKo''oKKx;.l0x,,d0l'cOd,cOd;lOlxx:lkccxlcxllxcod:',,'',,'''',,,,,,,'
,,,,,,,,,,,,,,,,cxkkkkkkOOkkkkOO;.,x00x,'l00o'.;kKx,.;kKo'.l0Kk;.c0k;'o0o':kk;;kk::kdlkl:xd:dd:odcdocdl,,,,,,,,,,,,,,,,,,,
''',,,,,,,,,,,,;okkkkkOkkkkkkk0x,.;k0Oo''o00l..;OKd,.;kKo'.l0Kk;.cOk:.l0d,,xO:,dOc,dk:kd;oxccxlcxlcxlld:,,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,cxkkkkOOkkkkkkkOo..cOOOc..,x0Oc.:OKd'.;kKo'.l0KO:.:kOc.:Ok;'oOl'lOo,lOl,dk::kodd:od:odcdo;,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,okkkOOOkOOkkkkOO: .o00O;..,k0O;.:O0o'.;k0o'.c00Oc.;k0l.;kO:'lOd':kx,;kd,ckldx:lklcxlcxlcxl,,,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,cxkkkOOOOOkkkkk0x' .x00k'..;O0k,.c00o'.;k0d'.cO0Oc.;x0l.,x0c.:Ox;,xk:,dk:;xxckl:xd:od:odcoxc,,,,,,,,,,,,,,,,
,,,,,,,,,,,;:lxkkkkOOOOkkkkkO0o. ,O00d...c00x'.l00o..;kKd'.:O00c.,d0o''o0o';xk:'oOl'lOl,okc;xxlxccxlcxlcxo::::;;,',,,,,,,,
,,,,,,,,,,,ckOkkkkOOkkOOOOkkOO:  cOOOl...l00d'.o00l..;OKd'.:O00l.'oKd,'o0d,'dOc'cOd,;kd,:kolkc:xd:ox:lxclxolllcc::::;;;;;;
,,'',;;,,;;oOkkkkkkkkOOOkkkkOk' .o0OO:...d0Oo.'o00c..;k0d'.:k00l''oKx;.c0x;'o0o';kk;,dk:,dx:xd;lxccxl:do:dxllllllollcc::;;
,''',:,,cc:dOkkkkkkkOOkkkkkk0d. 'x0Ok,..'x00l.'d00c..;k0d'.;k00o'.l0k:.:kk:.cOx,,dOc'lOl,lklok::xo;ox:lxccxddddddolc;;;'..
,'.';:;:cldkkkkkkkkkkkkkkkkO0c. :kOOx'..,k00c.'x0O:..:O0d'.;k00o'.cOOc.;xOc.:kk:'lOo':kx,;kxcko,oxc:xo:do:dxc;,,..........
;,'',,,,,:coxkkkkkkkkkkkkxdxOxoodxxxxlcclxkxc;:xOOc'':O0d'.;x0Kd,.:O0l.,d0o',dOc':kx;,dk:,okcdx::xo;ox:lxccd;...   .......
;;;;,,,'',okkkkkkkkkkxddodxkOOOOOOOOOOkkkkkkxxxxxkdoodxkd:cxkkd:,ck0o,,o0d,'o0d',dOc'lOo,cko,cklox::xl:do:oo.          ..
,,;,','',cxkkkkkkkxddddxkkkOOOOOOOOOOOOOOOOOOOOOOOOOOOOOkkkkkkkkxxkkxoodkxlcokd:;oko,:kx;;xk:;xx;ckoox:cxccd;            
.''''''''lkkkkkxddddxxkxkkkOOOOO000OOOOO00OOOOOOOOOOOOOOOOOOO000O0000OOOOOOOkkkkkkkxxdxxdodxocoxc:dd:lx:do:oo.           
.........dkxxddddxxxxxkkkkkOOOOOOOOOOOOOOOOOOOOO00OOO0000OO00000OOOOOOOOOOOOOO00OOO00OOOOOOOkxxxxddddododdlod:..         
''......cxddddxxxxxxxxkkkkkOOOOOOOOOOO0OOOOOOO0OOOOOOOOOOOOOOOOOOOOOOOOO000OxxdoooodxkO0OOOOOOkkkkxkkxkkkxkxxxdc.        
,,',''':oddxxxxxxddoldkkkkkOOOOOOOOOOOOOOOOOOOOOOOOOOOO00OOOOOOOOOOO00Oxo:,...      .':ldkOOOkkkkkkkkkkkkkkxxxxd:''..    
;,,,,,,:dxxxxddodklc:dkkkkOOOOOOO0OkxdxkOOOOOOOOOOOOOOOOOOOOOOO0OOO0xl,.                  .:okOkkkkkkkkkkkkx;:dxdc;;'....
'',,,,;lddddllccdxc:;ckxxkkOOOOOOdc,'...'okOOOOOOOOOOOOOOOOOOOO000Od;.                       ':dkkkkkkkkkkkx:.,okxc.......
ooooolodoldoccclxoc:;okxkkOOOOOx:..........xOOOOOOOOOOOOOOOOOOOOOo,         .....              .;okkkkkkkkxxdddxxxd;... ..
'''..,odlldlcccoxcc::xkxxkkkkOd,...........:kOOOOOOOOOOOOOOOOOOx;          ........              .;dkkkkkxlloodddxxl'...  
..   ,olcoocc:cxo::;cxxxxkkkOd,............ dOOOOOOOOOOOOOOOOxl.          .............'.          .cxkkkx::lloolodd:.    
..'';locldl:::okc;:;dkxxxkkkkc...........   oOOOOOOOOOOOOOOk;.            ...........''c,.           ,okkkc,clldl:;cl'    
;;;:odl:oocc:cdd::;:xxxxxkkkk:...... ..     kOkOOOOOOOOOOOd'                  .   ......'.         ...'lxxxooolodl;:oc.   
   .ldcldoccloxo::;cxxxxkkkkOo.            .ldkOOOOOOOOOOOd.                        ........ .,.    ...''',,;cloloddoll:..  
   ,oc,cdoccodxc::,':ddxxkkkkkd,           .;;lkOOOOkkkkOo'...........    .. ........'..,;;,'''..''...','';;'.,;,',;;,,'. . 
 .'cc;';l:;,;:;'.'. .;:clllllll:............'.':ldooooc::::cccc:;,;cccc;'''''',::;''';::;::;::,,,;:;,';:;,;;;;;;'.......'...
;:::;;cllc:::::;'..,;::;'..';::::::;''ccclll:'';cllllc;,;collllc;;:cccc:;;;;;,;::;,;;clcl:;;:::::::::::::::;;;;'.......,,,
;:;,,;ccllcllll;..;loool;'',ccccccc:,',cccccc;,,cc:::::::ccccccc:::::::::::::::::::::clccc::::::::::::::::::::;...'...';;
    """)
          
def print_header():
    print("""
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx         
░▒▓██████████████▓▒░░▒▓█▓▒░▒▓███████▓▒░░▒▓█▓▒░▒██████████████▓▒░░▒▓████████▓▒░▒▓███████▓▒░▒▓███████▓▒░▒▓████████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░   ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░   ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓██████▓▒░ ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░   ░▒▓██████▓▒░   
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░   ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░   ░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒▓█▓▒░░▒▓█▓▒░▒▓█▓▒░▒█▓▒░░▒▓█▓▒░░▒▓█▓▒░▒▓████████▓▒░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░   ░▒▓████████▓▒░
xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx                                                                                                            
     ) (          
  ( /( )\ )        
  )\()|()/((   (    created by: @cheffjoker
|((_)\ /(_))\  )\       powered by: @Dolpin-Mixtral - @LMStudio - @LangChain
|_ ((_|_))((_)((_)          version: 1.0
| |/ /| _ \ \ / /       date: 2024-01-29
  ' < |   /\ V /    license: lisensiado
 _|\_\|_|_\ \_/   
--------------------------------------------------------------------------------------------------------------------                                                                                                              
    """)
