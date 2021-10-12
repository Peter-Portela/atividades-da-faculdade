import java.util.Random;
import java.util.Scanner;

public class MetodosEmVetores {
    //gera o vetor
    static void geraVetor (int[] v, int limite) {
        Random random = new Random();
        for (int i=0; i<v.length; i++) v[i] = random.nextInt(limite);
    }
    //mostra o vetor
    static void mostraVetor(int[] v, String msg) {
        System.out.println(msg);
        for (int i=0; i<v.length; i++) System.out.print(v[i] + " ");
        System.out.println();
    }
    //somaElementos
    static int somaElementos(int[]v){
        int soma = 0;
        for(int i = 0; i<v.length;i++) soma+=v[i];
        return soma; 
    }
    //mediaElementos
    static double mediaElementos(int[]v){
        return (double)(somaElementos(v))/v.length;
    }

    public static void main(String[] args) {

        Scanner input= new Scanner(System.in);
        System.out.print("\ndigite o tamanho do vetor: ");
        int n = input.nextInt();
        System.out.print("\ndigite o limite de geracao: ");
        int limite = input.nextInt();
        int[] v = new int[n];
        
        geraVetor(v, limite);
        mostraVetor (v, "Vetor gerado:");
        System.out.println("a media dos elementos do vetor = "+mediaElementos(v));
    
     input.close();
    }
}
