class Solution{
	public int numJewelsInStones(String J, String S){
		char[] cacheRes = S.toCharArray();
		int res = 0;
		for(int i=0; i<S.length(); i++){
			if(J.indexOf(String.valueOf(cacheRes[i]))>=0){
				res += 1;
			}
		}
		return res;
	}
}
