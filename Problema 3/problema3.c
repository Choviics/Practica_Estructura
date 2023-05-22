#include <stdlib.h>
#include <stdio.h>

typedef struct _nodo {
   int valor;
   struct _nodo *siguiente;
} tipoNodo;

typedef tipoNodo *pNodo;
typedef tipoNodo *Pila;


void Push(Pila *pila, int v) {
   pNodo nuevo;

   /* Crear un nodo nuevo */
   nuevo = (pNodo)malloc(sizeof(tipoNodo));
   nuevo->valor = v;

   /* Añadimos la pila a continuación del nuevo nodo */
   nuevo->siguiente = *pila;
   /* Ahora, el comienzo de nuestra pila es en nuevo nodo */
   *pila = nuevo;
}

int Pop(Pila *pila) {
   pNodo nodo; /* variable auxiliar para manipular nodo */
   int v;      /* variable auxiliar para retorno */

   /* Nodo apunta al primer elemento de la pila */
   nodo = *pila;
   if(!nodo){ printf("La pila esta vacia");} /* Si no hay nodos en la pila retornamos 0 */
   /* Asignamos a pila toda la pila menos el primer elemento */
   *pila = nodo->siguiente;
   /* Guardamos el valor de retorno */
   v = nodo->valor;
   /* Borrar el nodo */
   free(nodo);
   printf("Se borro el nodo %d\n", v);
}

void MostrarPila(Pila pila) {
   pNodo nodo;/*variables auxiliar*/
   nodo = pila; /* nos posicionamos en el primer nodo */
   if(pila==NULL) {
      printf("La pila esta vacia");
      return;
   }else{
      while(nodo!=NULL) { /* mientras nodo no sea nulo */
         printf("%d ", nodo->valor);
         nodo = nodo->siguiente;
      }
   }
   printf("\n");
}

int main() {
   Pila pila = NULL;

   /*primer nodo de la pila sera 20 y el segundo 10*/
   Push(&pila, 20);
   Push(&pila, 10);
   /*Mustra la pila en orden de atras hacia adelante*/
   MostrarPila(pila);
   /*Sacamos el ultimo elemento de la pila*/
   Pop(&pila);
   Push(&pila, 40);
   Push(&pila, 30);
   MostrarPila(pila);

   Pop(&pila);
   Pop(&pila);
   Push(&pila, 90);
   Pop(&pila);
   Pop(&pila);
   MostrarPila(pila);

   getchar();
   free(pila);
   return 0;
}