package metier;

import java.io.Serializable;

import javax.xml.bind.annotation.XmlRootElement;

@XmlRootElement
public class EtudiantMetier implements Serializable {
	
	private String prenom;
	private String nom;
	
	
	// Constructeur
	public EtudiantMetier(String prenom, String nom) {
		this.prenom = prenom;
		this.nom = nom;
	}

	public EtudiantMetier() {
	}


	// Getters et Setters
	public String getPrenom() {
		return prenom;
	}

	public void setPrenom(String prenom) {
		this.prenom = prenom;
	}

	public String getNom() {
		return nom;
	}

	public void setNom(String nom) {
		this.nom = nom;
	}

	public EtudiantMetier CreerEtu(String leprenom, String lenom) {
		return new EtudiantMetier(leprenom, lenom);
	}

	@Override
	public String toString() {
		return "EtudiantMetier [prenom=" + prenom + ", nom=" + nom + "]";
	}

}
