from scrapping_inval import buscar_muebles_inval
from scrapping_homecenter import extraer_muebles_homecenter
from integracion import integrar_scrappers
from modelo import *

if __name__ == "__main__":
    
    # Scrapping
    muebles_inval = buscar_muebles_inval()
    muebles_homecenter = extraer_muebles_homecenter()
    
    lista_integrada = integrar_scrappers(muebles_inval, muebles_homecenter)
    
    print(lista_integrada)
    