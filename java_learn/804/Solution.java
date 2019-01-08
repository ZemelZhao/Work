class Solution{
	public int uniqueMorseRepresentations(String[] words){
		String[] cacheMorse = {".-", "-...", "-.-.", "-..", ".", 
			"..-.", "--.", "....", "..", ".---", 
			"-.-", ".-..", "--", "-.", "---", 
			".--.", "--.-", ".-.", "...", "-", 
			"..-", "...-", ".--", "-..-", "-.--", "--.."};
		Map<String, Integer> mapRes = new HashMap();
		for(String tempWord: words){
			String tempMorseRes = "";
			char[] tempCharList = tempWord.toCharArray();
			for(char i: tempCharList){
				tempMorseRes += cacheMorse[i-97];
			}
			if(mapRes.get(tempMorseRes) == null){
				mapRes.put(tempMorseRes, 1);
			}
		}
		return mapRes.size();
	}
}
