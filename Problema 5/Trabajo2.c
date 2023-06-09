#include <stdio.h>
#include <stdlib.h>
#include <time.h>


struct N;
typedef struct N Node;

struct N{
	int numero;
	int valor;
	int altura;
	Node *izq;
	Node *der;
};

int altura(Node *n){
	if(n == NULL){
		return 0;
	}else{
		return n->altura;
	}
}

int max(int a, int b){
	return(a >b) ? a : b;
}

Node *createNode(int valor, int numero){
	Node *s = NULL;
	s = (Node *)malloc(sizeof(Node)); //Se asigna la memoria al nodo
	s->numero = numero;
	s->valor = valor; //Asigna el valor del nodo
	s->altura = 1; //Inicializa la altura del nodo en 1
	s->izq = NULL; //Inicializar el puntero del hijo izquierdo apuntando a nulo
	s->der = NULL; //Inicializar el puntero del hijo derecho apuntando a nulo
	return s;			
}

int obtenerBalance(Node *n){
	if(n == NULL){
		return 0;
	}else{
		return altura(n->izq) - altura(n->der);
	}
}

Node *valorMinimoNodo(Node *n){
	Node *actual = n;
	while(actual->izq != NULL){
		actual = actual->izq;
	}
	return actual;
}

Node *rotacionIzquierda(Node* x){
	Node *y = x->der;
	Node *T2 = y->izq;
	y->izq = x;
	x->der = T2;
	x->altura = max(altura(x->izq), altura(x->der)) + 1;
	y->altura = max(altura(y->izq), altura(y->der)) + 1;
	return y;
}

Node *rotacionDerecha(Node *y){
	Node *x = y->izq;
	Node *T2 = x->der;
	x->der = y;
	y->izq = T2;
	y->altura = max(altura(y->izq), altura(y->der)) + 1;
	x->altura = max(altura(x->izq), altura(x->der)) + 1;
	return x;
}

Node *insertarNodo(Node *n, int valor, int numero){
	if (n == NULL)
		return createNode(valor, numero);
	if (valor < n->valor)
		n->izq = insertarNodo(n->izq, valor, numero);
	else if(valor > n->valor)
		n->der = insertarNodo(n->der, valor, numero);
	else
		return n;
	
	//Actualizar el factor de equilibrio del �rbol.
	n->altura = 1 + max(altura(n->izq), altura(n->der));
	int fe = obtenerBalance(n);
	
	//Rotaciones
	if (fe > 1 && valor < n->izq->valor)
		return rotacionDerecha(n);
	if (fe < -1 && valor > n->der->valor)
		return rotacionIzquierda(n);
	if (fe > 1 && valor > n->izq->valor){
		n->izq = rotacionIzquierda(n->izq);
		return rotacionDerecha(n);
	}
	if (fe < -1 && valor < n->der->valor){
		n->der = rotacionDerecha(n->der);
		return rotacionIzquierda(n);
	}
	return n;
}

void inorder(Node *raiz){
	if(raiz != NULL){
		inorder(raiz->izq);
		printf("%d ", raiz->valor);
		inorder(raiz->der);
	}
}

void preorder(Node *raiz){
	if(raiz != NULL){
		printf("%d ", raiz->valor);
		preorder(raiz->izq);
		preorder(raiz->der);
	}
}

void postorder(Node *raiz){
	if(raiz != NULL){
		postorder(raiz->izq);
		postorder(raiz->der);
		printf("%d ", raiz->valor);
	}
}

int buscar(Node *raiz, int valor){
    if(raiz->valor == valor){
        return raiz->numero;
    }else{
        if(valor > raiz->valor && raiz->der != 0){
            return  buscar(raiz->der, valor);
        }else if(valor < raiz->valor && raiz->izq != 0){
            return buscar(raiz->izq, valor);
        }
    }
    return 0;
}


int main(){
	Node *raiz = NULL;
	int cantidad, ch, valor, id;
	while(1){
		printf("\n1.Agregar Trabajadores.\n2.Visualizar numeros identificadores.\n3.Consultar.\n4.Salir\n");
		printf("\nElija una opcion: ");
		scanf("%d", &ch);
		switch(ch){
			case 1:
				srand (time(NULL));
				printf("\nIngrese la cantidad de trabajadores a agregar: ");
				scanf("%d", &cantidad);
				for (int i = 0; i < cantidad; i++){
					valor = rand() % 1001;
					raiz = insertarNodo(raiz, valor, i + 1);
    				}
				break;
				
			case 2:
				printf("\nRecorrido In order: ");
				inorder(raiz);
				printf("\n");
				printf("\nRecorrido Pre order: ");
				preorder(raiz);
				printf("\n");
				printf("\nRecorrido Post order: ");
				postorder(raiz);
				printf("\n");
				break;
			case 3:
				printf("\nIngrese un numero identificador: ");
				scanf("%d", &id);
				printf("Trabajador ");
				printf("%d\n", buscar(raiz, id));
				break;
			case 4:
				exit(0);
				break;
			}
		}
		return(0);
	}