import java.util.Date;
import java.util.Random;
import java.util.Scanner;

public class Ordenacao {
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
    //Insertion Sort
    static void insertion(int[] v){
       
            for (int j = 1; j < v.length; j++) {
               int temp = v[j];
               int i;
               for (i = j-1; i >= 0 && v[i] > temp; i--) 
                  v[i+1] = v[i];
               v[i+1] = temp;
            }
         }    
    //Selection Sort
    static void selection(int[] v){
        for (int i = 0; i < v.length - 1; ++i) {
            int min = i;
            for (int j = i+1; j < v.length; ++j)
               if (v[j] < v[min])  min = j;
            int temp = v[i]; v[i] = v[min]; v[min] = temp;
         }
      }  

    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        System.out.print("digite o tamanho do vetor: ");
        int n = entrada.nextInt();
        System.out.print("digite o limite de geracao: ");
        int limite = entrada.nextInt();
        int[] v = new int[n];
        geraVetor(v, limite);

        //mostraVetor (v, "Vetor gerado:");
        System.out.println("ordenando vetor...");
        
        //Bubble Sort
        Date date = new Date();
        long ini = date.getTime();
        bubble(v);
        long fim = new Date().getTime();
      
        System.out.println("o Bubble demorou " + (fim-ini) + "ms para tamanho " + n);
      
        //mostraVetor(v, "vetor ordenado:");
        geraVetor(v, limite);
        //Insert Sort
        Date dateIns = new Date();
        long iniIns = dateIns.getTime();
        insertion(v);
        long fimIns = new Date().getTime();

        //mostraVetor(v, "vetor ordenado:");
        System.out.println("o Insertion demorou " + (fimIns-iniIns) + "ms para tamanho " + n);
    
        geraVetor(v, limite);
        //Selection Sort
        Date dateSel = new Date();
        long iniSel = dateSel.getTime();
        selection(v);
        long fimSel = new Date().getTime();
        
        System.out.println("o Selection demorou " + (fimSel-iniSel) + "ms para tamanho " + n);
       
        entrada.close();
    }
}
