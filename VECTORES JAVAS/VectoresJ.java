import java.util.Arrays;

public class VectoresJ {
    public static void main(String[] args) {

        String[] listaVacia = new String[0];

        Integer[] listaConElementos = { 1, 2, 3, 4, 5, 6 };

        System.out.println("Longitud de listaVacia: " + listaVacia.length);
        System.out.println("Longitud de listaConElementos: " + listaConElementos.length);

        if (listaConElementos.length > 0) {
            int primerElemento = listaConElementos[0];
            int elementoCentral = listaConElementos[listaConElementos.length / 2];
            int ultimoElemento = listaConElementos[listaConElementos.length - 1];
            System.out.println("Primer elemento: " + primerElemento);
            System.out.println("Elemento central: " + elementoCentral);
            System.out.println("Último elemento: " + ultimoElemento);
        }

        String[] datosPersonales = new String[5];
        datosPersonales[0] = "Junior";
        datosPersonales[1] = "20";
        datosPersonales[2] = "1.95cm";
        datosPersonales[3] = "Soltero";
        datosPersonales[4] = "Barrio libano";

        String[] itCompanies = { "Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon" };

        String[] nuevaLista = new String[itCompanies.length + 1];
        String nuevaEmpresa = "Xioami";
        for (int i = 0; i < itCompanies.length; i++) {
            if (i == 1) {
                nuevaLista[i] = nuevaEmpresa;
            }
            nuevaLista[i + (i >= 1 ? 0 : 0)] = itCompanies[i];
        }
        itCompanies = nuevaLista;

        String empresaBuscada = "Apple";
        boolean existe = false;
        for (String empresa : itCompanies) {
            if (empresa.equals(empresaBuscada)) {
                existe = true;
                break;
            }
        }
        if (existe) {
            System.out.println(empresaBuscada + " existe en la lista it_companies.");
        } else {
            System.out.println(empresaBuscada + " no existe en la lista it_companies.");
        }

        Arrays.sort(itCompanies);

        for (int i = 0; i < itCompanies.length / 2; i++) {
            String temp = itCompanies[i];
            itCompanies[i] = itCompanies[itCompanies.length - 1 - i];
            itCompanies[itCompanies.length - 1 - i] = temp;
        }

        String[] nuevaListaEmpresas = new String[itCompanies.length - 1];
        for (int i = 1; i < itCompanies.length; i++) {
            nuevaListaEmpresas[i - 1] = itCompanies[i];
        }
        itCompanies = nuevaListaEmpresas;

        itCompanies = new String[0];
    }
}
