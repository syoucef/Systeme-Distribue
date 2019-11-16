package ServiceList;
import java.util.ArrayList;

import javax.jws.WebMethod;
import javax.jws.WebParam;
import javax.jws.WebService;

import metier.ListeEtu;
import metier.EtudiantMetier;

@WebService
public class ServiceDeGestion {
	
	// constructeur
	public ServiceDeGestion() {
	}
	
	public ListeEtu te = new ListeEtu();
	
	public int calcul(int n) {
		return 1;
	}
	
	@WebMethod(operationName = "ajouterEtu")
	public void ajouter(@WebParam(name = "prenom")String prenom,@WebParam(name = "nom") String nom) {
		this.te.addToList(new EtudiantMetier(prenom, nom));
	}
	
	@WebMethod(operationName = "afficherToutEtu")
	public ArrayList<EtudiantMetier> afficher(){
		return this.te.afficherTous();
	}

	@WebMethod(operationName = "affichertostring")
	public String toString() {
		return "ServiceDeGestion [afficher()=" + afficher() + "]";
	}

	
	@WebMethod(operationName = "supprimerEtu")
	public void supprimer(@WebParam(name = "prenom")String prenom,@WebParam(name = "nom") String nom) {
		this.te.delFromList(prenom, nom);
	}
	
	@WebMethod(operationName = "modifierEtu")
	public void modifier(@WebParam(name = "ancienPrenom")String ancienPrenom,@WebParam(name = "ancienNom") String ancienNom,
			@WebParam(name = "nouveauPrenom")String nouveauPrenom,@WebParam(name = "nouveauNom") String nouveauNom) {
		this.te.modifyEtu(ancienPrenom, ancienNom, nouveauPrenom, nouveauNom);
	}
}
