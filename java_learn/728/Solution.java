class Solution{
	public List<Integer> selfDividingNumbers(int left, int right){
		List<Integer> cacheRes = new ArrayList();
		for(int i=left; i<=right; i++){
			int tempInt = i;
			int tempMod = 0;
			boolean judge = true;
			while(tempInt != 0){
				tempMod = tempInt % 10;
				if(tempMod == 0){
					judge = false;
					break;
				}
				else{
					if(i % tempMod != 0){
						judge = false;
						break;
					}
					else{
						tempInt /= 10;
					}
				}
			}
			if(judge){
				cacheRes.add(i);
			}
		}
		return cacheRes;
	}
}
