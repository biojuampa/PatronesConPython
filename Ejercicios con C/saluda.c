#include <stdio.h>


int main(void) {

	char nombre[100];
       
	printf("¿Cuál es tu nombre? ");
	scanf("%s", nombre);
	printf("Hola, %s!\n", nombre);

	return 0;

}
