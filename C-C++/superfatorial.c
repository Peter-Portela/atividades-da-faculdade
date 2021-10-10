#include <stdio.h>

int superfatorial(int num);

int main(void){
int fat = -1;

printf("Informe um numero entre 0 e 10: ");//obs: nos testes só foi até o 6.
scanf("%d",&fat);
if (fat >= 0 && fat <=10)printf("o  superfatorial de %d eh %d", fat, superfatorial(fat));
else printf("Erro, numero informado eh diferente de 0 a 10");

}


int superfatorial(int num) {
int fat = 1;
int i;

 if(num==0) 
 return 1;

 else 
 {   
    for (i = 1; i <= num; i++) 
    {
       fat = fat * i;
    }

 }

return fat * superfatorial(num-1);

}