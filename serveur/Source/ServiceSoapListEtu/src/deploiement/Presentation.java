package deploiement;
import javax.xml.ws.Endpoint;

import ServiceList.ServiceDeGestion;

public class Presentation {

	public static void main(String[] args) {
	String PORT; 
	if (args.length != 0) {
		PORT = args[0];
	}
	else PORT = "8585"; 
	Endpoint.publish("http://localhost:"+PORT+"/?wsdl", new ServiceDeGestion());
	System.out.println("Serveur lancé en écoute sur le port " + PORT);
	System.out.println("Lien du wsdl : http://localhost:"+PORT+"/?wsdl");
	System.out.println("Pour stopper le serveur : ctrl+c");
	}

}
