package metier;

import java.util.ArrayList;
import java.util.Iterator;
import java.io.Serializable;
import javax.xml.bind.annotation.XmlRootElement;



@XmlRootElement
public class ListeEtu implements Serializable {
	
	
	private ArrayList<EtudiantMetier> ListeEtu; 
	
	// Constructeur
	public ListeEtu() {
		this.ListeEtu =  new ArrayList <EtudiantMetier>();
	}

	// Methode to String
	public String toString() {
		return "ListeEtu [ListeEtu=" + ListeEtu + "]";
	}
	
	
	public ArrayList<EtudiantMetier> getListeEtu() {
		return ListeEtu;
	}

	public void setListeEtu(ArrayList<EtudiantMetier> listeEtu) {
		ListeEtu = listeEtu;
	}

	// M�thode
	public void addToList(EtudiantMetier etu) {
		this.ListeEtu.add(etu);
	}
	
	public void delFromList(String prenom, String nom) {
		Iterator<EtudiantMetier> it = ListeEtu.iterator();
		while (it.hasNext()) {
			EtudiantMetier user = it.next();
			if (user.getPrenom().equals(prenom) && user.getNom().equals(nom)) {
			  it.remove();
			  break;
			}
		}
	}

	
	public ArrayList<EtudiantMetier> afficherTous(){
		return this.ListeEtu;
	}
	
	public void modifyEtu(String ancienPrenom, String ancienNom, String nouveauPrenom, String nouveauNom) {
		Iterator<EtudiantMetier> it = ListeEtu.iterator();
		while (it.hasNext()) {
			EtudiantMetier user = it.next();
			if (user.getPrenom().equals(ancienPrenom) && user.getNom().equals(ancienNom)) {
			  user.setNom(nouveauNom);
			  user.setPrenom(nouveauPrenom);
			  break;
			}
		}
	}
}
