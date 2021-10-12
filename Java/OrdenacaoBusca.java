import java.util.Random;
import java.util.Scanner;

public class OrdenacaoBusca {
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
    //Bubble Sort
    static void bubble (int[] v) {
        for (int i=1; i<v.length; i++) {
            for (int j=0; j<v.length-i; j++) {
                if (v[j] > v[j+1]) {
                    int temp = v[j];
                    v[j] = v[j+1];
                    v[j+1] = temp;
                }
            }
        }
    }
    //Busca Simples
    static boolean buscaSimples(int x ,int[] v){
        for(int i=0;i<v.length; i++){
            if (x==v[i]) {
                return true;
            }
        }
        return false;
    }
    //Busca Simples com posiçãoou -1
    static int buscaSimplesPosicao(int x ,int[] v){
        for(int i=0;i<v.length; i++){
            if (x==v[i]) {
                return i;
            }
        }
        return -1;
    }


    public static void main(String[] args) {

        Scanner input= new Scanner(System.in);
        System.out.print("\ndigite o tamanho do vetor: ");
        int n = input.nextInt();
        System.out.print("digite o limite de geracao: ");
        int limite = input.nextInt();
        int[] v = new int[n];
        
        geraVetor(v, limite);
        mostraVetor (v, "Vetor gerado:");
        System.out.print("\ndigite um numero para busca: ");
        int x = input.nextInt();

        if(buscaSimples(x,v)){
            System.out.println("\n"+x+" está no vetor");
        }
        else{
            System.out.println(x+" não está no vetor");
        }

        //(exemplo didatico)eficiencia ruim
        if(buscaSimples(x, v)){
            System.out.println("a primeira ocorrencia de "+x+" foi na posicao "+
            buscaSimplesPosicao(x, v) + " do vetor");
        }
        else{ 
            System.out.println(x+" nao apararece no vetor");
        }
        // melhor desempenho :
        int posicao = buscaSimplesPosicao(x, v);
        if(posicao>-1){
        System.out.println("a primeira ocorrencia de "+x+" foi na posicao "+ 
        posicao+" do vetor");
        }
        else{
            System.out.println(x+" nao apararece no vetor");
        }
        /*System.out.println("ordenando vetor...");
        bubble(v);
        mostraVetor(v, "vetor ordenado:");
        */
     input.close();
    }
}
