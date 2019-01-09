class Solution{
	public int[] diStringMatch(String S){
		int numMin = 0;
		int numMax = S.length();
		int[] res = new int[numMax + 1];
		for(int i=0; i<S.length(); i++){
			if(S.charAt(i) == 'I'){
				res[i] = numMin;
				numMin += 1;
			}
			else{
				res[i] = numMax;
				numMax -= 1;
			}
		}
		res[S.length()] = (S.charAt(S.length()-1) == 'D') ? numMin : numMax;
		return res;
	}
}
