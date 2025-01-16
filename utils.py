

def add_name(content, new_name):
    #new_name = input('Write new item: ')
    if new_name == '' or new_name == '  ':
        return content
    else:
        content.append(new_name)
        return content
    
def sort_cont():
    with open('./names.txt') as file:
        content = file.read()
        content = content.strip().split(',')
        content = [i.replace(' ', '') for i in content]
        content = [i.replace("'", '') for i in content]
    return content

def new_item(new_name):
    content = sort_cont()
    content = add_name(content=content, new_name=new_name)
    list_names = ", ".join(i for i in content)

    with open('./names.txt', 'w') as file:
        file.write(list_names)
    return 'A new item has beed added'


def del_item(rem_item):
    #rem_item = input('Wirte the item to delete: ')
    content = sort_cont()
    content = ", ".join(i for i in content if i != rem_item)
    
    with open('./names.txt', 'w') as file:
        file.write(content)
    return f'The item: {rem_item} has been deleted'



def dict_procces():
    procces = {
        'Custom_Control': 
        '''Head of the area Ing. Edgar Ruíz 
                            \n\nEl deposito que se encuentra frontalmente a la entrada de la bodega es el lugar donde actualmente Aviatour realiza 
                            \nel proceso de nacionalización, allí mismo, a las 8 a.m. aproximadamente se abren las puertas en compañía de los 
                            \nencargados, seguridad y personal de importaciones, es importante resaltar que no se puede abrir la puerta sin que 
                            \ntodos se encuentren en el mismo lugar.

                            \n\nEl personal del depósito se encarga de realizar el desembarque de los contenedores, teniendo en cuenta que a cada 
                            \ncontenedor le pueden pertenecer diferentes facturas y su vez distinto número de cajas asociado a la factura.

                            \n\nDesde el depósito empieza el proceso de carga de cajas, en la que se debe anotar el número de factura y cajas.

                            \n\nUna vez la caja sale del depósito no puede volver a entrar, además, se realizan varios registros fotográficos
                            \ndesde tres diferentes posiciones, esto con el fin de evidenciar las condiciones con las que son recibidas las cajas.

                            \nA partir de este punto las cajas son llevadas a la zona 15
        ''',
        'Picking':
        ''' Head of the area Ing. Pablo Rodríguez
            \n\n
        
        ''',
        'Zones':
        '''
            Zone 1: 
            Zone 2: Modula\n
            Zone 3: Repuestos pesados o grandes\n
            Zone 4: Mesanine (Repuestos livianos, filtros, empaques...)\n
            Zone 5: Líquidos\n
            Zone 6: Farolas y bompers
            Zone 7:
            Zone 8:
            Zone 9:
            Zone 10:
            Zone 11:
            Zone 12
            Zone 13: Backorder o entrega urgente
            Zone 14:
            Zone 15: Importaciones o recibos
        '''

        

    }



    return procces


d = dict_procces()
print(d)