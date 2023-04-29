#include <stdio.h>
#include <stdlib.h>
#include <string.h>


typedef struct nodo{
	char valor[40];
	struct nodo *prev;
	struct nodo *next;
	struct nodo *up;
	struct nodo *down1;
	struct nodo *down2;
}Nodo;

typedef struct list{
	char nombre [20];
	Nodo *ini;
	Nodo *final;
}list;

list *crearL(char nombre[20]){
	list *List = (list *) malloc(sizeof(list));
	List->ini = List->final = NULL;
	strcpy(List->nombre, nombre);
	return List;
}

Nodo *creanodo(char nombre[40]){
	Nodo *aux = (Nodo *) malloc(sizeof(Nodo));
	strcpy(aux->valor,nombre);
	aux->prev = NULL;
	aux->next = NULL;
	aux->up = NULL;
	aux->down1 = NULL;
	aux->down2 = NULL;
	return aux;
}

list *listaenlazada1(){
	list *c1 = crearL("lista de cargos");
	Nodo *gerente = creanodo("Gerente");
	Nodo *jefedeproyecto = creanodo("Jefe de proyecto");
	Nodo *programador = creanodo("Programador");
	gerente->next = jefedeproyecto;
	jefedeproyecto->prev = gerente;
	jefedeproyecto->next = programador;
	programador->prev = jefedeproyecto;
	c1->ini = gerente;
	c1->final = programador;
	return c1;	
}

list *listaenlazada2(list *c1){
	list *c2 = crearL("Lista de roles");
	Nodo *analista = creanodo("Analista");
	Nodo *admin = creanodo("Administrador");
	Nodo *auditor = creanodo("Auditor");
	Nodo *prod = creanodo("Produccion");
	c1->ini->down1 = analista;
	analista->up = c1->ini;
	analista->next = admin;
	c1->ini->down2 = admin;
	admin->up = c1->ini;
	admin->next = auditor;
	admin->prev = analista;
	c1->ini->next->down1 = auditor;
	auditor->up = c1->ini->next;
	auditor->next = prod;
	auditor->prev = admin;
	c1->final->down1 = prod;
	prod->up = c1->final;
	prod->prev = auditor;
	c2->ini = analista;
	c2->final = prod;	
	return c2;
	
	
}

list *listaenlazada3(list *c2){
	list *c3 = crearL("Lista de permisos");
	Nodo *edicion = creanodo("Edicion de archivos gerenciales");
	Nodo *progreso = creanodo("Administracion de progreso");
	Nodo *procesos = creanodo("Verificador de Procesos");
	Nodo *empresa = creanodo("Edicion de programas empresariales");
	c2->ini->down1 = edicion;
	edicion->up = c2->ini;
	edicion->next = progreso;
	c2->ini->next->down1 = progreso;
	progreso->next = procesos;
	progreso->prev = edicion;
	progreso->up = c2->ini->next;
	c2->final->prev->down2 = procesos;
	procesos->up = c2->final->prev;
	procesos->next = empresa;
	procesos->prev = progreso;
	c2->final->down1 = empresa;
	empresa->up = c2->final;
	empresa->prev = procesos;
	c3->ini = edicion;
	c3->final = empresa;
	return c3;	
}

list *listaenlazada4(list *c3){
	list *c4 = crearL("Lista de personal");
	Nodo *raul = creanodo("Raul Alvarez");
	Nodo *ibai = creanodo("Ibai Llanos");
	Nodo *ruben = creanodo("Ruben Doblas");
	Nodo *guillermo = creanodo("Guillermo Diaz");
	Nodo *joaquin = creanodo("Joaquin Dominguez");
	Nodo *juan = creanodo("Juan Guarnizo");
	c3->ini->down1 = raul;
	raul->next = ibai;
	raul->up = c3->ini;
	c3->ini->next->down1 = ibai;
	ibai->prev = raul;
	ibai->next = ruben;
	ibai->up = c3->ini->next;
	c3->ini->next->down2 = ruben;
	ruben->up = c3->ini->next;
	ruben->prev = ibai;
	ruben->next = guillermo;
	c3->final->prev->down1 =guillermo;
	guillermo->up =c3->final->prev;
	guillermo->prev = ruben;
	guillermo->next = joaquin;
	c3->final->down1 = joaquin;
	joaquin->up = c3->final;
	joaquin->prev = guillermo;
	joaquin->next= juan;
	c3->final->down2 = juan;
	juan->up = c3->final;
	juan->prev = joaquin;
	c4->ini = raul;
	c4->final = juan;
	return c4;
}	

Nodo *busqueda(list *c1, list *c2, list *c3, list *c4, char nombre[40]){
	Nodo *aux = c1->ini;
	while(strcmp(nombre, aux->valor)!=0){
		aux = aux->next;
		if(aux->next == NULL && strcmp(nombre, aux->valor)!=0){
			aux = aux->down1;
			while(strcmp(nombre, aux->valor)!=0){
				aux = aux->prev;
				if(aux->prev == NULL){
					break;
				}
			} 
		}		
	}

	return aux;
	
}

Nodo *mostrarderecha(Nodo *principal){
	Nodo *ndo = principal;
	if(ndo->down2 != NULL){		
		ndo = ndo->down2;
		printf("\n%s",ndo->valor);
		mostrarderecha(ndo);
		if(ndo->down1 != NULL){
			printf("\n%s",ndo);
			return principal;
		}		
	}
	return principal;
	
}

void mostrarnodos(Nodo *principal){
	Nodo *aux = principal;

	if(principal->up != NULL){
	
		while(aux->up != NULL){
			aux = aux->up;
			printf("\n%s", aux->valor);
		}
		
	}	
	if(principal->down1 != NULL){
	
		while(aux->down1 != NULL){
			aux = mostrarderecha(aux);
			aux = aux->down1;
			printf("\n%s", aux->valor);
		}
	}
}


int main (void){

	list *c1 = listaenlazada1();
	list *c2 = listaenlazada2(c1);
	list *c3 = listaenlazada3(c2);
	list *c4 = listaenlazada4(c3);
	char nombre[40];
	printf("Escriba el nombre de un nodo: ");
	scanf("%[^\n]", &nombre);
	Nodo *main = busqueda(c1,c2,c3,c4,nombre);
	mostrarnodos(main);
	free(c1);
	free(c2);
	free(c3);
	free(c4);
}

