class Tree(object):
  def __init__(self, r, j, o, h):
    self.resultado = r
    self.jugada = j
    self.opciones = o
    self.hijos = h

def inicializar(Arb):
    if not Arb.opciones:
        return
    else:
        chamacos = []
        for i in Arb.opciones:
            print "Trabajando con opcion " + str(i)
            aux = []
            for k in Arb.opciones:
                if k != i:
                    aux.append(k)
            print "El aux es: ", aux
            A = Tree(None, i, aux, [])
            A.hijos = inicializar(A)
            chamacos.append(A)
        return chamacos

def imprimir(Arb):
    if not Arb.hijos:
        print "[." + str(Arb.jugada) + " ]",
    else:
        print "[." + str(Arb.jugada) + " ",
        for h in Arb.hijos:
            imprimir(h)
        print " ]",

def imprimir_opciones(Arb):
    if not Arb.hijos:
        print Arb.jugada,
    else:
        print "[",
        for h in Arb.hijos:
            imprimir_opciones(h),
        print "]"

Opciones = range(1, 4)
print "Opciones: ", Opciones
B = Tree(None,None,Opciones,[])
B.hijos = inicializar(B)
print "Objetos creados con exito!"
print "\n"
imprimir(B)
