public class blackjack {

	/**
	 * @param args
	 */
	public static void main(String[] args) {

		// Create deck
		deck house = new deck();
		house.fillDeck();

		// for(int x = 0; x < 52; x++){
		// System.out.println(house.cards[x].atrib);
		// }

		//Game loop for 8 instances assuming at most 7 cards per match 
		int games = 0;

		while (games < 7) {
			
			hand dealer = new hand("Dealer");
			hand player = new hand("Player");
			
			for (int dealt = 0; dealt < 2; dealt++) {
				dealer.hand[dealt] = house.hit();
				dealer.cardCount++;
				player.hand[dealt] = house.hit();
				player.cardCount++;
			}

			System.out.println("Initial deal");
			player.findValue();
			dealer.findValue();

			player.showHand();
			dealer.showHand();

			while (player.total < 16) {
				player.hand[player.cardCount] = house.hit();
				player.cardCount++;
				player.findValue();
			}

			while (dealer.total < 16) {
				dealer.hand[dealer.cardCount] = house.hit();
				dealer.cardCount++;
				dealer.findValue();
			}
			
			System.out.println("Final hands");
			
			player.showHand();
			dealer.showHand();
			
			if(player.total > 21 || player.total < dealer.total){
				System.out.println("The house always wins");
			}else if(dealer.total > 21 || dealer.total < player.total){
				System.out.println("Player wins");
			}else
				System.out.println("It's a push");
			
			games++;
		}
	}

}
