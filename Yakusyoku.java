package main;

import java.util.ArrayList;
import java.util.List;
import java.util.Random;

public class Yakusyoku {


//	private boolean insiderFlg;
//	private boolean masterFlg;


	public int getInt(int ninzu) {


		Random random = new Random();
		int x = random.nextInt(ninzu);
		//System.out.println(x);
		return x;

	}

	public void haibun(int ninzu) {

		List<String> pList = playerList(ninzu);


		int z = getInt(ninzu);
		pList.set(z,"インサイダー");

		int m = getInt(ninzu);

		do {
			m = getInt(ninzu);

			if(z!=m) {
				pList.set(m,"マスター");
			}

		}while(z==m);


		for(int i = 0; i< pList.size();i++) {

			String yakusyoku = pList.get(i);
			if(yakusyoku == "インサイダー") {

				System.out.println("プレイヤー" + (pList.indexOf("インサイダー")+1) +"はインサイダーです");

			}else if(yakusyoku == "マスター") {

				System.out.println("プレイヤー" + (pList.indexOf("マスター")+1) +"はマスターです");

			}else {

				System.out.println("プレイヤー" + (i+1) + "は市民です");
			}


		}

		pList.forEach(System.out::println);

	}
	public List<String> playerList(int playerCount){

		List<String> pList = new ArrayList<String>();

		for(int i = 0; i < playerCount;i++) {

			pList.add(i,"市民");

		}
		return pList;
	}




}
