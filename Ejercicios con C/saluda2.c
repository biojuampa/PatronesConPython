#include <stdio.h>

void saluda(char * nombre) {
	printf("Hola, %s!\n", nombre);
}

int main() {
	saluda("Juan Pablo");
	return 0;
}
