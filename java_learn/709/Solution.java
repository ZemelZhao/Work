class Solution{
	public String toLowerCase(String str){
		char[] cache = str.toCharArray();
		for(int i=0; i<cache.length; i++){
			if(cache[i] >= 65 && cache[i] <= 90){
				cache[i] += 32;
			}
		}
		String res = String.valueOf(cache);
		return res;
	}
}
