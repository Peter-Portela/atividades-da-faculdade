#include <stdio.h>
#include <string.h>

int main()
{

    char palavra[20], frase[200];
    int i, j, f, p;
    int quant = 0;
    int x = 0;
    int aux = 0;

    printf("\nDigite uma palavra: \n");
    scanf(" %19[^\n]", &palavra);
    
    printf("\nDigite uma frase: \n");
    scanf(" %199[^\n]", &frase);

    p = strlen(palavra);
    f = strlen(frase);


    for (i = 0; i < f; i++)
    {
    
        if (palavra[0] == frase[i])
        {
       
            aux = i;
        
            x = 0;
           
            for (j = 0; j < p; j++)
            {
         
                if (palavra[j] == frase[aux])
                {
                    x++;
                }
                aux++;
            }

            if (x >= p)
                quant++;
        }
    }

    if (quant >= 1)
        printf("\nA palavra aparece %d vezes na frase", quant);
    else
        printf("\nA palavra nao aparece na frase");
    return 0;
}