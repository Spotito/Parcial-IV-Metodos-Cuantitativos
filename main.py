import mochila as mo
import RamificacionAcotacion as raac
import Binaria as bi
import EnteraMixta as enm
import EnteraPura as enp
import PlanosCortes as pc

while True: 
    option = int(input("""    
        1. Binaria.py
        2. EnteraMixta.py
        3. EnteraPura.py
        4. mochila.py
        5. PlanosCortes.py
        6. RamificacionAcotacion.py
                       
        Ingrese una opcion > """))

    if option == 1: 
        bi.main()

    if option == 2:
        enm.main()

    if option == 3:
        enp.main()

    if option == 4:
        mo.main()

    if option == 5:
        pc.main()

    if option == 6:
        raac.main()
    
    input("(Presione Enter para continuar)")




