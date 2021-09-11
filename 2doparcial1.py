de  abc  import  ABC , método abstracto

class  Cliente ( ABC ):
    def  __init__ ( self , nom , cel , tel ):
        yo . nombre  =  nom
        yo . cedula  =  cel
        yo . telefono  =  tel

    @ método abstracto
    def  getCedula ( auto ):
        volver a  sí mismo . cédula

class  ClientePersonal ( Cliente ):
    def  __init__ ( self , nom , cel , tel ):
        super (). __init__ ( nom , cel , tel )

    @ propiedad
    def  contrato ( yo ):
        volver a  sí mismo . __contrato
    @ contrato . setter
    def  contrato ( yo , valor ):
        si  valor :
            yo . __contrato = valor
        otra cosa :
            yo . __contrato = 'Sin contrato'

    def  getCedula ( auto ):
        return  super (). getCedula ()


class  InterfaceSistemaPago ( ABC ):
    @ método abstracto
    def  pago ( yo ):
        aprobar

    @ método abstracto
    def  saldo ( yo ):
        aprobar

class  PagoTarjeta ( InterfaceSistemaPago ):
    def  pago ( yo ):
        volver  'Pago Tarjeta'

    def  saldo ( yo ):
        volver  'Saldo Tarjeta'
class  ImplementsPagoContrato ( InterfaceSistemaPago ):
    def  pago ( yo ):
        volver  'Pago contrato'

    def  saldo ( yo ):
        volver  'Saldo contrato'

class  Vendedor :
    def  __init__ ( self , nombre ):
        yo . nombre  =  nombre

    def  modulopago ( yo , contrato ):
        devolución del  contrato . pago ()

pagoContrato  =  ImplementaPagoContrato ()
# imprimir (pagoContrato.pago ())
vendedor1  =  Vendedor ( 'Josué' )
imprimir ( vendedor1 . modulopago ( pagoContrato ))
