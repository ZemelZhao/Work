class Solution{
	public int repeatedNTimes(int[] A){
		int N = A.length;
		int res = 0;
		HashMap<Integer, Integer> cache = new HashMap<Integer, Integer>();
		for(int a: A){
			if(cache.get(a) == null){
				cache.put(a, 1);
			}
			else{
				int tempValue = cache.get(a);
				cache.replace(a, tempValue, tempValue+1);
			}
		}
		for(int key: cache.keySet()){
			if(cache.get(key) == N/2){
				res = key;
			}
		}
		return res;
	}
}
