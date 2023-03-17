package FlyWeight.Solution;

import java.awt.Image;

//FlyWeight
public class TankType {
	String typeName;
	int power;
	int orgHealth;
	Image img;
	
	TankType(String typeName,int power,int orgHealth,Image img) {
		this.typeName = typeName;
		this.power = power;
		this.orgHealth = orgHealth;
		this.img = img;
	}
}
