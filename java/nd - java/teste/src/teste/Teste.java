package teste;
 
public class Teste {
 
    public static String caminhoDados;
 
    public static void main(String[] args) throws Exception {
 
        // Indica onde estão os dados (neste exemplo, eles estão no formato .data)
        int i = 0;
        caminhoDados = "C:\\Users\\Alexandre\\Anaconda\\Examples\\MLiA_SourceCode\\arquivos\\teste_250_chi.arff";
        //caminhoDados = "C:\\Users\\Alexandre\\Anaconda\\Examples\\MLiA_SourceCode\\minicurso\\Bigramas\\2000_chi_bi.arff";
        ExemploWeka exemplo1 = new ExemploWeka(caminhoDados);
 
        exemplo1.leDados();
        exemplo1.ENDModified(33);
        exemplo1.Experimento(caminhoDados);
        /*for(i = 0; i < 100; i++)
        {   
            exemplo1.ENDModified(i);
            System.out.println("Numero: "+i+"\n");
        }*/
    }
}
