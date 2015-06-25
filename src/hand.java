
public class hand {
	
	/*
	 * Hand holds an array of cards and will have a total and name
	 * attached.
	 * 
	 * Hand will be initialized with a name.
	 * 
	 */
	
	card hand[];
	int total;
	String name;
	
	public hand(String name){
		
		this.name = name;
		this.total = 0;
		hand = new card[8];

	}
	
	
}
