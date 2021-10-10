/*Questão 1(1,5 pontos):Faça um programa em linguagem C para armazenar 15 valores inteiros em um vetor.
Em  seguida  o  programa  deve  organizar  os  dados  que  foram  inseridos  no  vetor  de  forma  que
esses valores fiquem em ordem crescente.Imprima o vetor antes e  depois da ordenação.Obs:  não é permitido
usar  mais  do  que  um  vetor,  use  apenas  variáveis  simples  que  irão  auxiliar  a  ordenação  do vetor. */
#include <stdio.h>
#include <stdlib.h>

int main () {
    

    int i, count, aux, v[15];

    for (i=0; i<15; i++) {
        printf("Informe o %d numero para ser armazenado no vetor: ",i+1);
        scanf("%d", &v[i]);
    }

    printf("\nElementos do vetor: ");
    for (i=0; i<14; i++) {
        printf("%d | ", v[i]);
    }
    
    for (count=0; count<15; count++) {
        for( i = 0; i<15-1 ; i++){
            if(v[i] > v[i + 1]){
                aux = v[i];
                v[i] = v[i + 1];
                v[i + 1] = aux;
            }
        }
    }
    printf("\nElementos do vetor em ordem crescente: ");
    for (i = 0; i < 15; i++)
    {
        printf("%d | ", v[i]);
    }
    printf("\n");

return 0;

}