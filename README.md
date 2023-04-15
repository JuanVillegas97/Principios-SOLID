## ¿Cual es su entrada?
La entrada es el url con la pagina de IMDb con las mejores peliculas calificadas

## ¿Que procesamiento esta haciendo?
Primero hace una request a la pagina de IMDb, despues extrae informacion haciend web scrapping y lo alamcena un diccionario, finalmente crea un csv con la informacion extraida

##¿Cual es su salida?
La salida es el csv con la informacion extraida

Se aplica los fundamentos SOLID:
    Single Responsibility: Hice dos clases en la cad auna de las clases se encarga de una tarea en concreto.
    Open Closed Principle: Las clases pueden tener clases hijas de tal manera que agregar metodos y sobre implementar metodos sobre los ya existentes entonces no necesitan ser modificados
    Liskov Substitution Principle: No logr eidear uin forma de implementar herencia o polimorfismo, pero en dado caso que eso suceda los objetos hijos van a poder rempalzar a los padres
    Interface Segregation Principle, no hay dependencia entre emtodos
    Dependency Inversion las clases usadas son dependiendientes de las clases implementadas


