class Solution{
	public int minDeletionSize(String[] A){
		char[][] cacheChar = new char[A.length][(A[0]).length()];
		int iterCount = 0;
		for(int i=0; i<A.length; i++){
			char[] tempCache = A[i].toCharArray();
			for(int j=0; j<A[0].length(); j++){
				cacheChar[i][j] = tempCache[j];
			}
		}
		if(A.length == 1){
			return iterCount;
		}
		else{
			for(int i=0; i<A[0].length(); i++){
				for(int j=1; j<A.length; j++){
					if(cacheChar[j][i] < cacheChar[j-1][i]){
						iterCount += 1;
						break;
					}
				}
			}
		}
		return iterCount;
	}
}
