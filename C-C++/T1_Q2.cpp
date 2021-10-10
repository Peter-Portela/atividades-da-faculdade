/*Questão 2 - Crie um programa que armazena a tabela acima, em uma matriz,e informa ao usuário o
tempo necessário para percorrer duas cidades (origem e destino) por ele fornecidas,
até o momento em que ele fornecer duas cidades iguais (origem e destino).*/

#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#define DIS 7
int main()
{
    int i, j, origem, destino;
    int soma = 0;
    int ori_des[DIS][DIS];
    char l[DIS];
    char pontoO, pontoD, valor;

    l[0] = 'A';
    l[1] = 'B';
    l[2] = 'C';
    l[3] = 'D';
    l[4] = 'E';
    l[5] = 'F';
    l[6] = 'G';

    /*		A 					B 				   C 				D 					E 						F 				G*/
    /*A*/ ori_des[0][0] = 00;
    ori_des[0][1] = 02;
    ori_des[0][2] = 11;
    ori_des[0][3] = 06;
    ori_des[0][4] = 15;
    ori_des[0][5] = 11;
    ori_des[0][6] = 01;
    /*B*/ ori_des[1][0] = 02;
    ori_des[1][1] = 00;
    ori_des[1][2] = 07;
    ori_des[1][3] = 12;
    ori_des[1][4] = 04;
    ori_des[1][5] = 02;
    ori_des[1][6] = 15;
    /*C*/ ori_des[2][0] = 11;
    ori_des[2][1] = 07;
    ori_des[2][2] = 00;
    ori_des[2][3] = 11;
    ori_des[2][4] = 8;
    ori_des[2][5] = 03;
    ori_des[2][6] = 13;
    /*D*/ ori_des[3][0] = 06;
    ori_des[3][1] = 12;
    ori_des[3][2] = 11;
    ori_des[3][3] = 00;
    ori_des[3][4] = 10;
    ori_des[3][5] = 02;
    ori_des[3][6] = 01;
    /*E*/ ori_des[4][0] = 15;
    ori_des[4][1] = 04;
    ori_des[4][2] = 8;
    ori_des[4][3] = 10;
    ori_des[4][4] = 00;
    ori_des[4][5] = 05;
    ori_des[4][6] = 13;
    /*F*/ ori_des[5][0] = 11;
    ori_des[5][1] = 8;
    ori_des[5][2] = 03;
    ori_des[5][3] = 02;
    ori_des[5][4] = 05;
    ori_des[5][5] = 00;
    ori_des[5][6] = 14;
    /*G*/ ori_des[6][0] = 01;
    ori_des[6][1] = 15;
    ori_des[6][2] = 13;
    ori_des[6][3] = 01;
    ori_des[6][4] = 13;
    ori_des[6][5] = 14;
    ori_des[6][6] = 00;

    //impressão da tabela
    printf("\nO tempo que um determinado aviao dispensa para percorrer o trecho \n");
    printf("entre duas localidades distintas (origem e destino) \n");
    printf("esta disponivel na tabela a seguir.\n");
    printf("     A   B   C   D   E   F   G\n");
    printf("    --------------------------\n");
    for (i = 0; i < DIS; i++)
    {
        printf("%c |", l[i]);
        for (j = 0; j < DIS; j++)
        {
            if (ori_des[i][j] < 10)
            {
                printf(" ");
            }
            printf("  %d", ori_des[i][j]);
        }
        printf("\n");
    }

    printf("\nDigite o ponto de origem desejado, de A a G: ");
    scanf(" %c", &valor);

    pontoO = toupper(valor);

    switch (pontoO)
    {
    case 'A':
        origem = 0;
        break;
    case 'B':
        origem = 1;
        break;
    case 'C':
        origem = 2;
        break;
    case 'D':
        origem = 3;
        break;
    case 'E':
        origem = 4;
        break;
    case 'F':
        origem = 5;
        break;
    case 'G':
        origem = 6;
        break;
    }

    printf("\nDigite o ponto de destino desejado, de A a G: ");
    scanf(" %c", &valor);

    pontoD = toupper(valor);

    switch (pontoD)
    {
    case 'A':
        destino = 0;
        break;
    case 'B':
        destino = 1;
        break;
    case 'C':
        destino = 2;
        break;
    case 'D':
        destino = 3;
        break;
    case 'E':
        destino = 4;
        break;
    case 'F':
        destino = 5;
        break;
    case 'G':
        destino = 6;
        break;
    }

    for (j = 0; j <= destino; j++)
    {
        soma = soma + ori_des[origem][j];
    }

    if (soma == 0)
    {
        printf("\nO destino e a origem sao iguais");
    }
    else
    {
        printf("\nO tempo necessario e de %d horas", soma);
    }

    return 0;
    system("pause");
}
