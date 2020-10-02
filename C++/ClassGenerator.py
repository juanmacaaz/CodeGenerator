# Funcionalidad: Scrip que genera getters, setter y constructores en una Clase C++
# Autor:         Juan Manuel Camara
# Version:       0.0.1

# Variables globales

atributos = []
className = ""
prefijo   = ""

# Funciones

def main():
    about()
    readData()
    clase = createClass()
    print(clase)

def about():
    print("Este script genera una clase CPP con tan solo los atributos")
    print("Creado por github.com/juanmacaaz")
    
def readData():
    print("Introduce el nombre de la clase: ")
    global className
    className = input()
    print("Que prefijo le quieres dar a los atributos? Ej: m_ = m_a, m_b | _ = _a, _b: ")
    global prefijo
    prefijo  = input()
    print("Introduce el attributo de la clase Ej: int a, ClassA* a: (Introduce 0 para finalizar la entrada de atributos)")
    entrada = input()
    if entrada == "0":
        return
    else:
        atributos.append(entrada)
    while entrada != "0":
        entrada = input()
        if entrada != "0":
            atributos.append(entrada)

def createClass():
    clase = "class " + className + "\n"
    clase += "{" + "\n"
    clase += "public: " + "\n"
    clase += "\n"
    clase += createConstructorParam()
    clase += "\n"
    clase += cretaeCostructorCopy()
    clase += "\n\n"
    for line in createGetterSetters():
        clase += line + "\n"
    clase += "\n"
    clase += createAsigmentOperator()
    clase += "\n\n"
    clase += "private:"
    clase += "\n\n"
    for atributo in atributos:
        tipo   = atributo.split(" ")[0]
        nombre = atributo.split(" ")[1]
        clase += "\t" + tipo + " " + prefijo+nombre+";\n"
    clase += "\n"
    clase += "}"
    return clase


def createGetterSetters():
    lines = []
    for atributo in atributos:
        tipo   = atributo.split(" ")[0]
        nombre = atributo.split(" ")[1]
        getter = "\t"+tipo+" get"+nombre.capitalize()+"() const { return "+prefijo+nombre+"; }"
        setter = "\tvoid set"+nombre.capitalize()+"(const "+tipo+"& "+nombre+") { "+prefijo+nombre+" = "+nombre+"; }"
        lines.append(setter)
        lines.append(getter)
    return lines

def createCostructorDefault():
    pass

def cretaeCostructorCopy():
    contructor = "\t"
    contructor += className + "(const " + className + "&" + className[0].lower() + ");"
    return contructor

def createAsigmentOperator():
    contructor = "\t"
    contructor += className + "& operator=(const " + className + "& " + className[0].lower() + ");"
    return contructor

#toDO Si es un puntero no poner &
def createConstructorParam():
    contructor = "\t"
    contructor += className+"("
    for atributo in atributos:
        tipo   = atributo.split(" ")[0]
        nombre = atributo.split(" ")[1]
        contructor += "const " + tipo + "& " + nombre + ", "
    contructor = contructor[0:-2]
    contructor += "): "
    for atributo in atributos:
        tipo   = atributo.split(" ")[0]
        nombre = atributo.split(" ")[1]
        contructor += prefijo+nombre + "("+nombre+"), "
    contructor = contructor[0:-2]
    contructor += r" {}"
    return contructor


# Main run
if __name__ == '__main__':
    main()