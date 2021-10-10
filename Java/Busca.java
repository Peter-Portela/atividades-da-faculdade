//exercício 1

//exercício 2
import java.util.Random;
import java.util.Scanner;

public class Questao2 {
    
    //gera o vetor
    static void geraVetor (int[] v) {
        Random random = new Random();
        for (int i=0; i<v.length; i++) v[i] = random.nextInt(99);
    }
    
    //busca multiplo
    static int buscaMultiplo(int x ,int[] v){
        int multiplos = 0;
        for(int i=0 ; i < v.length; i++){
            if(v[i]%x ==0){
                multiplos +=1;
            }
        }
        return multiplos;
    }
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.print("digite o tamanho do vetor: ");
        int n = entrada.nextInt();
        System.out.print("digite um numero: ");
        int x = entrada.nextInt();
        int[] v = new int[n];

        geraVetor(v);

        System.out.println("Vetor:");
        for (int i=0; i<v.length; i++) System.out.print(v[i] + " ");
        System.out.println();

        System.out.println("no vetor tem "+ buscaMultiplo(x ,v) +" multiplo(s) de "+ x);
        
        entrada.close();
    }
}