package teste;
 
import java.io.File;
import java.util.Random;
import javax.swing.DefaultListModel;
import weka.classifiers.Classifier;
import weka.core.Instances;
import weka.core.Instance;
import weka.core.converters.ConverterUtils.DataSource;
import weka.classifiers.Evaluation;
import weka.classifiers.bayes.NaiveBayesMultinomial;
import weka.classifiers.bayes.NaiveBayes;
import weka.classifiers.functions.SMO;
import weka.classifiers.trees.J48;
import weka.classifiers.lazy.IBk;
import weka.experiment.ClassifierSplitEvaluator;
import weka.experiment.CrossValidationResultProducer;
import weka.experiment.Experiment;
import weka.experiment.SplitEvaluator;
 
public class ExemploWeka {
 
    public String caminhoDados;
     
    // As instancias do dado
    public Instances dados;
 
    public ExemploWeka(String caminhoDados) {
        this.caminhoDados = caminhoDados;
    }
 
    public void leDados() throws Exception {
 
        DataSource fonte = new DataSource(caminhoDados);
        dados = fonte.getDataSet();
 
        // seta o atributo classe caso o formato de dados nao contenha essa informacao
        if (dados.classIndex() == -1)
            dados.setClassIndex(dados.numAttributes() - 1);
    }
 
    public void imprimeDados() {
 
        // Imprime cada instância (linha) dos dados
        for (int i = 0; i < dados.numInstances(); i++) {
            Instance atual = dados.instance(i);
            System.out.println((i + 1) + ": " + atual + "\n");
        }
    }
 
    //Cria uma instância da árvore J48 e avalia seu desempenho
    public void ENDModified(int n) throws Exception {
 
 
        // Cria um novo END
        NaiveBayesMultinomial nbm = new NaiveBayesMultinomial();
        //SMO svm = new SMO();
        //NaiveBayes nb = new NaiveBayes();
        //J48 tree = new J48();
        //IBk knn = new IBk();
        int a = 1;
        ND nd = new ND();
        nd.setClassifier(nbm);
        //nd.setClassifier(svm);
        //nd.setClassifier(nb);
        //nd.setClassifier(tree);
        //nd.setClassifier(knn);
        END end = new END();
        end.setClassifier(nd);
        end.setSeed(n);
        end.setNumIterations(1);
        // Constrói classificador
        end.buildClassifier(dados);
 
        // Imprime a arvore
        System.out.println(end);
 
        // Avalia o resultado
        /*System.out.println("Avaliacao inicial: \n");
        Evaluation avaliacao;
        avaliacao = new Evaluation(dados);
        avaliacao.evaluateModel(nbm, dados);
        System.out.println("Instancias corretas: " + avaliacao.correct() + "\n");*/
 
        // Avaliacao cruzada (cross-validation)
        System.out.println("Avaliacao cruzada: \n");
        Evaluation avalCruzada;
        avalCruzada = new Evaluation(dados);
        avalCruzada.crossValidateModel(end, dados, 10, new Random(1));
        System.out.println("Instancias corretas: " + avalCruzada.correct() + "\n");
        double[][] confusion = new double[5][5];
        int i = 0;
        int j = 0;
        confusion = avalCruzada.confusionMatrix();
        for(i = 0; i < confusion.length; i++)
        {
            for(j = 0; j < confusion.length; j++)
            {
                System.out.print(confusion[i][j]+"    ");                
            }
            System.out.print("\n");
        }
        System.out.println("Acurácia: "+ avalCruzada.pctCorrect());
        // Neste caso ele imprime o equivalente a uma chamada padrão ao algoritmo, como se
        // estivesse usando a interface gráfica
        /*System.out.println("Chamada de linha de código: \n");
        String[] options = new String[2];
        options[0] = "-t";
        options[1] = caminhoDados;
        System.out.println(Evaluation.evaluateModel(end, options));*/
 
    }
    
     public void Experimento(String caminhoDados) throws Exception {
        System.out.println("Setting up...");
        Experiment exp = new Experiment();
        CrossValidationResultProducer cvrp = new CrossValidationResultProducer();
        SplitEvaluator se = null;
        Classifier sec    = null;
        se  = new ClassifierSplitEvaluator();
        sec = ((ClassifierSplitEvaluator) se).getClassifier();
        cvrp.setNumFolds(10);
        cvrp.setSplitEvaluator(se);
        exp.setResultProducer(cvrp);
        exp.setRunLower(1);
        exp.setRunUpper(2);
        DefaultListModel model = new DefaultListModel();
        File file = new File(caminhoDados);
        model.addElement(file);
        NaiveBayesMultinomial nbm = new NaiveBayesMultinomial();
        exp.setPropertyArray(new Classifier[]{nbm}); 
        exp.setDatasets(model);
        exp.initialize();
        System.out.println("Running...");
        exp.runExperiment();
        System.out.println("Finishing...");
        exp.postProcess();
     }
 
}