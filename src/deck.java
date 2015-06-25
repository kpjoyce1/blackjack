
public class deck {

	/*
	 * Deck of 52 cards can be altered to have 2 decks if 
	 * cardsInDeck set to 104, contains hit which is primary
	 * funtion used in blackjack
	 */
	
	int cardsInDeck = 52;
	card cards[];
	int excludes[];
	
	public deck(){
		
		this.cards = new card[cardsInDeck];
		this.excludes = new int[cardsInDeck];
		
	}
	
	public void fillDeck(){
		
		int suitChooser = 0;
		String suit;
		
		for(int cardCount = 0; cardCount < cardsInDeck; cardCount++){
			if(suitChooser == 4)
				suitChooser = 0;
			
			if(suitChooser == 0){
				suit = "C";
			}else if(suitChooser == 1){
				suit = "S";
			}else if(suitChooser == 2){
				suit = "H";
			}else
				suit = "D";
			
			this.cards[cardCount] = new card(cardCount, suit);
			
			suitChooser++;
		}
		
	}
	
	public boolean contains(int card){
		if(this.excludes[card] == 1)
			return true;
		else 
			return false;
		
	}
	
	public card hit(){
		
		boolean existsInDeck = true;
		int random = -1;
		while(existsInDeck){
			random = (int)(Math.random() * 51);
			
			existsInDeck = this.contains(random);
		}
		this.excludes[random]++;
		
		return this.cards[random];
		
	}
	
}
