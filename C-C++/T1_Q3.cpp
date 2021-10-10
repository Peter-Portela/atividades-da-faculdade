/*Questão  3 (2,0pontos): Cite  um problema  (situação) da  vida  real em  que  você  usaria  o  conceito de matriz
(variável composta bidimensional homogênea) para auxiliar na solução desse problema.
Dessa forma, elabore um enunciado e respectivo programa em linguagem C em que seja necessário o uso de matrizes.

Faça um programa que crie uma matriz 5x5 que relaciona Exercios X dias da semana de segunda a sexta, 
gere valores aleatorios com o (min) definido pelo usuaio e max de 100, esses valores serão o numero de 
vezes que os exercios deverão ser feitos no dia. Emprima o Resultado para que o usario possa ver.

*/

#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(void)
{
    
    int mat[5][5], a, b, min, max;

    printf("\nInforme o nuemro minimo de exercicios(de 1 até 100): ");
    scanf("%d", &min);
    
    max=101-min;

    printf("\nTabela de exercicios:\n\n");

    srand(time(NULL));

    for (a = 0; a < 5; a++)
    {
        for (b = 0; b < 5; b++)
        {
            mat[a][b] = min+ rand() % max;      
        }
    }

    printf("                S        T        Q        Q        S\n");
    printf("Agachamento");
    for (a = 0; a < 5; a++){
        printf("    %3d  ", mat[0][a]);
    }

    printf("\nAbdominal  ");
    for (a = 0; a < 5; a++){
        printf("    %3d  ", mat[1][a]);
    }
    
    printf("\nFlexao     ");
    for (a = 0; a < 5; a++){
        printf("    %3d  ", mat[2][a]);
    }
    
    printf("\nBarra      ");
    for (a = 0; a < 5; a++){
        printf("    %3d  ", mat[3][a]);
    }

    printf("\nPular corda");
    for (a = 0; a < 5; a++){
        printf("    %3d  ", mat[4][a]);
    }
    
    return 0;
}