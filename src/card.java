
public class card {

	/*
	 *
	 *Card class with card constructor. Will be given a random number between
	 *0-51. Which will determine its value and suit
	 *Cards will have atrib, value, isAnAce
	 *
	 */
	String atrib;
	int value;
	boolean isAnAce;
	
	public card(int map, String suit){
		
		if(map < 4){
			this.atrib = "2";
			this.value = 2;
		}else if(map < 8){
			this.atrib = "3";
			this.value = 3;
		}else if(map < 12){
			this.atrib = "4";
			this.value = 4;
		}else if(map < 16){
			this.atrib = "5";
			this.value = 5;
		}else if(map < 20){
			this.atrib = "6";
			this.value = 6;
		}else if(map < 24){
			this.atrib = "7";
			this.value = 7;
		}else if(map < 28){
			this.atrib = "8";
			this.value = 8;
		}else if(map < 32){
			this.atrib = "9";
			this.value = 9;
		}else if(map < 36){
			this.atrib = "10";
			this.value = 10;
		}else if(map < 40){
			this.atrib = "J";
			this.value = 10;
		}else if(map < 44){
			this.atrib = "Q";
			this.value = 10;
		}else if(map < 48){
			this.atrib = "K";
			this.value = 10;
		}else if(map < 52){
			this.atrib = "A";
			this.value = 11;
		}
		
		this.atrib += suit;
		
		if(this.atrib.contains("A"))
			this.isAnAce = true;
		else
			this.isAnAce = false;
		
	}
	
	
}
