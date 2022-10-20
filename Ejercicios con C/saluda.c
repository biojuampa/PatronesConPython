#include <stdio.h>


int main(void) {

	char nombre[] = "nobody";
       
	printf("¿Cuál es tu nombre? ");
	scanf("%s", nombre);
	printf("Hola, %s!\n", nombre);

	return 0;

}
