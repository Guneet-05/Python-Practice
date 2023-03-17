package FlyWeight.Solution;

import java.util.HashMap;

public class TankTypeFactory {
//	FlyWeight Repository
	static HashMap<String,TankType> map = new HashMap<>();
	
//	FlyWeight factory
	public static TankType getTankType(String type) {
		
		TankType res = null;   
		
		if(map.containsKey(type)) {
			res = map.get(type);
		} else {
			switch(type) {
			case "typeA":
				res = new TankType("typeA",10,20,null);
				break;
			case "typeB":
				res = new TankType("typeB",100,2,null);
				break;
			case "typeC":
				res = new TankType("typeC",50,10,null);
				break;
			default:
				break;
			}
			map.put(type, res);
		}
		
		return res;
	}
}
