/*Questão 5(3,0pontos): Faça um programa, usando o conceito de  funções, para armazenar números
 inteiros  em  dois  vetores  de  10  posições. Dessa  forma,  o  programa  deverá  possuir  uma
função denominada LeEComparaVets  que  será  responsável  por  inserir  os  valores  nos 
dois  vetores  e  em seguida,  deverá  imprimir  todos os valores  (iguais)  presentes  nos  dois  
vetores. Ao  final  a  função  deve retornar à função principal o totalde números que se repetem nos 
dois vetores.*/
#include <stdio.h>
#include <stdlib.h>

int LeEComparaVets()
{
    int vet1[10] = {19, 5, 2, 6, 3, 7, 20, 8, 25, 10};
    int vet2[10] = {5, 0, 19, 4, 25, 5, 80, 19, 34, 5};
    
    int i, j, k;
    int nRepetidos = 0;
    int tRepetidos = 0;

    for (i = 0; i < 10; i++)
    {
        for (j = 0; j < 10; j++)
        {
            if (vet1[i] == vet2[j])
            {
                nRepetidos++;
                tRepetidos++;
            }
        }
        if (nRepetidos > 0)
        {
            printf("\n");
            tRepetidos++;
            for (k = 0; k <= nRepetidos; k++)
            {
                printf("%d ", vet1[i]);
            }
        }
        nRepetidos = 0;
    }
    return tRepetidos;
}

int main()
{
    int repetidos;

    repetidos = LeEComparaVets();

    printf("\n\nO total de numeros que se repetem em algumm momento: %d\n", repetidos);

    return 0;
}