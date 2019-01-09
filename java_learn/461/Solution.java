class Solution{
	public int hammingDistance(int x, int y){
		int[] cacheX = new int[32];
		int[] cacheY = new int[32];
		int tempIndex = 0;
		int res = 0;
		for(int i=0; i<32; i++){
			cacheX[i] = 0;
			cacheY[i] = 0;
		}
		while(x != 0){
			cacheX[tempIndex] = x % 2;
			x /= 2;
			tempIndex += 1;
		}
		tempIndex = 0;
		while(y != 0){
			cacheY[tempIndex] = y % 2;
			y /= 2;
			tempIndex += 1;
		}
		for(int i=0; i<32; i++){
			if(cacheY[i] != cacheX[i]){
				res += 1;
			}
		}
		return res;
	}
}
