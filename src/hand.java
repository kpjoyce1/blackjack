
public class hand {
	
	/*
	 * Hand holds an array of cards and will have a total and name
	 * attached.
	 * 
	 * Hand will be initialized with a name.s
	 * 
	 */
	
	card hand[];
	int total;
	int cardCount;
	String name;
	
	public hand(String name){
		
		this.name = name;
		this.total = 0;
		this.cardCount = 0;
		hand = new card[8];

	}
	
	public void showHand(){
		System.out.print(this.name + "'s hand: ");

		for(int count = 0; count < this.cardCount; count++){
			System.out.print(this.hand[count].atrib + "  ");
		}
		System.out.println();
		System.out.println("Hand value: " + this.total);
		System.out.println();
		
	}
	
	public void findValue(){
		int currentValue = 0;
		
		for(int count = 0; count < this.cardCount; count++){
			if(this.hand[count].isAnAce){
				if(currentValue + 11 > 21)
					currentValue += 1;
				else
					currentValue += 11;
			}else{
				currentValue += this.hand[count].value;
			}
			this.total = currentValue;
		}
		
	}
	
	
}
