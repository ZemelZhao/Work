class Solution{
	public int arrayPairSum(int[] nums){
		List<Integer> cacheNums = new ArrayList();
		int res = 0;
		int tempIndex = 0;
		for(int i:nums){
			cacheNums.add(i);
		}
		cacheNums = quickSort(cacheNums);
		while(tempIndex < cacheNums.size()){
			res += cacheNums.get(tempIndex);
			tempIndex += 2;
		}
		return res;
	}

	public List<Integer> quickSort(List<Integer> data){
		int sizeOfData = data.size();
		List<Integer> cacheLeft = new ArrayList();
		List<Integer> cacheRight = new ArrayList();
		if(sizeOfData <= 1){
			return data;
		}
		else if(sizeOfData == 2){
			if(data.get(0) > data.get(1)){
				cacheLeft.add(data.get(1));
				cacheLeft.add(data.get(0));
				return cacheLeft;
			}
			else{
				cacheLeft.add(data.get(0));
				cacheLeft.add(data.get(1));
				return cacheLeft;
			}
		}
		int flagNum = data.get(0);
		for(int i=1; i<data.size(); i++){
			if(data.get(i) < flagNum){
				cacheLeft.add(data.get(i));
			}
			else{
				cacheRight.add(data.get(i));
			}
		}
		cacheLeft = quickSort(cacheLeft);
		cacheRight = quickSort(cacheRight);
		cacheLeft.add(flagNum);
		for(int i=0; i<cacheRight.size(); i++){
			cacheLeft.add(cacheRight.get(i));
		}
		return cacheLeft;
	}
}
